from setuptools import setup, find_packages
import py2exe

setup(
    name="hangman",
    version="1.0",
    windows=["hangman.py"],  # Usa 'windows' en lugar de 'console' para aplicaciones GUI
    packages=find_packages(include=["pygame", "random"]),
)
