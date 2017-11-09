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
        #app = os.path.abspath('./HHH.app')
        app = os.path.abspath('./YHB_Prj.app')
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '11.0',
                'deviceName': 'iPhone 7'
            })

    def tearDown(self):
        #退出app
        self.driver.quit()

    def atest_control(self):
        print "ggg"
        #allowbtn = self.driver.find_element_by_ios_predicate("label =='Allow'")
        #allowbtn.click()
        # btn = self.driver.find_element_by_ios_predicate("label =='Button'")
        # self.assertIsNotNone(btn)
        # label = self.driver.find_element_by_ios_predicate("label =='Label'")
        # self.assertIsNotNone(label)

        #image = self.driver.find_element_by_ios_predicate("value =='tu.jpg'")
        #self.assertIsNotNone(image)

        # textfiled = self.driver.find_element_by_ios_predicate("label =='textfid'")
        # self.assertIsNotNone(textfiled)
        # textfiled.send_keys("textFilll")

        #text_view = self.driver.find_element_by_ios_predicate("label =='textarea'")
        #self.assertIsNotNone(text_view)

        # 比较落伍的方式
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="buttonlabel"]').click()


        # 键盘消失
        #self.driver.hide_keyboard()
        self.driver.hide_keyboard()
        #self.driver.hide_keyboard(strategy='swipeOutside')

        btn2 = self.driver.find_element_by_accessibility_id('buttonlabel')
        self.assertIsNotNone(btn2)
        label2 = self.driver.find_element_by_accessibility_id("accty")
        self.assertIsNotNone(label2)


        button = self.driver.find_elements_by_class_name('XCUIElementTypeButton')[0]
        self.assertIsNotNone(button)

        # UILable
        label = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')[0]
        self.assertIsNotNone(label)
        #label.send_keys("label ok")

        image = self.driver.find_elements_by_class_name('XCUIElementTypeImage')[0]    
        self.assertIsNotNone(image)

        text_view = self.driver.find_elements_by_class_name('XCUIElementTypeTextView')[0]
        text_view.send_keys("text view ok")

        text_field = self.driver.find_elements_by_class_name('XCUIElementTypeTextField')[0]
        # get default/empty text
        default_val = text_field.get_attribute("value")
        print "aaaa"
        print default_val
        print "tttt"
        text_field.send_keys("text field ok")



        switch = self.driver.find_elements_by_class_name('XCUIElementTypeSwitch')[0]
        self.assertIsNotNone(switch)
        
        slider = self.driver.find_elements_by_class_name('XCUIElementTypeSlider')[0]
        self.assertIsNotNone(slider)

        #text_view2 = self.driver.find_element_by_accessibility_id('textarea')
        #self.assertIsNotNone(text_view2)

        sleep(1)



    def goHome(self):
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

        sleep(6)


    def atest_login(self):
        self.goHome();

        #self.driver.implicitly_wait(6)

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

        sleep(1)

        skipbtn = self.driver.find_element_by_accessibility_id("跳过")
        #skipbtn = self.driver.find_element_by_ios_predicate("label =='跳过'")
        skipbtn.click()

        self.assertTrue(skipbtn)

        #self.assertIsNotNone(skipbtn)

        #切换到后台 3 s
        #self.driver.background_app(3)  

        sleep(5)


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

    def test_webview(self):
        self.goHome();
        TouchAction(self.driver).tap(x=275, y=283).perform()  
        #TouchAction(self.driver).tap(275, 283).perform()
        #TouchAction(self.driver).tap([(275, 283)]).perform()
        #TouchAction(self.driver).press(x=275, y=283).move_to(x=280, y=290).release().perform()
        sleep(100)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)