# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fretboard',
    version='1.0.0',
    description='Python project that shows scales and chords on an ASCII fretboard for guitar or bass',
    long_description=readme,
    author='Steven Muschalik',
    author_email='steven.muschalik@gmail.com',
    url='https://github.com/fusionprogguy/Fretboard',
    license=license,
    packages=['fretboard']
)
