#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Alejandro Marrero",
    author_email='amarrerd@ull.edu.es',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="FastAPI example with ML ",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ml_fastapi_example',
    name='ml_fastapi_example',
    packages=find_packages(include=['ml_fastapi_example', 'ml_fastapi_example.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/amarrerod/ml_fastapi_example',
    version='0.1.0',
    zip_safe=False,
)
