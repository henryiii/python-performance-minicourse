# High Performance Python
## Princeton minicourse
### By Henry Schreiner, with Jim Pivarski

## Installation

To run on Binder, click this badge: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/henryiii/python-performance-minicourse/master?urlpath=lab)

To install locally:

Download and install miniconda. On macOS with homebrew, just run `brew cask install miniconda`.

Run:

```bash
conda env create -f environment.yml
```

from this directory. This will create an environment `performance-minicourse`. To use:

```bash
conda activate performance-minicourse
```

And, to disable:

```bash
conda deactivate
```

or restart your terminal.


If you want to add a package, modify `environment.yml` then run:

```bash
conda env update -f environment.yml
```


## Lessons

* [00 Intro](./00_intro.ipynb): The introduction
* [01 Fractal accelerate](./01_fractal_accelerate.ipynb): A look at a fractal computation, and ways to accelerate it with Numpy changes, numexpr, and numba.
* [02 Temperatures](./02_temperatures.ipynb): A look at reading files and array manipulation in Numpy and Pandas.
* [03 MCMC](./03_mcmc.ipynb): A Marco Chain Monte Carlo generator (and metropolis generator) in Python and Numba, with a focus on profiling.
* [04 Runge-Kutta](./04_runge_kutta.ipynb): Implementing a popular integration algorithm in Numpy and Numba.
* [05 Distributed](./05_distributed.ipynb): An exploration of ways to break up code (fractal) into chunks for multithreading, multiproccessing, and Dask distribution.
* [06 Tensorflow](./06_tensorflow.ipynb): A look at implementing a Negative Log Likelihood function (used for unbinned fitting) in Numpy and Google's Tensorflow.
* [07 Callables](./07_callables.ipynb): A look at Scipy's LowLevelCallable, and how to implement one with Numba.