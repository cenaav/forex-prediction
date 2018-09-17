from datetime import date, datetime, timedelta
from pytz import timezone
import pytz


def get_season(now):
    """

    :param now:
    :return:
    """
    Y = 2000  # dummy leap year to allow input X-02-29 (leap day)
    seasons = [('winter', (date(Y, 1, 1), date(Y, 3, 20))),
               ('spring', (date(Y, 3, 21), date(Y, 6, 20))),
               ('summer', (date(Y, 6, 21), date(Y, 9, 22))),
               ('autumn', (date(Y, 9, 23), date(Y, 12, 20))),
               ('winter', (date(Y, 12, 21), date(Y, 12, 31)))]

    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)


def get_datetime(tz=pytz.utc, fmt="%Y-%m-%d %H:%M:%S"):
    """

    :param tz:
    :param fmt:
    :return:
    """
    utc_time = datetime.utcnow()
    tz_time = pytz.utc.localize(utc_time, is_dst=None).astimezone(tz)
    return tz_time.strftime(fmt)


def str_to_date(time, fmt='%Y-%m-%d %H:%M:%S', old_tz=pytz.utc, new_tz=pytz.utc):
    """

    :param time:
    :param fmt:
    :param old_tz:
    :param new_tz:
    :return:
    """
    naive_date = datetime.strptime(time, fmt)
    local_tz = old_tz.localize(naive_date).astimezone(new_tz)
    return local_tz


def str_to_minute_pass_from_midnight(time, fmt='%Y-%m-%d %H:%M:%S', old_tz=pytz.utc, new_tz=pytz.utc):
    """

    :param time:
    :param fmt:
    :param old_tz:
    :param new_tz:
    :return:
    """
    naive_date = datetime.strptime(time, fmt)
    local_tz = old_tz.localize(naive_date).astimezone(new_tz)
    min = (local_tz.hour * 60) + local_tz.minute
    return min


def str_to_date_wtz(time, fmt='%Y-%m-%d %H:%M:%S'):
    """

    :param time:
    :param fmt:
    :return:
    """
    naive_date = datetime.strptime(time, fmt)
    return naive_date


def utc_now_to_different_timezone(time, old_tz=pytz.utc, new_tz=pytz.utc):
    """

    :return:
    """
    if time is None:
        time = datetime.utcnow()

    # returns datetime in the new timezone
    my_timestamp_in_new_timezone = old_tz.localize(time).astimezone(new_tz)
    return my_timestamp_in_new_timezone


def is_date_in(d1, d2, d3):
    """

    :param d1:
    :param d2:
    :param d3:
    :return:
    """
    try:
        d1 = pytz.UTC.localize(d1)
    except:
        pass
    try:
        d2 = pytz.UTC.localize(d2)
    except:
        pass
    try:
        d3 = pytz.UTC.localize(d3)
    except:
        pass

    if (d1 <= d2) and (d2 <= d3):
        return 1
    else:
        return 0