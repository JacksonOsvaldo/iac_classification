#!/usr/bin/env python3
# -*- ecoding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "csv", "tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win64":
    base = "Win64"

setup(name="SPI Classification",
      version="0.1",
      description="Classificação de valores SPI.",
      options={"build_exe": build_exe_options},
      executables=[Executable("main.py", base=base)])
