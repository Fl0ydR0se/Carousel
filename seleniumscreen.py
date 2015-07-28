from selenium import webdriver
from PIL import Image
import time

"""This is a screenshoting function based on selenium webdriver.
It returns saved screenshot in PNG format and takes selenium webdriver instanse,
locator type (id, css) to find and then screenshot the element and filename
to name the screenshot.


Usage:
#import, ensure that selenium and supported browser are installed 
from selenium import webdriver
from seleniumscreen import get_screenshot

#create a new webdriver instanse (firefox or other) 
driver = webdriver.Firefox()

#target credentials
url = 'http://getbootstrap.com/examples/carousel/'
filename = 'img.png'
css_locator='div.carousel-inner div.item.active img'  

#open url in browser
driver.get(url)

get_screenshot(driver=driver,
               css='div.carousel-inner div.item.active img',
               filename=filename)

#close browser
driver.quit()
"""

def get_screenshot(driver, id=None, css=None, filename='screenshot.png'):
    if id:
        element = driver.find_element_by_id(id)
    elif css:
        element = driver.find_element_by_css_selector(css)
    location = element.location
    size = element.size
    driver.save_screenshot(filename)
    

    _image = Image.open(filename)

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    image = _image.crop((left, top, right, bottom))
    image.save(filename)

