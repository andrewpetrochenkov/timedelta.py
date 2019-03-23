<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/timedelta.svg?longCache=True)](https://pypi.org/project/timedelta/)
[![](https://img.shields.io/pypi/v/timedelta.svg?maxAge=3600)](https://pypi.org/project/timedelta/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/timedelta.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/timedelta.py/)

#### Installation
```bash
$ [sudo] pip install timedelta
```

#### Classes
class|`__doc__`
-|-
`timedelta.Timedelta` |datetime.timedelta replacement
`timedelta.Total` |

#### Examples
```python
>>> import timedelta

>>> td = timedelta.Timedelta(days=2, hours=2)

# init from datetime.timedelta
>>> td = timedelta.Timedelta(datetime1 - datetime2)
```

`total` seconds, minutes, hours, days
```python
>>> td = timedelta.Timedelta(days=2, hours=2)
>>> td.total.seconds
180000
>>> td.total.minutes
3000
>>> td.total.hours
50
>>> td.total.days
2
```

#### Links
+ [timedelta Objects](https://docs.python.org/3/library/datetime.html#timedelta-objects)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>