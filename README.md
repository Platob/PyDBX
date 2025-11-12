# Volcano

Starter template for building Python packages, inspired by the [Yggdrasil](https://github.com/Platob/Yggdrasil) project.

## Features

- Modern `pyproject.toml` configuration powered by `setuptools`
- Ready-to-use CLI entry point (`volcano`)
- Simple core module with accompanying tests
- Optional development dependencies for linting and testing

## Getting Started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

## License

This project is licensed under the terms of the included LICENSE file.
