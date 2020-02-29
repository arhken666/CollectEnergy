from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
                "platformName": "Android",
                "deviceName": "OnePlus 7 Pro",
                "appPackage": "com.eg.android.AlipayGphone",
                "appActivity": "com.eg.android.AlipayGphone.AlipayLogin",
                "noReset": "true",
                "fullReset": "false"
}

server = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(server, desired_caps)
time.sleep(1)#每一个time.sleep避免网速或硬件速度影响导致没有正确执行到语句
driver.find_element_by_id('com.alipay.android.phone.openplatform:id/more_app_icon').click() #点击更多
time.sleep(1)
driver.find_element_by_id('com.alipay.android.phone.wallet.homemarket:id/app_group_item_icon').click() #点击蚂蚁森林
time.sleep(1)

def Swipe(driver):
    n=0
    while n<=5:#滑置最下方找到所有好友栏
        start_x = 500
        start_y = 1800
        distance = 1000
        driver.swipe(start_x, start_y, start_x,#driver.swipe(开始的横坐标，开始的纵坐标，滑动后横坐标，滑动后纵坐标)
                     start_y - distance)
        n=n+1
    driver.find_element_by_xpath("//*[@text='查看更多好友']").click() #点击查看更多好友
    time.sleep(1)
def run(driver):
    Swipe(driver)#进入排行榜
    while True:
        start_x = 500  # 向上滑动一个框的高度
        start_y = 2100
        distance = 180
        TouchAction(driver).press(x=170, y=700).release().perform() #永远按压第一个人的坐标
        time.sleep(1)
        name = driver.find_element_by_id('com.alipay.mobile.nebula:id/h5_tv_title').text
        if len(name)==4: #判断是否点到自己
            driver.swipe(start_x, start_y, start_x,
                         start_y - distance)
            time.sleep(1)
            continue
        print('正在查看{0}的蚂蚁森林'.format(name))
        items = driver.find_elements_by_class_name("android.widget.Button")
        if len(items)>5:#android.widget.Button的数量大于5便存在能量
            for i in items:
                if '收集' in i.text:#判断可以收取的能量
                    print('收取{0}的能量'.format(name))
                    i.click()
                    time.sleep(1)
            #driver.find_elements_by_class_name('android.widget.Image')[1].click()
        time.sleep(1)
        driver.tap([(44, 126), (100, 190)], 100)#返回排行榜
        time.sleep(1.5)
        driver.swipe(start_x, start_y, start_x,
                     start_y - distance)
        time.sleep(1)

if __name__ == '__main__':
    run(driver)