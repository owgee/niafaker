# NiaFaker

[![Tests](https://github.com/owgee/niafaker/actions/workflows/test.yml/badge.svg)](https://github.com/owgee/niafaker/actions/workflows/test.yml)
[![PyPI version](https://img.shields.io/pypi/v/niafaker.svg)](https://pypi.org/project/niafaker/)
[![Python versions](https://img.shields.io/pypi/pyversions/niafaker.svg)](https://pypi.org/project/niafaker/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Fake data generator localized for African regions. Names, phone numbers, addresses, mobile money accounts, national IDs, companies, and currencies — all culturally accurate for 10 major African economies.

**Why NiaFaker?** Standard fake data libraries generate Western-centric data. NiaFaker generates Swahili names, M-Pesa numbers, NIDA IDs, Safaricom carrier prefixes, and Tanzanian Shilling amounts. If you're building or testing software for African markets, this is for you.

## Installation

```bash
pip install niafaker
```

## Quick Start

```python
from niafaker import NiaFaker

fake = NiaFaker("tz")  # Tanzania

fake.name()            # "Baraka Kimaro"
fake.phone()           # "+255754832109"
fake.mobile_money()    # {"provider": "M-Pesa", "number": "+255754832109"}
fake.national_id()     # "19901234-12345-00001-01"
fake.company()         # "Bakhresa Holdings"
fake.amount()          # "TSh 425,000"
fake.city()            # "Dar es Salaam"
fake.address()         # "1234 Samora Avenue, Dodoma, Dodoma"
```

## Supported Countries

| Code | Country | Currency | Mobile Money | National ID |
|------|---------|----------|-------------|-------------|
| `tz` | Tanzania | TZS | M-Pesa, Tigo Pesa, Airtel Money, Halopesa | NIDA |
| `ke` | Kenya | KES | M-Pesa, Airtel Money, T-Kash | Kenya National ID |
| `ng` | Nigeria | NGN | OPay, PalmPay, Moniepoint | NIN |
| `za` | South Africa | ZAR | FNB eWallet, Standard Bank Instant Money, Vodapay | SA ID Number |
| `gh` | Ghana | GHS | MTN MoMo, Vodafone Cash, AirtelTigo Money | Ghana Card |
| `ug` | Uganda | UGX | MTN MoMo, Airtel Money | NIN |
| `rw` | Rwanda | RWF | MTN MoMo Rwanda, Airtel Money | Irangamuntu |
| `et` | Ethiopia | ETB | telebirr, M-Pesa | Fayda Digital ID |
| `eg` | Egypt | EGP | Vodafone Cash, Orange Money, WE Pay | Bitaqa |
| `ma` | Morocco | MAD | Maroc Telecom m-wallet, Orange Money, Inwi Money | CNIE |

## API Reference

### NiaFaker Class

```python
from niafaker import NiaFaker

fake = NiaFaker("ke")  # Pass any supported locale code
```

#### Person
| Method | Returns | Example |
|--------|---------|---------|
| `fake.name()` | Full name | `"Wanjiku Kamau"` |
| `fake.name(gender="male")` | Gendered name | `"Ochieng Otieno"` |
| `fake.first_name()` | First name only | `"Amina"` |
| `fake.last_name()` | Last name only | `"Mwangi"` |
| `fake.email()` | Email address | `"wanjiku.kamau42@gmail.com"` |
| `fake.email(domain="company.co.ke")` | Custom domain | `"wanjiku.kamau42@company.co.ke"` |

#### Phone
| Method | Returns | Example |
|--------|---------|---------|
| `fake.phone()` | Phone number | `"+254712345678"` |
| `fake.phone(carrier="Safaricom")` | Carrier-specific | `"+254712345678"` |
| `fake.carrier()` | Carrier name | `"Safaricom"` |

#### Address
| Method | Returns | Example |
|--------|---------|---------|
| `fake.city()` | City name | `"Nairobi"` |
| `fake.region()` | Region/county | `"Kiambu"` |
| `fake.address()` | Full address | `"123 Kenyatta Avenue, Nairobi, Nairobi, 00100"` |
| `fake.country()` | Country name | `"Kenya"` |

#### Company
| Method | Returns | Example |
|--------|---------|---------|
| `fake.company()` | Company name | `"Safaricom PLC"` |
| `fake.company_type()` | Entity type | `"Ltd"` |
| `fake.registration_number()` | Reg number | `"PVT-0012345"` |

#### Mobile Money
| Method | Returns | Example |
|--------|---------|---------|
| `fake.mobile_money()` | Account dict | `{"provider": "M-Pesa", "number": "+254712345678"}` |
| `fake.mobile_money_provider()` | Provider name | `"M-Pesa"` |
| `fake.transaction_id()` | Transaction ref | `"QE1234567890"` |

#### National ID
| Method | Returns | Example |
|--------|---------|---------|
| `fake.national_id()` | ID number | `"12345678"` |
| `fake.national_id_name()` | ID system name | `"Kenya National ID"` |

#### Currency
| Method | Returns | Example |
|--------|---------|---------|
| `fake.currency_code()` | ISO code | `"KES"` |
| `fake.currency_name()` | Full name | `"Kenyan Shilling"` |
| `fake.currency_symbol()` | Symbol | `"KSh"` |
| `fake.amount()` | Formatted amount | `"KSh 125,000"` |
| `fake.amount(min_val=10, max_val=100)` | Custom range | `"KSh 42"` |

### Backward-Compatible Functions

These pick a random country each time — useful for quick prototyping:

```python
from niafaker import generate_name, generate_phone_number, generate_city

generate_name()          # random country
generate_phone_number()  # random country
generate_city()          # random country
```

### Listing All Locales

```python
NiaFaker.locales()
# {'tz': 'Tanzania', 'ke': 'Kenya', 'ng': 'Nigeria', ...}
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License. See [LICENSE](LICENSE).

## Author

**Owden Godson** — [owden.site](https://owden.site) | [GitHub](https://github.com/owgee)
