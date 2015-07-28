from selenium import webdriver
import os, time
from seleniumscreen import get_screenshot
from md5_hash_image import get_md5_hash
import unittest

"""Carousel - is an example of "carousel" testing to ensure that images which are changing
within certain time interval are unique.
The test is based on usage md5 hash for images and selenium webdriver to get screenshots.

"""

class TestCarousel(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        url = 'http://getbootstrap.com/examples/carousel/'
        self.driver.get(url)
        
    def test_carousel(self):
        driver = self.driver
        fnames = ['img1.png', 'img2.png', 'img3.png','img4.png']
        base_dir = os.path.dirname(__file__)
        md5_list = []
        TIME = 4 # carousel image is changing in TIME seconds

        for file in range(len(fnames)):
            get_screenshot(driver=driver,
                           css='div.carousel-inner div.item.active img',
                           filename=fnames[file])
            time.sleep(TIME) 

        for file in range(len(fnames)):
            path_to_file = os.path.join(base_dir, fnames[file]) 
            f = open(path_to_file, 'rb')
            md5_list.append(get_md5_hash(f))

        self.assertEqual( len(md5_list), 4,
                          "Unexpected number (%d) of images."% len(md5_list))
        self.assertEqual( len(set(md5_list)), 3,
                          "Unexpected number (%d) of unique images." % len(set(md5_list)))
        

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()    
