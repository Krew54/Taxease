easytax/
│
├── app/
│   ├── main.py
│   ├── core/                     # App config, DB, settings, utils
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   │
│   ├── models/                   # (optional central registry for imports)
│   │   ├── __init__.py
│   │   └── base.py
│   │
│   ├── features/
│   │   ├── profile/
│   │   │   ├── models.py         # SQLAlchemy models for Profile
│   │   │   ├── schemas.py        # Pydantic models for Profile
│   │   │   ├── routes.py         # FastAPI routers (endpoints)
|   |   |   ├── user_auth.py      # User authentication
│   │   │   ├── crud.py           # Business logic
│   │   │   └── __init__.py
│   │   │
│   │   ├── documents/
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── routes.py
│   │   │   ├── crud.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── tax_computation/
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── routes.py
│   │   │   ├── crud.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── tax_filing/
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── routes.py
│   │   │   ├── crud.py
│   │   │   └── __init__.py
│   │
│   └── __init__.py
│
└── requirements.txt