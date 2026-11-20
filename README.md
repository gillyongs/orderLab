# OrderLab

Python CI/CD 실습 프로젝트 (Ruff, Pytest, GitHub Actions)

## 프로젝트 구조

```
orderlab-project/
├── .github/workflows/ci.yml
├── orderlab/
│   ├── __init__.py
│   ├── pricing.py        # Level 1-2
│   ├── csv_report.py     # Level 3
│   └── api.py            # Level 4
├── tests/
│   ├── test_pricing.py
│   ├── test_csv_report.py
│   └── test_api.py
├── data/sample_orders.csv
├── generate_report.py    # Level 5
├── requirements-dev.txt
└── pyproject.toml
```

## 시작하기

```powershell
# 가상환경 활성화 (Windows)
.venv\Scripts\Activate.ps1

# 테스트 및 린트 실행
pytest -q
ruff check .
ruff format --check .
```
