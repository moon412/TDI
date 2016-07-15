# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:15:48 2016

@author: yue
"""
import os
os.chdir('D:\courses\TDI')

path = 'cities_loc.xml'
import xml.etree.ElementTree as ET
import urllib2
url = 'http://api.trulia.com/webservices.php?library=TruliaStats&function=getCityStats%20&city=Saint%20Louis&state=MO&startDate=2007-02-06&endDate=2016-07-12&apikey=v82j7c3btep9njcn7zardju6'
url = 'http://api.trulia.com/webservices.php?library=LocationInfo&function=getCitiesInState&state=MO&apikey=v82j7c3btep9njcn7zardju6'
response = urllib2.urlopen(url)
tree = ET.parse(response)
root = tree.getroot()
cities = {}
for city in root2.iter('city'):
    for elem in list(city):
        if elem.tag in cities:
            cities[elem.tag].append(elem.text)
        else:
            cities[elem.tag] = [elem.text]
import pandas as pd
cities_df = pd.DataFrame(cities)
cities_df.index = cities_df['name']