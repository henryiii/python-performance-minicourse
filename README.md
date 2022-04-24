# High Performance Python
## Princeton mini-course
### By Henry Schreiner, with Jim Pivarski

## Installation

#### Binder

In the minicourse, if you haven't prepared beforehand, please use this link to run online via Binder: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/henryiii/python-performance-minicourse/master?urlpath=lab)

#### Local install:

If you are reading this at least 10 minutes before the course starts or you have anaconda
or miniconda installed, you will probably be best off installing miniconda.
This way you will keep local edits and will have an environment to play with.

Get the repository:

```bash
git clone https://github.com/henryiii/python-performance-minicourse.git
cd python-performance-minicourse
```

Download and install
[miniconda](https://docs.conda.io/en/latest/miniconda.html). On macOS with
homebrew, just run `brew cask install miniconda` [(see my
recommendations)](https://iscinumpy.gitlab.io/post/setup-a-new-mac/).

Run:

```bash
conda env create
```

from this directory. This will create an environment `performance-minicourse`. To use:

```bash
conda activate performance-minicourse
./check.py # Check to see if you've installed this correctly
jupyter lab
```

And, to disable:

```bash
conda deactivate
```

or restart your terminal.


> If you want to add a package, modify `environment.yml` then run:
>
> ```bash
> conda env update
> ```


## Lessons

* [00 Intro](./00_intro.ipynb): The introduction
* [01 Fractal accelerate](./01_fractal_accelerate.ipynb): A look at a fractal computation, and ways to accelerate it with NumPy changes, numexpr, and numba.
    - [01b Fractal interactive](./01b_fractal_interactive.ipynb): An interactive example using Numba.
* [02 Temperatures](./02_temperatures.ipynb): A look at reading files and array manipulation in NumPy and Pandas.
* [03 MCMC](./03_mcmc.ipynb): A Marco Chain Monte Carlo generator (and metropolis generator) in Python and Numba, with a focus on profiling.
* [04 Runge-Kutta](./04_runge_kutta.ipynb): Implementing a popular integration algorithm in NumPy and Numba.
* [05 Distributed](./05_distributed.ipynb): An exploration of ways to break up code (fractal) into chunks for multithreading, multiproccessing, and Dask distribution.
* [06 Tensorflow](./06_tensorflow.ipynb): A look at implementing a Negative Log Likelihood function (used for unbinned fitting) in NumPy and Google's Tensorflow.
* [07 Callables](./07_callables.ipynb): A look at Scipy's LowLevelCallable, and how to implement one with Numba.


Class participants: please complete the survey that will be posted.
