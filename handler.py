import ephem
from dateutil import tz
import json

FROM_ZONE = tz.gettz('UTC')
TO_ZONE = tz.gettz('Australia/Adelaide')
BUTE_SA_LAT = '-33.8393058'
BUTE_SA_LONG = '137.9405358'

def sunrise(event, context):
    bute = get_observer()
    next_sunrise = bute.next_rising(ephem.Sun()).datetime()
    next_sunrise = next_sunrise.replace(tzinfo=FROM_ZONE)
    body = {
        "sunrise": str(next_sunrise.astimezone(TO_ZONE))
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

def sunset(event, context):
    bute = get_observer()
    next_sunset = bute.next_setting(ephem.Sun()).datetime()
    next_sunset = next_sunset.replace(tzinfo=FROM_ZONE)
    body = {
        "sunset": str(next_sunset.astimezone(TO_ZONE))
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

def get_observer():
    bute = ephem.Observer()
    bute.lat, bute.lon = BUTE_SA_LAT, BUTE_SA_LONG
    return bute
