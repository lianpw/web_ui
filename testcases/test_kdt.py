import random
import time

from selenium.webdriver.common.by import By
from webdriver_helper import debugger

from core.kdt import KeyWord


def test_login(driver):
    kw = KeyWord(driver)
    kw.key_get_url('http://101.34.221.219:8010/')
    kw.key_clikc('/html/body/div[2]/div/ul[1]/div/div/a[1]')
    kw.key_input('/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input', 'test101')
    kw.key_input('/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input', '123456')
    kw.key_clikc('/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button')
    kw.key_assert_text('html/body/div[10]/div/p', '登录成功')


def test_goods_collect(clear_collect_goods):
    kw = KeyWord(clear_collect_goods)
    kw.key_get_url('http://101.34.221.219:8010/?s=goods/index/id/5.html')
    collect_count = kw.key_get_text('/html/body/div[4]/div[2]/div[2]/div/div[3]/div[1]/span/em[2]')[1:-1]
    kw.key_clikc('/html/body/div[4]/div[2]/div[2]/div/div[3]/div[1]/span/em[1]')
    kw.key_assert_text('/html/body/div[10]/div/p', '收藏成功')
    new_collect_count = kw.key_get_text('/html/body/div[4]/div[2]/div[2]/div/div[3]/div[1]/span/em[2]')[1:-1]
    assert int(new_collect_count) - int(collect_count) == 1


def test_update_user_info(login_driver):
    name = '南柯一梦'+str(random.randint(1000,9999))
    kw = KeyWord(login_driver)
    kw.key_get_url('http://101.34.221.219:8010/?s=personal/index.html')
    kw.key_clikc('/html/body/div[4]/div[3]/div/legend/a')
    kw.key_input('/html/body/div[4]/div[3]/div/form/div[1]/input', name)
    kw.key_clikc('/html/body/div[4]/div[3]/div/form/div[2]/div/label[3]/span/i[2]')
    kw.key_input('/html/body/div[4]/div[3]/div/form/div[3]/input', '2022-06-15')
    kw.key_clikc('/html/body/div[4]/div[3]/div/form/div[4]/button')
    kw.key_assert_text('//p[@class="prompt-msg"]', '编辑成功')
    # 断言 页面跳转之后, 信息被修改
    kw.key_get_url('http://101.34.221.219:8010/?s=personal/index.html')
    # debugger(login_driver)
    kw.key_assert_text('/html/body/div[4]/div[3]/div/dl/dd[2]', name)


def test_update_user_avatar(login_driver):
    kw = KeyWord(login_driver)
    kw.key_get_url('http://101.34.221.219:8010/?s=personal/index.html')
    kw.key_clikc('/html/body/div[4]/div[3]/div/dl/dd[1]/span/a')
    # login_driver.find_element(By.XPATH, '//*[@id="user-avatar-popup"]/div/div[2]/form/div[2]/div/input')
    kw.key_execute_sql('//*[@id="user-avatar-popup"]/div/div[2]/form/div[2]/div/input', 'arguments[0].style="position:static;"')
    # debugger(login_driver)
    time.sleep(1)
    kw.key_input('//*[@id="user-avatar-popup"]/div/div[2]/form/div[2]/div/input', 'D:\\img\\photo.jpg')
    kw.key_clikc('//*[@id="user-avatar-popup"]/div/div[2]/form/button')
    kw.key_assert_text('//p[@class="prompt-msg"]', '上传成功')