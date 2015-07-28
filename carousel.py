from selenium import webdriver
import os, time
from seleniumscreen import get_screenshot
from md5_hash_image import get_md5_hash

fnames = ['img1.png', 'img2.png', 'img3.png','img4.png']
driver = webdriver.Firefox()
url = 'http://getbootstrap.com/examples/carousel/'

driver.get(url)

base_dir = os.path.dirname(__file__)

for file in range(len(fnames)):
    get_screenshot(driver=driver,
                   css='div.carousel-inner div.item.active img',
                   filename=fnames[file])
    time.sleep(5)

driver.quit()

for file in range(len(fnames)):
    path_to_file = os.path.join(base_dir, fnames[file]) 
    f = open(path_to_file, 'rb')

    print get_md5_hash(f)

