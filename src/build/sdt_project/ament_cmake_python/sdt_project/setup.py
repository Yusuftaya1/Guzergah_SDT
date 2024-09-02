from setuptools import find_packages
from setuptools import setup

setup(
    name='sdt_project',
    version='0.0.0',
    packages=find_packages(
        include=('sdt_project', 'sdt_project.*')),
)
