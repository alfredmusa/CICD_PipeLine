from setuptools import setup, find_packages


setup(
    name='CICD_PipeLine',
    version='7.1.3',
    python_requires=">=3.6",
    packages=find_packages(where="src"),
    install_requires=[
        'Cython','pytest','labels','pandas==1.3.4','numpy==1.21.4'
    ]
    
)
