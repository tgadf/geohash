from distutils.core import setup
import setuptools

setup(
  name = 'geohash',
  py_modules = ['geohash'],
  version = '0.0.1',
  description = 'A Python Geohash Tool',
  long_description = open('README.md').read(),
  author = 'Thomas Gadfort',
  author_email = 'tgadfort@gmail.com',
  license = "MIT",
  url = 'https://github.com/tgadf/geohash',
  keywords = ['geohash', 'location'],
  classifiers = [
    'Development Status :: 3',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ],
  install_requires = [
	'argparse'
  ]
)
 
