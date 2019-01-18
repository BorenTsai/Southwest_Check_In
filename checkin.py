import requests
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Fill in your Southwest Airlines flight information
confirmation = ""
first_name = ""
last_name = ""
flight_time = {"hour" : , "minute" : , "second" : } 

url = "https://www.southwest.com/air/check-in/index.html?clk=GSUBNAV-CHCKIN"

def run():
  checktime = datetime.datetime.today()
  if (flight["hour"] == checktime.hour
      and flight["minute"] == checktime.minute
      and flight["second"] <= checktime.second):
    checkin()
    print("Successfully checked in - Have a Safe Flight!")
    return None
  else:
    if flight["hour"] - checktime.hour > 1:
      time.sleep(3600)
      return run()
    elif flight["minute"] - checktime.minute > 1:
      time.sleep(15)
      return run()
    else:
      time.sleep(1)
      return run()

def checkin():
  driver = webdriver.Firefox()
  driver.get(url)

  number = driver.find_element_by_id("confirmationNumber")
  first = driver.find_element_by_id("passengerFirstName")
  last = driver.find_element_by_id("passengerLastName")

  number.send_keys(confirmation)
  first.send_keys(first_name)
  last.send_keys(last_name)

  driver.find_element_by_id("form-mixin--submit-button").click()
  time.sleep(5)
  driver.close()

run()
