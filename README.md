Rainbow Runners
===============

Awesome rainbow test runners!!1
See demo with Nyan Cat on [Shelr.tv](http://shelr.tv/records/52bb2fad9660800fe9000037)!

Available runners
-----------------

* NyanCatRunner

```python
from rainbowrunners.runner import NyanCatRunner

suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
NyanCatRunner().run(suite)
```
```shell
» python tests_ok.py
 20  -_-_-_-_-_-_-_-_-_-__,------,
 0   -_-_-_-_-_-_-_-_-_-__|  /\_/\
 0   -_-_-_-_-_-_-_-_-_-_~|_( ^ .^)
     -_-_-_-_-_-_-_-_-_-_ ""  ""
----------------------------------------------------------------------
Ran 20 tests in 3.04s

OK
```

Django support
--------------

```python
# settings.py
TEST_RUNNER = 'rainbowrunners.djrunner.NyanCatDiscoverRunner'
```


License
-------

Rainbow Runners is distributed under the [MIT license](http://www.opensource.org/licenses/MIT).
