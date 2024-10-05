import pandas as pd
import sqlite3 

con = sqlite3.connect('db.sqlite3')

planet = pd.read_csv('data/planets.csv', encoding='cp949')
star = pd.read_csv('data/stars.csv', encoding='cp949')

planet.to_sql('exoplanet_planet', con=con, if_exists='replace')
star.to_sql('exoplanet_star', con=con, if_exists='replace')

con.close()
