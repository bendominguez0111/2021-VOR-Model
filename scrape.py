from bs4 import BeautifulSoup as BS
import requests
import pandas as pd

positions = ['QB', 'FLEX']

BASE_URL = 'https://www.fantasypros.com/nfl/projections/{position}.php?week=draft'

for position in positions:
    URL = BASE_URL.format(position=position)
    print(URL)
    res = requests.get(URL)
    soup = BS(res.content, 'html.parser')
    table = soup.find('table', {'id': 'data'})
    df = pd.read_html(str(table))[0]
    print(df.head())
    