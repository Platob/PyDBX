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
- A Databricks workspace personal access token (PAT) with the permissions required to deploy jobs and workspace files
- A configured Databricks profile that points to the target workspace. Run `databricks configure --profile <profile>` and supply the workspace host (for example, `https://<region>.azuredatabricks.net`) together with the PAT when prompted.

### Deploy the bundle

The repository ships with a Databricks bundle that provisions shared workspace assets, a reusable job cluster, and a nightly validation job. Deploy it with:

```bash
databricks bundle deploy --profile <profile> --target dev
```

Replace `<profile>` with the Databricks CLI profile you configured. The default `dev` target deploys the notebooks and job definitions to `/Shared/volcano`.

> **Tip:** If the CLI returns `HTTP Status: 403 Forbidden` with `Invalid access token`, the PAT stored in the profile has expired or was revoked. Generate a new PAT in the Databricks workspace UI and re-run `databricks configure --profile <profile>` to update the saved credentials before deploying again.

### Trigger the nightly validation job

After the bundle is deployed you can trigger the scheduled job on demand:

```bash
databricks bundle run nightly_validation --profile <profile> --target dev
```

You can override the notebook that the job runs by setting the `var.notebooks.run_tests` bundle variable when deploying or running the job.
