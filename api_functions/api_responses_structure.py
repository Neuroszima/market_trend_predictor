# all data types here only cover the "json to python" conversion
# these do not contain data types used in actual database
from datetime import datetime


stocks = {
    'symbol': str,
    'name': str,
    'currency': str,
    'exchange': str,
    'country': str,
    'type': str,
    'access': {
        'global': str,
        'plan': str
    }
}
# this contains dict in dict
exchanges = {
    'access': {
        'global': str,
        'plan': str
    },
    'code': str,
    'country': str,
    'name': str,
    'timezone': str
}
etfs = {

}
cryptocurrencies = {

}
forex_pairs = {

}
# following contain proper read rules to be used in "strptime"
time_series_1min = {
    'datetime': (datetime, "%Y-%m-%d %H:%M:%S"),
    'high': float,
    'low': float,
    'open': float,
    'close': float,
    'volume': int
}
time_series_1day = {
    'datetime': (datetime, "%Y-%m-%d"),
    'high': float,
    'low': float,
    'open': float,
    'close': float,
    'volume': int
}
api_usage = {
    'timestamp': (datetime, "%Y-%m-%d %H:%M:%S"),
    'current_usage': int,
    'plan_limit': int,
    'daily_usage': int,
    'plan_daily_limit': int,
}
earliest_timestamp_1day = {
    'datetime': (datetime, "%Y-%m-%d"),
    'unix_time': int
}
exchange_rate = {

}
