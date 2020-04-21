#!/usr/bin/env python3

import sys

try:
    assert sys.version_info >= (3, 7), "Python should be 3.7+"

    import pandas
    import numba
    import line_profiler
except (AssertionError, ImportError) as e:
    print("Environment not setup property! Use conda, see readme.")
    print("Maybe `conda activate performance-minicourse` is missing?")
    print(e)
    sys.exit(1)

print("Environment appears correct, congratulations!")
