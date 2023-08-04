import os

from setuptools import setup, find_packages

import {{cookiecutter.module_name}}


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(os.path.join(this_directory, "requirements_module.txt"), "r") as f:
    requirements = [line for line in f]

setup(
    name="{{cookiecutter.module_name}}",
    version={{cookiecutter.module_name}}.__version__,
    packages=find_packages(),
    install_requires=requirements,
    package_data={'': ['README.md']},
    include_package_data=True,
    license='',
    long_description=long_description,
    long_description_content_type='text/markdown'
)