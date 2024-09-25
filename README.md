# Reflex-Map

A Custom Component for [Reflex](https://reflex.dev/) that wraps [React-Map-GL](https://visgl.github.io/react-map-gl/)

## Installation

```bash
pip install reflex-map
```

## Development

Install a [Poetry](https://python-poetry.org/) project from the root directory:

```bash
poetry install
```

To publish an update to the package, run the following command:

```bash
poetry run reflex component publish -r <PACKAGEINDEX> -t <PYPIKEY>
```
Where `<PACKAGEINDEX>` is the package index (either pypi or testpypi), and `<PYPIKEY>` is the account's API key.

## Running the Demo

Run the demo app from the `map_demo` directory:

```bash 
poetry run reflex run
```
