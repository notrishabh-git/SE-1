# Custom Code Linter and Formatter CI Workflow

This repository demonstrates an automated Continuous Integration (CI) workflow using **GitHub Actions** to enforce code styling and formatting rules on every Pull Request and branch push.

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── lint.yml          # GitHub Actions workflow for PR & Push lint checks
├── src/
│   ├── __init__.py
│   └── calculator.py         # Core Python module
├── tests/
│   ├── __init__.py
│   └── test_calculator.py    # Pytest unit tests
├── .flake8                   # Flake8 configuration (PEP 8 rules, max line length)
├── .gitignore                # Git ignore rules
├── pyproject.toml            # Black formatter & Pytest configuration
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development & CI dependencies (flake8, black, pytest)
├── LINT_WORKFLOW_DEMO.md     # Detailed demonstration and lab report
└── README.md
```

## Tools Used

- **Linter**: [`flake8`](https://flake8.pycqa.org/) - Checks for PEP 8 styling violations, syntax issues, and unused variables/imports.
- **Formatter Checker**: [`black`](https://black.readthedocs.io/) - Enforces deterministic, unambiguous code formatting.
- **Test Runner**: [`pytest`](https://docs.pytest.org/) - Verifies unit tests pass.
- **CI/CD Platform**: **GitHub Actions** (`.github/workflows/lint.yml`) - Automatically triggers on incoming `pull_request` to `main`/`master` and on `push`.

## Quick Start (Local Development)

1. **Install dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. **Run Flake8 linting**:
   ```bash
   flake8 src tests
   ```

3. **Check formatting with Black**:
   ```bash
   black --check --diff src tests
   ```

4. **Automatically format code**:
   ```bash
   black src tests
   ```

5. **Run test suite**:
   ```bash
   pytest
   ```
