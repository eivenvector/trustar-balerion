from setuptools import setup, find_packages

setup(name='trustar-owl',
      version='0.0.1',
      author='TruSTAR Technology Inc.',
      url='https://github.com/trustar/trustar-owl',
      description='Python SDK for TruSTAR Owl Tools',
      author_email='nkseib@trustar.co',
      license='Apache',
      packages=find_packages(),
      use_2to3=True, requires=['py2neo', 'flask']
      )
