import codecs
from setuptools import setup


def readme():
    with codecs.open('README.md') as f:
        return f.read()

setup(
    name='geohash',
    version='0.0.1',
    description='?',
    long_description=readme(),
    url='http://github.com/tgadf/geohash',
    keywords='geohash',
    author='Thomas Gadfort',
    author_email='tgadfort@gmail.com',
    classifiers=[ 
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    license='MIT',
    install_requires=[],
    packages=[],
    scripts=[],
    zip_safe=False,
    include_package_data=True,
    project_urls={  
        'Bug Reports': 'https://github.com/tgadf/geohash/issues',
        'Source': 'https://github.com/tgadf/geohash'
    },
)
 