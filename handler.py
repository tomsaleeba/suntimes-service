import ephem
from dateutil import tz
import json

FROM_ZONE = tz.gettz('UTC')
TO_ZONE = tz.gettz('Australia/Adelaide')
BUTE_SA_LAT = '-33.8393058'
BUTE_SA_LONG = '137.9405358'

def sunrise(event, context):
    bute = get_observer()
    ephem_next_sunrise = bute.next_rising(ephem.Sun())
    next_sunrise = ephem_next_sunrise.datetime()
    next_sunrise = next_sunrise.replace(tzinfo=FROM_ZONE)
    local_next_sunrise = next_sunrise.astimezone(TO_ZONE)
    return response200({
        "type": "sunrise",
        "date_string": str(local_next_sunrise),
        "epoch_ms": float(ephem_next_sunrise),
        "decomposed": decompose(ephem_next_sunrise)
    })

def sunset(event, context):
    bute = get_observer()
    ephem_next_sunset = bute.next_setting(ephem.Sun())
    next_sunset = ephem_next_sunset.datetime()
    next_sunset = next_sunset.replace(tzinfo=FROM_ZONE)
    local_next_sunset = next_sunset.astimezone(TO_ZONE)
    return response200({
        "type": "sunset",
        "date_string": str(local_next_sunset),
        "epoch_ms": float(ephem_next_sunset),
        "decomposed": decompose(ephem_next_sunset)
    })

def get_observer():
    bute = ephem.Observer()
    bute.lat, bute.lon = BUTE_SA_LAT, BUTE_SA_LONG
    return bute

def decompose(e):
    year, month, date, hours, minutes, seconds = e.tuple()
    return {
        "year": year,
        "month": month,
        "date": date,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

def response200(body):
    result = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return result