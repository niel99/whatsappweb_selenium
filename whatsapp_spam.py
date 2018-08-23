#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 23:43:06 2018
Whatsapp Spammer
@author: niel99
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url='https://web.whatsapp.com/'
name=input("Enter name of the victim:")
Msg=input("Enter your spam message:")
driver=webdriver.Chrome()
driver.get(url)
#After this you need to login to whatsapp web by scanning and then press anything in the console
input("Press any key to continue...")
driver.find_element_by_class_name("jN-F5").send_keys(name)
sleep(2)
#driver.find_element_by_class_name("jN-F5").send_keys(Keys.RETURN)
l=driver.find_elements_by_class_name("_1wjpf")
for i in l:
    if i.text==name:
        i.click()
        break
while(True):
    driver.find_element_by_class_name("_2S1VP").send_keys(Msg)
    driver.find_element_by_class_name("_2S1VP").send_keys(Keys.RETURN)
    #Here you can set the time after which message will be spammed
    sleep(3)

