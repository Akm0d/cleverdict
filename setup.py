import pathlib
from setuptools import setup
# from distutils.core import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
  name = 'cleverdict',
  packages = ['cleverdict'],
  version = '1.01',
  license='MIT',
  description = 'A data structure which allows both object attributes and dictionary keys and values to be used simultaneously and interchangeably.',
  long_description=README,
  long_description_content_type="text/markdown",
  author = 'Peter Fison',
  author_email = 'peter@southwestlondon.tv',
  url = 'https://github.com/pfython/cleverdict',
    download_url = 'https://github.com/pfython/cleverdict/archive/v_1.01.tar.gz',
  keywords = ['data', 'attribute', 'key', 'value', 'attributes', 'keys', 'values', 'database', 'utility', 'tool', "clever", "dictionary", "att", "__getattr__", "__setattr__", "getattr", "setattr"],
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Object Brokering',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
  ],
)

# Run the following from the command prompt:
# python setup.py sdist
# python -m twine upload --repository testpypi dist/*
# python -m twine upload --repository pypi dist/*
