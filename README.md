# pypiTest
pypiTest

# setup
python setup.py sdist

# upload to test.pypi.org
python3 -m twine upload --repository testpypi dist/*
