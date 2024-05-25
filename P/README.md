### Welcome to pytest

The [official](https://docs.pytest.org/en/8.2.x/) site is available.

In order to run the examples you may use the following codes. 

``` bash
python3 -m unittest
python3 -m unittest -v
python3 -m pytest -q pytesting/test_compare.py -vvv
python3 -m pytest --html=report.html --self-contained-html
python3 -m pytest -q pytesting/test_class_based.py::TestClass::test_one -vvv
```

For the **pytest** examples you have to install the following.

``` bash
pip install pytest pytest-html
```

