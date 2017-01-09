from setuptools import setup, find_packages

setup(name='trustar-balerion',
      version='0.0.1',
      author='TruSTAR Technology Inc.',
      url='https://github.com/trustar/trustar-balerion',
      description='Python SDK for TruSTAR Balerion Tools',
      author_email='nkseib@trustar.co',
      license='Apache',
      packages=find_packages(),
      use_2to3=True, requires=['py2neo', 'pandas']
      )