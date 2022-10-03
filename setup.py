from setuptools import setup, find_packages
import pathlib
import Cython

setup(
    name='CICD_PipeLine',
    version='7.1.3',
    python_requires=">=3.7",
    install_requires=[
        "Cython","pytest","labels","pandas","numpy==1.21.5"
    ],
    packages=find_packages(where="src")
)
