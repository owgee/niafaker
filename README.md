# NiaFaker

[![Tests](https://github.com/owgee/niafaker/actions/workflows/test.yml/badge.svg)](https://github.com/owgee/niafaker/actions/workflows/test.yml)
[![PyPI version](https://img.shields.io/pypi/v/niafaker.svg)](https://pypi.org/project/niafaker/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Fake data generator localized for African regions. Names, phone numbers, mobile money, national IDs, and more — culturally accurate for 10 African economies.

## Install

```bash
pip install niafaker
```

## Usage

```python
from niafaker import NiaFaker

fake = NiaFaker("tz")  # Tanzania

fake.name()            # "Baraka Kimaro"
fake.phone()           # "+255754832109"
fake.mobile_money()    # {"provider": "M-Pesa", "number": "+255754832109"}
fake.national_id()     # "19901234-12345-00001-01"
fake.company()         # "Bakhresa Holdings"
fake.amount()          # "TSh 425,000"
fake.address()         # "1234 Samora Avenue, Dodoma, Dodoma"
```

## Supported Countries

`tz` Tanzania · `ke` Kenya · `ng` Nigeria · `za` South Africa · `gh` Ghana · `ug` Uganda · `rw` Rwanda · `et` Ethiopia · `eg` Egypt · `ma` Morocco

```python
NiaFaker.locales()  # {'tz': 'Tanzania', 'ke': 'Kenya', ...}
```

## What You Can Generate

**Person** — `name()`, `first_name()`, `last_name()`, `email()`
**Phone** — `phone()`, `phone(carrier="Safaricom")`, `carrier()`
**Address** — `city()`, `region()`, `address()`, `country()`
**Company** — `company()`, `company_type()`, `registration_number()`
**Mobile Money** — `mobile_money()`, `mobile_money_provider()`, `transaction_id()`
**National ID** — `national_id()`, `national_id_name()`
**Currency** — `currency_code()`, `currency_symbol()`, `amount()`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Adding a new country is just 7 JSON files and one line in the config.

## License

MIT — [Owden Godson](https://owden.site)
