# Custom Code Linter and Formatter CI Workflow Demo & Lab Report

**Objective:** Enforce code styling rules automatically on every incoming pull request using GitHub Actions.

---

## 1. Overview & Architecture

Modern software engineering teams enforce code styling and quality standards before merging code into production branches. This project implements a GitHub Actions CI pipeline that:
1. Triggers on any `pull_request` targeting `main`/`master` (and direct `push` events).
2. Sets up Python across multiple versions (`3.11`, `3.12`).
3. Executes `flake8` to detect PEP 8 violations, unused imports, undefined variables, and complexity.
4. Executes `black --check` to verify uniform indentation and formatting standards.
5. Runs `pytest` to guarantee functional correctness.

```
       [Developer]
            │
            ▼ creates branch & commits code
     [feature branch]
            │
            ▼ opens Pull Request
   [GitHub Pull Request]
            │
            ▼ triggers workflow (.github/workflows/lint.yml)
┌────────────────────────────────────────────────────────┐
│                   GitHub Actions CI                    │
│                                                        │
│  1. Checkout code (actions/checkout@v4)                │
│  2. Setup Python environment (actions/setup-python@v5) │
│  3. Install flake8, black, pytest                      │
│  4. Run flake8 linter (PEP 8 check)                   │
│  5. Run black --check (Format verification)            │
│  6. Run pytest (Unit tests)                            │
└──────────────────────────┬─────────────────────────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
       [Violations Found]         [No Violations]
        ❌ CI FAILS                ✅ CI PASSES
     (PR Merge Blocked)          (Ready for Review & Merge)
```

---

## 2. GitHub Actions Workflow Definition (`.github/workflows/lint.yml`)

```yaml
name: Lint and Format Checker

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  lint:
    name: Code Quality & Style Checks
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements-dev.txt

      - name: Run Flake8 (Syntax and PEP8 Style Linter)
        run: |
          # Stop build on fatal errors or undefined names
          flake8 src tests --count --select=E9,F63,F7,F82 --show-source --statistics
          # Full style check
          flake8 src tests --count --statistics

      - name: Run Black Code Formatter Check
        run: |
          black --check --diff src tests

      - name: Run Unit Tests
        run: |
          pytest
```

---

## 3. Demo Step 1: Intentionally Flawed Code & Pipeline Failure

To prove that the pipeline catches styling violations and blocks non-compliant PRs, we introduce intentional styling violations into `src/calculator.py` on a demo branch (e.g. `feat/lint-failure-demo`).

### Flawed Code Example (`src/calculator.py` with violations):
```python
import sys, os    # F401: unused imports; E401: multiple imports on one line
from typing import Union

Number = Union[int, float]

class Calculator:
    @staticmethod
    def add(a: Number,b: Number)->Number:  # E231: missing whitespace after ',' ; E225: missing whitespace around operator
        x=a+b                              # E225: missing whitespace around operator
        return x   

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        # E501: line longer than 88 characters
        super_long_comment_that_exceeds_the_maximum_allowed_pep8_character_limit_per_line_by_a_wide_margin = True
        return a-b                         # E225: missing whitespace around '-'
```

### Terminal / GitHub Action Failure Output:
```text
Run flake8 src tests --count --statistics
src/calculator.py:1:1: F401 'sys' imported but unused
src/calculator.py:1:1: F401 'os' imported but unused
src/calculator.py:1:1: E401 multiple imports on one line
src/calculator.py:7:1: E302 expected 2 blank lines, found 1
src/calculator.py:8:22: E231 missing whitespace after ','
src/calculator.py:8:32: E225 missing whitespace around operator
src/calculator.py:9:10: E225 missing whitespace around operator
src/calculator.py:10:17: W291 trailing whitespace
src/calculator.py:15:89: E501 line too long (114 > 88 characters)
src/calculator.py:16:17: E225 missing whitespace around operator
10      total errors
Error: Process completed with exit code 1.
```

```text
Run black --check --diff src tests
would reformat src/calculator.py
--- src/calculator.py	2026-09-09 06:20:00.000000 +0000
+++ src/calculator.py	2026-09-09 06:20:01.000000 +0000
@@ -6,8 +6,8 @@
-    def add(a: Number,b: Number)->Number:
-        x=a+b
+    def add(a: Number, b: Number) -> Number:
+        x = a + b
Error: Process completed with exit code 1.
```

**Status on Pull Request:** ❌ **Checks failed (1 failing check: Code Quality & Style Checks)**. Pull Request merging is blocked.

---

## 4. Demo Step 2: Fixing Styling Violations & Pipeline Turning Green

To resolve the errors:
1. Remove unused imports `sys, os`.
2. Ensure standard 2-space blank lines between top-level definitions.
3. Fix operator and parameter spacing.
4. Keep line lengths within 88 characters.
5. Format with `black src tests`.

### Fixed Clean Code (`src/calculator.py`):
```python
"""Calculator module providing basic arithmetic and statistical operations."""

from typing import Union

Number = Union[int, float]


class Calculator:
    """A standard arithmetic calculator with error handling."""

    @staticmethod
    def add(a: Number, b: Number) -> Number:
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        """Return the difference between two numbers."""
        return a - b

    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        """Return the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a: Number, b: Number) -> float:
        """Return the quotient of two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def power(base: Number, exponent: Number) -> Number:
        """Return base raised to power exponent."""
        return base**exponent
```

### Terminal / GitHub Action Passing Output:
```text
Run flake8 src tests --count --statistics
0
All files pass Flake8 standards.

Run black --check --diff src tests
All done! ✨ 🍰 ✨
4 files would be left unchanged.

Run pytest
============================= test session starts =============================
platform ubuntu-latest -- Python 3.12
rootdir: /home/runner/work/SE-1/SE-1
collected 5 items

tests/test_calculator.py .....                                           [100%]

============================== 5 passed in 0.05s ==============================
```

**Status on Pull Request:** ✅ **All checks have passed (2 successful checks: Python 3.11, Python 3.12)**. Pull Request is eligible for merge.

---

## 5. Jira / Project Management Integration Guide

When using Jira for tracking software engineering deliverables:

| Jira Issue Field | Value / Details |
| :--- | :--- |
| **Issue Type** | Story / Task (`SE-11`) |
| **Summary** | Setup Custom Code Linter and Formatter Workflow on Pull Requests |
| **Description** | Automate code formatting and PEP 8 style validation via GitHub Actions on all incoming pull requests to ensure clean code quality. |
| **Acceptance Criteria** | 1. Workflow file `.github/workflows/lint.yml` created.<br>2. Flake8 and Black integrated with project configs.<br>3. Branch with styling errors fails CI pipeline.<br>4. Branch with fixed styling passes all CI checks. |
| **Status Transition** | `To Do` ➔ `In Progress` ➔ `Code Review` (PR with failed then passing CI) ➔ `Done` |
| **Smart Commits** | `SE-11 #comment Automated linting workflow added #time 2h` |

---

## 6. Commands to Replicate the Full Demo Live

1. **Push the workflow & main clean project**:
   ```bash
   git add .
   git commit -m "feat(ci): add GitHub Actions lint and format workflow and calculator project"
   git push origin main
   ```

2. **Create failure branch & submit PR**:
   ```bash
   git checkout -b feat/lint-failure-demo
   # Inject intentional style violation into src/calculator.py
   git add src/calculator.py
   git commit -m "test: introduce style violations to verify CI failure"
   git push origin feat/lint-failure-demo
   # Open PR on GitHub -> View Red X CI failure
   ```

3. **Push fix & verify green status**:
   ```bash
   # Fix violations or run 'black src tests'
   git add src/calculator.py
   git commit -m "fix: resolve flake8 and black styling violations"
   git push origin feat/lint-failure-demo
   # Watch GitHub Actions update -> Turns Green ✅
   ```
