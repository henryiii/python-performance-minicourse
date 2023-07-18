#!/usr/bin/env python3

import importlib.util
import sys

assert sys.version_info >= (3, 8), "Python should be 3.8+"


for lib in ["pandas", "numba", "line_profiler"]:
    if importlib.util.find_spec(lib) is None:
        print("Environment not setup property! Use conda, see readme.")
        print("Maybe `conda activate performance-minicourse` is missing?")
        print("At least", lib, "is missing")
        sys.exit(1)

print("Environment appears correct, congratulations!")
