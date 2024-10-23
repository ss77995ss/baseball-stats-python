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
