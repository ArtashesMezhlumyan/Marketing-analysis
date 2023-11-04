from setuptools import setup, find_packages

setup(
    author='Karen Hovhannisyan',
    description='DS-223 ETL staff',
    name='etl',
    version='0.1.0',
    packages=find_packages(include=['etl','etl.*']),
    
)