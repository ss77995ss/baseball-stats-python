# Contributing to baseball-stats-python

Thanks for noticing this project! The following is a set of guidelines for contributing to **baseball-stats-python**. These are mostly guidelines, not rules. Feel free to propose changes to this document in a pull request.

## How Can I Contribute?

### 1. Reporting Bugs

If you find a bug, feel free to open a [new issue](https://github.com/ss77995ss/baseball-stats-python/issues) to report it. Please use the template or the following format:

- **Description**: A clear and concise description of what the bug is.
- **Steps to Reproduce**: Provide a step-by-step guide on how to reproduce the issue.
- **Expected Behavior**: What you expected to happen.
- **Actual Behavior**: What actually happened.
- **Environment**: Include relevant environment details (e.g., Python version, OS).

### 2. Feature Requests

If you have an idea for a new feature or enhancement, feel free to [open a new issue](https://github.com/ss77995ss/baseball-stats-python/issues) with the `enhancement` label. Provide a clear description of the feature and why it would be useful.

### 3. Contributing Code

#### Fork the Repository

1. [Fork this repository](https://github.com/ss77995ss/baseball-stats-python/fork).
2. Clone your fork:

```bash
git clone https://github.com/<your-username>/baseball-stats-python.git
```

3. Add the upstream repository as a remote:

```bash
git remote add upstream https://github.com/ss77995ss/baseball-stats-python.git
```

4. Sync your fork with the upstream repository:

```bash
git fetch upstream main
git pull upstream main
```

5. Create a new branch for your feature/fix:

```bash
git checkout -b my-new-feature
```

6. Start virtual environment(Recommend using [venv](https://docs.python.org/3/library/venv.html))

```bash
pip install venv
python -m venv .venv
source venv/bin/activate
```

7. Install requirements packages

```bash
pip install -r requirements.txt
```

#### Write Your Code

- Write docstrings for any new classes, functions, or modules.
- Write tests to ensure the feature or bug fix is working properly.
- Document your code if necessary.

#### Running Tests

Before submitting your changes, ensure that all tests pass. You can run the tests using the following command:

```bash
pytest
```

#### Running Linter Checks

```bash
ruff check
```

#### Commit and Push

1. Commit your changes:
   ```bash
   git commit -m "Add a brief message describing your changes"
   ```
2. Push to your branch:

```bash
  git push origin my-new-feature
```

#### Submit a Pull Request

- Go to the original repository on GitHub and submit a pull request from your branch.
- Provide a clear description of the changes and the motivation behind them.

## Community and Feedback

If you have any questions, feel free to email me or reach out through an issue. We're happy to help!

Thank you for contributing to **baseball-stats-python**! Let's make this project better together.

## Adding a New Data Source

Each data source (Baseball Savant, FanGraphs, a new league) lives in its own subpackage under `src/baseball_stats_python/`, e.g. `cpbl/`. Following these conventions keeps every source behaving the same way for users:

- **Requests** go through `utils.fetch` (`fetch_json` for JSON, `fetch_csv` for large CSV searches). It applies timeouts and retries and turns failures into `RequestError` / `RequestTimeoutError`. Do not call `requests` directly.
- **Logging** uses `logger = logging.getLogger(__name__)`. Never `print()` and never call `logging.basicConfig()`. Support `debug=True` by calling `utils.log.enable_debug_logging()`.
- **Seasons** accept `int` or `str` (and a list where the source supports several), validated with `utils.seasons.build_season_param` against the seasons the source actually has. Default to `constants.DEFAULT_SEASON` unless the competition is not held every year.
- **Arguments** that take a fixed set of values get an `Enum` in `enums/` and accept either the enum or its string value. Invalid arguments raise `ValueError` before any request is sent.
- **Results** are `pandas.DataFrame`s. Document the columns in `docs/<function>.md`.
- **Exports**: add the public functions to `__init__.py` and `__all__`.
- **Tests** run offline. Use the `fake_get` fixture from `tests/conftest.py` with a small saved sample of a real response, so CI never depends on the source being up.
- **Terms of use**: check that the source allows automated access before adding it, and keep request volume modest.
