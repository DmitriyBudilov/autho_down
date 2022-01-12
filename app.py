import requests as req
from requests.exceptions import ConnectionError
import os
import datetime as dt
import calendar

basedir = os.path.abspath(os.path.dirname(__file__))

def get_file_from_server(path, url, filename):
    if not os.path.exists(path):
        try:
            request = req.get(url + filename)
            with open(path, "wb") as file:
                    file.write(request.content)
        except ConnectionError as err:
            print(err)
        finally:
            print('Logger')

def get_year_and_month():
    now = dt.datetime.utcnow() - dt.timedelta(weeks=4)
    return now.year, now.month

year, month = get_year_and_month()
days_in_month = calendar.monthrange(year, month)
path_to_downloads = os.path.join(basedir, 'downloads', f'{year}', f'{month}')

if not os.path.exists(path_to_downloads):
    os.makedirs(path_to_downloads)

for day in range(1, days_in_month[1] + 1):
    date = dt.datetime(year=year, month=month, day=day)
    filename = f'sci_xrsf-l2-avg1m_g16_d{date:%Y%m%d}_v2-1-0.nc'
    path_for_file = os.path.join(path_to_downloads, filename)
    url_path = f'https://data.ngdc.noaa.gov/platforms/solar-space-observing-satellites/goes/goes16/l2/data/xrsf-l2-avg1m_science/{date:%Y}/{date:%m}/'
    get_file_from_server(path=path_for_file, url=url_path, filename=filename)
