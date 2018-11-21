#!/usr/bin/env python
from datetime import datetime
import timedelta

dt1 = datetime.now()
dt2 = datetime.now() + timedelta.Timedelta(days=2, hours=2)
td = timedelta.Timedelta(days=2, hours=2)
print("seconds = %s" % td.total.seconds)
print("minutes = %s" % td.total.minutes)
print("hours = %s" % td.total.hours)
print("days = %s" % td.total.days)
