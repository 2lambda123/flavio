from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(name='flavio',
      author='David M. Straub, Ece Gürler',
      author_email='david.straub@tum.de',
      packages=find_packages(),
      package_data={'flavio':['data/*']},
     )
