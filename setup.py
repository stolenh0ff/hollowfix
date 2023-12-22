# setup.py
from cx_Freeze import setup, Executable

setup(
    name="hollowfix",
    version="0.1",
    description="Fix for 21:9 Screens",
    executables=[Executable("hollowfix.py")]
)
