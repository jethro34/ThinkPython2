

import datetime

print(datetime.datetime.now().strftime('%A'))

# naive_date = datetime.date(2022, 3, 12)
# print(naive_date)

# aware_date = datetime.date.today()
# print(aware_date)

# print(aware_date.weekday())
# print(aware_date.isoweekday())

# tdelta = datetime.timedelta(days=21)
# print(aware_date + tdelta)              # what the date will be 21 days from now

# print(aware_date - tdelta)            # what the date was 21 days ago
# tdelta = datetime.timedelta(days=-21)   # timedelta can be negative
# print(aware_date + tdelta)              # what the date was 21 days ago

# bday = datetime.date(2022, 9, 23)
# till_bday = bday - aware_date               # till_day is a Timedelta object
# print(till_bday)
# print(till_bday.days)                   # printing only the days
# print(till_bday.total_seconds())        # getting only total seconds

# t = datetime.time(21, 17, 12, 10000)           # no time zone information; it's still naive
# print(t)
# print(t.hour)

# dt = datetime.datetime(2022, 3, 12, 21, 20, 12, 10000)
# print(dt)
# print(dt.date())
# print(dt.time())

# tdelta = datetime.timedelta(hours=12)
# print(dt + tdelta)

# dt_today = datetime.datetime.today()    # returns current local datetime with a tz of None, not AWARE
# dt_now = datetime.datetime.now()        # returns machine time, gives the option of passing in a tz, not AWARE
# dt_utcnow1 = datetime.datetime.utcnow()  # gives utc info, but still tz is None, not AWARE
# dt_utcnow = datetime.datetime.now(tz=datetime.timezone.utc)  #  AWARE current UTC datetime, BETTER

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# getting the local tz name
# now = datetime.datetime.now()
# print(now)
# local_now = now.astimezone()        # defaults to the local tz
# print(local_now)
# local_tz = local_now.tzinfo
# print(local_tz)
# local_tzname = local_tz.tzname(local_now)
# print(local_tzname)
#
# print(now.strftime('%B %d, %Y'))        # using strfttime; from datetime object to string
# dt_str = "March 14, 2022"
# print(datetime.datetime.strptime(dt_str, '%B %d, %Y')) # strptime; from string to datetime


