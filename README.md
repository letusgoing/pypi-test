# pypiTest
pypiTest

# 发布至公共仓库教程
[https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives)

# setup
python setup.py sdist

# upload to test.pypi.org
python3 -m twine upload --repository testpypi dist/*
