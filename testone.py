import pandas as pd
import numpy as np
import calendar
from datetime import datetime, timedelta


def testone(start_date, end_date):
    sdate = datetime.strptime(start_date, '%Y%m%d')
    edate = datetime.strptime(end_date, '%Y%m%d')
    for i in pd.date_range(sdate, edate - timedelta(days=1), freq='d'):
        day = calendar.day_name[i.weekday()]
        monthlist = calendar.monthcalendar(i.year, i.month)
        if monthlist[0][calendar.SATURDAY] == 0:
            fourth_saturday = monthlist[4][calendar.SATURDAY]
        else:
            fourth_saturday = monthlist[3][calendar.SATURDAY]
        if i.day == fourth_saturday and (i.day % 5 == 0 and day == 'Saturday'):
            continue
        elif i.day == fourth_saturday or (i.day % 5 == 0 and day == 'Saturday'):
            print(i.strftime('%Y%m%d'))


if __name__ == '__main__':
    testone('20180728', '20180927')
