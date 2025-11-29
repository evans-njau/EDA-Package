from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    version = '0.1',
    packages = find_packages(include = 'tests*'),
    long_description = open('README.md').read(),
    license = 'MIT',
    description = 'EDSA example python package',
    install_requires = ['Numpy'],
    url = '',
    author = 'Evans Njau',
    author_email = 'evansn873@gmail.com'
)