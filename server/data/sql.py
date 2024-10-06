

import sqlite3
import pandas as pd

con = sqlite3.connect('db.sqlite3')


star_sql = """INSERT INTO exoplanet_star (
            id, name, planets_number, spectral_type, effective_temp, 
            radius, mass, luminosity, azi, pol, 
            visual_magnitude, habitable_min, habitable_max, show
        ) VALUES (
            %s, "%s", %s, "%s", %s, 
            %s, %s, %s, %s, %s, 
            %s, %s, %s, %s
        )"""
planet_sql = """INSERT INTO exoplanet_planet (
            id, name, semimajor_axis, radius, mass, 
            density, eccentricity, insolation, temperature, escape_vel, 
            ESI, SType, TType, parent_id, created_by_user
        ) VALUES (
            %s, "%s", %s, %s, %s, 
            %s, %s, %s, %s, %s, 
            %s, "%s", "%s", %s, %s
        )"""


planet = pd.read_csv('data/planets.csv', encoding='cp949')
star = pd.read_csv('data/stars.csv', encoding='cp949')

#planet.to_sql('exoplanet_planet', con=con, if_exists='replace', index=False)
cursor = con.cursor()

import math
def formatting(row, *add):
    result = []
    for i in row:
        if isinstance(i, float) and math.isnan(i):
            result.append(0)
        else:
            result.append(i)
    for a in add:
        result.append(a)
    return tuple(result)


for i, row in star.iterrows():
    cursor.execute(star_sql%formatting(row))

for i, row in planet.iterrows():
    cursor.execute(planet_sql%formatting(row, False))
con.commit()

con.close()