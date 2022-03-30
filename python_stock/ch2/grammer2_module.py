
## keyword
import keyword

print(keyword.kwlist)

print(keyword.__file__)


## import
import calendar
print(calendar.month(2022,3))


from calendar import month
#  모듈없이 바로 calendar 사용하능.
print(month(2020, 1))


## datetime
import datetime
print(datetime.datetime.now())

from datetime import datetime as dt
print(dt.now())