# -*- coding:UTF-8 -*-
#!/usr/bin/env python

"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium        
        app = os.path.abspath('./YHB_Prj.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '11.0',
                'deviceName': 'iPhone 7'
            })

    def tearDown(self):
        self.driver.quit()

    # def test_print(self):
    #     print "ggg"

    def test_gohome(self):
        print "texxxxx"        
        #els = self.driver.findElementByIosNsPredicate("value =='Allow'")
        allowbtn = self.driver.find_element_by_ios_predicate("label =='Allow'")
        allowbtn.click()

        #sleep(1)

        #self.driver.implicitly_wait(1)

        for i in range(2):
            self.driver.swipe(start_x=333, start_y=497, end_x=-300, end_y=497, duration=1)

            #self.driver.implicitly_wait(150)

        #sleep(10)


        #TouchAction(self.driver).tap([(188, 340)]).perform()

        # 选择launchImage3  ，通过Appnium 选择工具选择
        launchImage3 = self.driver.find_element_by_accessibility_id("launchImage3")
        launchImage3.click()

        sleep(7)

        #tabmy = self.driver.find_element_by_ios_class_chain("//XCUIElementTypeApplication[@name=\"麦子金服财富\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeButton[4]")
        #tabmy.click()

        close_btn = self.driver.find_elements_by_class_name("XCUIElementTypeButton")[0]
        close_btn.click()



        tabbar = self.driver.find_elements_by_class_name('XCUIElementTypeTabBar')[0]        

        mybutton = tabbar.find_elements_by_class_name("XCUIElementTypeButton")[3]

        mybutton.click()

        #loginUser = tabbar.find_elements_by_class_name("XCUIElementTypeTextField")[0]

        #userNameField = self.driver.find_element_by_ios_predicate("label =='请输入手机号/用户名'")


        print len(self.driver.find_elements_by_class_name("XCUIElementTypeTextField"))

        phoneNum_field = self.driver.find_elements_by_class_name("XCUIElementTypeTextField")[0]
        phoneNum_field.send_keys("13262591951")

        #sleep(10)

        password_field = self.driver.find_elements_by_class_name("XCUIElementTypeSecureTextField")[0]
        password_field.send_keys("it789123")

        login_button = self.driver.find_elements_by_class_name("XCUIElementTypeButton")[2]
        login_button.click()

        #skipbtn = self.driver.find_elements_by_class_name('//XCUIElementTypeButton[@name="跳过"]')

        sleep(2)

        #skipbtn = self.driver.find_element_by_accessibility_id("跳过")
        skipbtn = self.driver.find_element_by_ios_predicate("label =='跳过'")
        skipbtn.click()

        self.assertTrue(skipbtn)

        # if(skipbtn)
        # {
        #     print "have skipbt"
        # }

        #self.assertIsNotNone(skipbtn)
        # if(skipbtn)
        # {
        #     self.assertTrue(scroll_after)
        # }

        sleep(2)




        #TouchAction(self.driver).tap([(188, 340)]).perform()

        #self.driver.flick(300, 300,50 , 500)

        #self.driver.swipe(300, 300, 0, 300, 100)

        #sleep(2)

        #self.driver.swipe(300, 300, 0, 300, 800)

        #self.driver.implicitly_wait(15)

        #TouchAction(self.driver).press(x=300, y=402).move_to(x=20, y=402).release().perform()

        #sleep(10)

        #TouchAction(self.driver).press(x=300, y=402).move_to(x=50, y=402).release().perform()
        #sleep(10)

        #TouchAction(self.driver).press(x=300, y=402).move_to(x=50, y=402).release().perform()

        #sleep(10)

        #ele = self.driver.find_elements_by_class_name('XCUIElementTypeAlert[0]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]')
        #ele.click()



        #launchImage1 = self.driver.find_element_by_accessibility_id("launchImage1")
        #launchImage1.click()

        
        #image1.swipe()        
        #metabbar.click()
        # els = self.driver.findElementByIosNsPredicate("value =='Allow'")

        # els.click()

        # els = self.driver.find_elements_by_class_name('XCUIElementTypeButton')
        # els[5].click()

        # sleep(1)
        # try:
        #     el = self.driver.find_element_by_accessibility_id('Allow')
        #     el.click()
        #     sleep(1)
        # except:
        #     pass        
        #el.click()



        # location = el.location
        # self.driver.swipe(start_x=location['x'], start_y=location['y'], end_x=0.5, end_y=location['y'], duration=800)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)