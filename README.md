# Volcano

Starter template for building Python packages, inspired by the [Yggdrasil](https://github.com/Platob/Yggdrasil) project.

## Features

- Modern `pyproject.toml` configuration powered by `setuptools`
- Ready-to-use CLI entry point (`volcano`)
- Simple core module with accompanying tests
- Optional development dependencies for linting and testing

## Getting Started

### Prerequisites

- Python 3.10 or later
- `pip` (comes bundled with Python)

### Installation (macOS/Linux)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

### Installation (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]
pytest
```

## License

This project is licensed under the terms of the included LICENSE file.

## Databricks Deployment

### Requirements

- [Databricks CLI](https://docs.databricks.com/dev-tools/cli/install.html) version 0.205.0 or later
- A configured Databricks profile with workspace access (for example, set via `databricks configure --profile <profile>`)

### Deploy the bundle

The repository ships with a Databricks bundle that provisions shared workspace assets, a reusable job cluster, and a nightly validation job. Deploy it with:

```bash
databricks bundle deploy --profile <profile> --target dev
```

Replace `<profile>` with the Databricks CLI profile you configured. The default `dev` target deploys the notebooks and job definitions to `/Shared/volcano`.

### Trigger the nightly validation job

After the bundle is deployed you can trigger the scheduled job on demand:

```bash
databricks bundle run nightly_validation --profile <profile> --target dev
```

You can override the notebook that the job runs by setting the `var.notebooks.run_tests` bundle variable when deploying or running the job.
