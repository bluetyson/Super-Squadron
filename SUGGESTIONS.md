# Suggestions for Future Improvements

This document provides recommendations for further enhancing the Super Squadron codebase.

## High Priority

### 1. Add Formal Unit Tests
**Why**: Automated tests prevent regressions and document expected behavior.

**Recommendation**: Use pytest framework
```python
# tests/test_roll.py
import pytest
from super_squadron.roll import roll_effects, roll_ap

def test_roll_effects_range():
    """Test that roll_effects returns values in expected range."""
    for _ in range(100):
        result = roll_effects(2, 6)
        assert 2 <= result <= 12

def test_roll_ap_simple_dice():
    """Test roll_ap with simple dice notation."""
    result = roll_ap('2d6')
    assert isinstance(result, int)
    assert 2 <= result <= 12

def test_roll_ap_character_stats():
    """Test roll_ap preserves character stat references."""
    assert roll_ap('Strength+Agility') == 'Strength+Agility'
```

### 2. Add Type Hints
**Why**: Improves IDE support, catches type errors early, serves as documentation.

**Example**:
```python
from typing import Dict, Union

def roll_effects(number: int, dice_sides: int) -> int:
    """Roll multiple dice and sum the results."""
    roll_total = 0
    for roll in range(number):
        dice_roll = np.random.randint(1, dice_sides + 1)
        roll_total = roll_total + dice_roll
    return roll_total

def roll_ap(deviceap: str) -> Union[str, int]:
    """Calculate Action Points for a device."""
    # ... implementation
```

### 3. Configuration File
**Why**: Separates configuration from code, makes paths easier to manage.

**Recommendation**: Create `config.py`
```python
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

POWER_DETAILS_FILE = os.path.join(DATA_DIR, 'power_details.csv')
GIMMICKS_FILE = os.path.join(DATA_DIR, 'Gimmicks.csv')

# Game constants
MIN_STATS_TOTAL = 60
LUCK_THRESHOLD = 11
```

## Medium Priority

### 4. Replace Print with Logging
**Why**: More flexible than print, can be configured to different levels and outputs.

**Example**:
```python
import logging

logger = logging.getLogger(__name__)

def roll_main_statistics(Statistics):
    stats_total = 0
    while stats_total <= 60:
        stats_total = 0
        for index, key in enumerate(Statistics.keys()):
            if index < 5:
                Statistics[key] = roll_statistic()
                stats_total = stats_total + Statistics[key]
                logger.debug(f"{key}: {Statistics[key]}")
        logger.debug(f"Total: {stats_total}")
    return Statistics
```

### 5. Character Dictionary Validation
**Why**: Prevents errors from malformed character data.

**Recommendation**: Use pydantic or dataclasses
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class CharacterStatistics:
    Strength: int
    Agility: int
    Charisma: int
    Intelligence: int
    Stamina: int
    PublicStanding: int
    Ego: int
    Luck: int

@dataclass
class Character:
    Statistics: CharacterStatistics
    Origin: dict
    Powers: dict
    # ... other fields
```

### 6. Refactor powers.py
**Why**: File is very large (1400+ lines), hard to navigate and maintain.

**Recommendation**: Split into multiple files
```
super_squadron/
  powers/
    __init__.py
    base.py           # PowerBase class
    enhancement.py    # Enhanced* powers
    generation.py     # *Generation powers
    control.py        # *Control powers
    projection.py     # Astral Projection, etc.
    combat.py         # Heightened Attack/Defense, etc.
```

## Lower Priority

### 7. Caching for CSV Data
**Why**: Currently reads CSV on every import, slower than needed.

**Example**:
```python
_powers_dict_cache = None

def get_powers_dict():
    global _powers_dict_cache
    if _powers_dict_cache is None:
        df = pd.read_csv(POWER_DETAILS_FILE, low_memory=False)
        _powers_dict_cache = {}
        for index, row in df.iterrows():
            _powers_dict_cache[row['Power']] = PowerBase(...)
    return _powers_dict_cache
```

### 8. Enhanced Documentation
**Why**: Makes it easier for new contributors to understand the code.

**Recommendations**:
- Add usage examples to docstrings
- Create a developer guide
- Document the game mechanics and how they map to code
- Add diagrams showing class relationships

### 9. Input Validation in Power Classes
**Why**: Many power classes access Character dict without validation.

**Example**:
```python
class AirGeneration(PowerBase):
    def __init__(self, Character):
        # Validate required keys exist
        required_keys = ['Statistics', 'Powers']
        for key in required_keys:
            if key not in Character:
                raise ValueError(f"Character missing required key: {key}")
        
        # Validate Statistics subkeys
        required_stats = ['Stamina', 'Agility']
        for stat in required_stats:
            if stat not in Character['Statistics']:
                raise ValueError(f"Character.Statistics missing: {stat}")
        
        # Continue with initialization...
```

### 10. Performance Optimization
**Why**: Some operations could be more efficient.

**Examples**:
- Use `dict.get()` with defaults instead of multiple if statements
- Pre-compile regex patterns if using regex
- Consider using numpy arrays for bulk dice rolling
- Profile code to find actual bottlenecks

## Development Workflow Improvements

### 11. Pre-commit Hooks
Set up pre-commit hooks for:
- Code formatting (black)
- Import sorting (isort)
- Linting (flake8 or ruff)
- Type checking (mypy)

### 12. Continuous Integration
Set up GitHub Actions for:
- Running tests on every PR
- Checking code coverage
- Linting and type checking
- Building and testing on multiple Python versions

### 13. Code Coverage
Aim for >80% test coverage, track with codecov.io or similar.

## Implementation Priority

1. **Start with**: Unit tests (#1) - Highest value, prevents regressions
2. **Then add**: Type hints (#2) - Good developer experience improvement
3. **Next**: Configuration (#3) and Logging (#4) - Better code organization
4. **Finally**: Refactoring (#6), Caching (#7), and other optimizations

## Questions to Consider

1. What Python versions should be supported? (Currently >=3.6)
2. Is there a need for API stability or can interfaces change freely?
3. Are there performance requirements for character generation?
4. Will this be distributed as a package on PyPI?
5. Are there plans for a GUI or web interface?

## Getting Started with Improvements

To implement these improvements:

1. Create a new branch for each major improvement
2. Start with tests - they'll help catch issues during refactoring
3. Make changes incrementally, testing after each change
4. Update documentation as you go
5. Get code reviews before merging

Remember: These are suggestions, not requirements. Prioritize based on your needs and available time.
