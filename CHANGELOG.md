# Changelog

## [1.0.0] - 2026-02-20

### Added
- `NiaFaker` class with locale-based generation
- 7 providers: person, phone, address, company, mobile_money, national_id, currency
- 10 African locales: Tanzania, Kenya, Nigeria, South Africa, Ghana, Uganda, Rwanda, Ethiopia, Egypt, Morocco
- Mobile money provider (M-Pesa, MTN MoMo, Airtel Money, etc.) — unique to NiaFaker
- National ID generator with structurally valid formats per country
- Currency formatter with locale-specific symbols and separators
- Phone numbers with real carrier prefixes (Safaricom, Vodacom, MTN, etc.)
- 307 tests across all providers and locales
- CI/CD with tests on Python 3.9–3.13 before PyPI publish
- Type hints and PEP 561 `py.typed` marker

### Changed
- Replaced `setup.py` with `pyproject.toml`
- Replaced `pkg_resources` with `importlib.resources`
- Restructured from flat generators to provider pattern
- Minimum Python version raised to 3.9

### Fixed
- Data files now included in repository (were previously gitignored)
- Added missing MIT LICENSE file

### Backward Compatibility
- `generate_name()`, `generate_city()`, `generate_address()`, etc. still work — they delegate to `NiaFaker` with a random locale

## [0.1.1] - 2024

- Initial release with basic name, city, address, and phone generation
