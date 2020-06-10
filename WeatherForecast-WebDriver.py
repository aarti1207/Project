# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:48:27 2020

@author: Aarti
"""

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:/Users/Aarti/PythonProject/chromedriver_win32/chromedriver.exe')


city =str(input("Enter the name of the city you want the weather forcast for : "))

driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")

print(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)