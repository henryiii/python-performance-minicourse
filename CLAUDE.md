# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Teaching material for a Princeton mini-course on high performance Python. The
content is a set of numbered Jupyter notebooks in the repository root, run in
order during the course. There is no package, no importable module, and no test
suite — the notebooks *are* the deliverable.

## Commands

```bash
pixi run lab        # start JupyterLab (the main entry point)
./check.py          # verify a conda/mamba environment has the needed libraries
prek -a --quiet     # lint and format (ruff, nbstripout, codespell)
```

There is no CI and no test suite. To check that a change did not break a lesson,
execute the notebook headlessly:

```bash
pixi run python -c "
import nbformat; from nbclient import NotebookClient
NotebookClient(nbformat.read('03_mcmc.ipynb', as_version=4), timeout=300).execute()"
```

`05_distributed.ipynb` needs a scheduler first (`pixi run dask scheduler &` and
`pixi run dask worker --nthreads 8 127.0.0.1:8786 &`); everything else runs
unattended.

Environment definition lives in `pixi.toml`. `environment.yml` is a **generated**
file for Binder and conda users — do not edit it by hand. Regenerate it after
changing dependencies:

```bash
pixi workspace export conda-environment -n performance-minicourse > environment.yml
```

## Conventions

Notebook outputs are stripped by `nbstripout` in pre-commit. Never commit
executed outputs; a diff full of output cells means the hook did not run.

`.ruff.toml` carries per-notebook lint exceptions (for example `F821` for names
defined inside `%%timeit` cells and `F811` for the deliberate re-definitions the
lessons use to show successive versions of a function). When a new notebook
redefines a name on purpose or relies on cell magics, add the exception there
rather than reworking the teaching code.

Cells that fail on purpose (the JAX tracer and immutability demos in
`06b_jax.ipynb`) carry a `raises-exception` tag, which keeps the notebooks
executable end to end. Tag any new one the same way.

Conda-forge's graphviz ships without a plugin config, so dask's `.visualize()`
fails until `dot -c` runs. The `dot-config` pixi task does this and `lab`
depends on it; `postBuild` covers Binder and `postCreateCommand` covers
Codespaces. Keep all three in sync.

`img/` holds slide images used by `00_intro.ipynb`; `data/` holds the datasets
the lessons read (Newark temperatures, NASA exoplanets). `classic/` is an older
variant of a lesson, kept for reference.

## Notebook structure

Each lesson takes one problem and re-implements it several ways, measuring each
step — that progression is the point, so keep the slow versions when editing.
The acceleration tools covered across the notebooks are NumPy vectorization,
numexpr, Numba (including `@vectorize`, `@jit`, and `LowLevelCallable`), Dask,
multiprocessing/threading, and JAX.
