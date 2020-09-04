from datetime import datetime, date
import vision

hour_mapping = {'0': 'twelve',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve'}


def tell_the_date():
    today = date.today()
    vision.speak('The current date is: {0}'.format(today))


def tell_the_time():
    now = datetime.now()
    hour, minute = now.hour, now.minute
    converted_time = _time_in_text(hour, minute)
    vision.speak('The current time is: {0}'.format(converted_time))


def _get_12_hour_period(hour):
    return 'p.m.' if 12 <= hour < 24 else 'a.m.'


def _convert_12_hour_format(hour):
    return hour - 12 if 12 < hour <= 24 else hour


def _create_hour_period(hour):
    hour_12h_format = _convert_12_hour_format(hour)
    period = _get_12_hour_period(hour)
    return hour_mapping[str(hour_12h_format)] + ' ' + '(' + period + ')'


def _time_in_text(hour, minute):
    if minute == 0:
        time = _create_hour_period(hour) + " o'clock"
    elif minute == 15:
        time = "quarter past " + _create_hour_period(hour)
    elif minute == 30:
        time = "half past " + _create_hour_period(hour)
    elif minute == 45:
        hour_12h_format = _convert_12_hour_format(hour + 1)
        period = _get_12_hour_period(hour)
        time = "quarter to " + hour_mapping[str(hour_12h_format)] + ' ' + '(' + period + ')'
    elif 0 < minute < 30:
        time = str(minute) + " minutes past " + _create_hour_period(hour)
    else:
        hour_12h_format = _convert_12_hour_format(hour + 1)
        period = _get_12_hour_period(hour)
        time = str(60 - minute) + " minutes to " + hour_mapping[str(hour_12h_format)] + ' ' + '(' + period + ')'

    return time
