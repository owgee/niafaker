# Contributing to NiaFaker

Thanks for your interest in making NiaFaker better.

## Adding a New Country

1. Create a new directory: `niafaker/locales/{two_letter_code}/`
2. Add all 7 JSON files following the existing locale format (see `niafaker/locales/tz/` as reference)
3. Add the locale code to `SUPPORTED_LOCALES` and `LOCALE_NAMES` in `niafaker/providers/__init__.py`
4. Add tests — the parametrized test suite will automatically cover your new locale
5. Run `pytest tests/ -v` and ensure all tests pass

## Adding a New Provider

1. Create a new file in `niafaker/providers/`
2. Inherit from `BaseProvider`
3. Add the corresponding JSON data file to each locale directory
4. Expose methods on the `NiaFaker` class in `niafaker/__init__.py`
5. Write tests in `tests/test_{provider}.py`

## Data Guidelines

- Names should be culturally accurate — include names from major ethnic groups
- Phone carrier prefixes must be real and current
- At least 30 first names per gender, 30 last names per locale
- At least 15 cities and all administrative regions per locale

## Running Tests

```bash
pip install pytest
pip install -e .
pytest tests/ -v
```

## Code Style

- Type hints on all functions
- Docstrings for public methods
- Python 3.9+ features are fine
