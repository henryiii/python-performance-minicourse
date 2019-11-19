# High Performance Python
## Princeton minicourse
### By Henry Schreiner, with Jim Pivarski

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


