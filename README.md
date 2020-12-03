<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/timedelta.svg?maxAge=3600)](https://pypi.org/project/timedelta/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/timedelta.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/timedelta.py/actions)

### Installation
```bash
$ [sudo] pip install timedelta
```

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
    <a href="https://readme42.com/">readme42.com</a>
</p>
