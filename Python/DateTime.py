import datetime as dt
import time as tm
tm.time() #time returns the current time in seconds since the Epoch. (January 1st, 1970)

dtnow=dt.datetime.fromtimestamp(tm.time())

delta = dt.timedelta(days = 100) # create a timedelta of 100 days . timedelta is a duration expressing the difference between two dates.
 
today = dt.date.today() #   date.today returns the current local date.
today - delta # the date 100 days ago
today > today-delta # compare dates