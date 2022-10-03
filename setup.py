from setuptools import setup, find_packages
import pathlib
from Cython.Build import cythonize
setup(
    name='CICD_PipeLine',
    version='7.1.3',
    python_requires="==3.8",
    install_requires=[
        'pytest','labels','pandas','numpy<1.22.0'
    ],
    packages=find_packages(where="src"),
    ext_modules=cythonize(ext_modules)
)
