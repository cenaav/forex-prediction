import pandas as pd
import datetime as dt
import matplotlib.dates as mdates

READ_DATE_FORMAT = '%Y.%m.%d %H:%M'
WRITE_DATE_FORMAT = '%Y-%m-%d %H:%M'


def read_temp(file):
    """

    :param file:
    :return:
    """
    csv = pd.read_csv(file)
    temp = csv['Date'] + ' ' + csv['Time']
    dates = [dt.datetime.strptime(d, '%Y.%m.%d %H:%M') for d in temp]
    data = {}
    data['date'] = date_to_mdate(dates)
    data['open'] = csv['Open'].fillna(0).astype(float)
    data['high'] = csv['High'].fillna(0).astype(float)
    data['low'] = csv['Low'].fillna(0).astype(float)
    data['close'] = csv['Close'].fillna(0).astype(float)
    data['volume'] = csv['Volume'].fillna(0).astype(int)
    try:
        data['predict'] = csv['Predict'].fillna(0).astype(float)
    except:
        pass
    data['str_time'] = temp
    return pd.DataFrame(data)


def read_all(file):
    """

    :param file:
    :return:
    """
    try:
        csv = pd.read_csv(file)
        data = {}
        data['date'] = csv['Date'].fillna(0).astype(str)
        data['time'] = csv['Time'].fillna(0).astype(str)
        data['open'] = csv['Open'].fillna(0).astype(float)
        data['high'] = csv['High'].fillna(0).astype(float)
        data['low'] = csv['Low'].fillna(0).astype(float)
        data['close'] = csv['Close'].fillna(0).astype(float)
        data['volume'] = csv['Volume'].fillna(0).astype(int)
        df = pd.DataFrame(data)
        return df
    except KeyError:
        csv = pd.read_csv(file, header=None)
        data = {}
        data['date'] = csv[0].fillna(0).astype(str)
        data['time'] = csv[1].fillna(0).astype(str)
        data['open'] = csv[2].fillna(0).astype(float)
        data['high'] = csv[3].fillna(0).astype(float)
        data['low'] = csv[4].fillna(0).astype(float)
        data['close'] = csv[5].fillna(0).astype(float)
        data['volume'] = csv[6].fillna(0).astype(int)
        df = pd.DataFrame(data)
        return df


def read_dtohlcv(file):
    """

    :param file:
    :return:
    """
    try:
        csv = pd.read_csv(file)
        temp = csv['Date'] + ' ' + csv['Time']
        dates = [dt.datetime.strptime(d, '%Y.%m.%d %H:%M') for d in temp]
        data = {}
        data['date'] = dates
        data['open'] = csv['Open'].fillna(0).astype(float)
        data['high'] = csv['High'].fillna(0).astype(float)
        data['low'] = csv['Low'].fillna(0).astype(float)
        data['close'] = csv['Close'].fillna(0).astype(float)
        data['volume'] = csv['Volume'].fillna(0).astype(int)
        data['str_time'] = temp
        df = pd.DataFrame(data)
        return df
    except KeyError:
        csv = pd.read_csv(file, header=None)
        temp = csv[0] + ' ' + csv[1]
        dates = [dt.datetime.strptime(d, READ_DATE_FORMAT) for d in temp]
        data = {}
        data['date'] = dates
        data['open'] = csv[2].fillna(0).astype(float)
        data['high'] = csv[3].fillna(0).astype(float)
        data['low'] = csv[4].fillna(0).astype(float)
        data['close'] = csv[5].fillna(0).astype(float)
        data['volume'] = csv[6].fillna(0).astype(int)
        data['str_time'] = temp
        df = pd.DataFrame(data)
        return df


def read_dtohlcv_2(file):
    """

    :param file:
    :return:
    """
    try:
        csv = pd.read_csv(file)
        temp = csv['Date']
        dates = [dt.datetime.strptime(d, '%Y%m%d') for d in temp]
        data = {}
        data['date'] = dates
        data['open'] = csv['Open'].fillna(0).astype(float)
        data['high'] = csv['High'].fillna(0).astype(float)
        data['low'] = csv['Low'].fillna(0).astype(float)
        data['close'] = csv['Close'].fillna(0).astype(float)
        data['volume'] = csv['Volume'].fillna(0).astype(int)
        df = pd.DataFrame(data)
        return df
    except KeyError:
        csv = pd.read_csv(file, header=None)
        temp = csv[0] + ' ' + csv[1]
        dates = [dt.datetime.strptime(d, '%Y%m%d') for d in temp]
        data = {}
        data['date'] = dates
        data['open'] = csv[2].fillna(0).astype(float)
        data['high'] = csv[3].fillna(0).astype(float)
        data['low'] = csv[4].fillna(0).astype(float)
        data['close'] = csv[5].fillna(0).astype(float)
        data['volume'] = csv[6].fillna(0).astype(int)
        df = pd.DataFrame(data)
        return df


def date_to_long(list):
    """

    :param list:
    :return:
    """
    return [int(d.timestamp()) for d in list]


def date_to_mdate(data):
    """

    :param data:
    :return:
    """
    return [mdates.date2num(d) for d in data]


def save_as_csv(file, data):
    """

    :param file:
    :param data:
    :return:
    """
    data.to_csv(file, sep=',', encoding='utf-8', index=False, float_format='%.5f')
    return True


def save_as_json(file, data):
    """

    :param file:
    :param data:
    :return:
    """
    with open(file, 'w') as f:
        f.write(data.to_json(orient='records')) #data.to_json(orient='records', lines=True)


def read_finance_data(file, long_date=False):
    """

    :param file:
    :param long_date:
    :return:
    """
    data = read_dtohlcv(file)
    if long_date:
        data["date"] = date_to_long(data.date)
    else:
        data["date"] = date_to_mdate(data.date)
    return data


def read_ohlc(file):
    """

    :param file:
    :return:
    """
    data = read_all(file)
    data.drop(["volume", "date", "time"], axis=1, inplace=True)
    return pd.DataFrame(data)