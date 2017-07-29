""" A quick test to make sure we can get pyephem to do what we want """
import ephem
from dateutil import tz

def doit():
    ''' runs the thingy '''
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Australia/Adelaide')

    bute = ephem.Observer()
    bute_sa_lat = '-33.8393058'
    bute_sa_long = '137.9405358'
    bute.lat, bute.lon = bute_sa_lat, bute_sa_long
    next_sunrise = bute.next_rising(ephem.Sun()).datetime()
    next_sunrise = next_sunrise.replace(tzinfo=from_zone)
    next_sunset = bute.next_setting(ephem.Sun()).datetime()
    next_sunset = next_sunset.replace(tzinfo=from_zone)

    print 'next sunrise = ' + str(next_sunrise.astimezone(to_zone))
    print 'next sunset = ' + str(next_sunset.astimezone(to_zone))

doit()
