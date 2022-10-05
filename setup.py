from setuptools import setup, find_packages

requirements = [
    'pytest'
]


setup(
    name="CICD_PipeLine",
    version='7.1.3',
    install_requires=requirements,
    python_requires=">=3.7",
    packages=find_packages(),
    
)
