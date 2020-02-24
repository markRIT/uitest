#coding=utf-8

from time import sleep
from public.common import mytest
from model import baiduIndexPage


class TestBaiduIndex(mytest.MyTest):
    """百度搜索测试"""

    def _search(self,searchKey):
        """封装百度搜索的函数"""
        baidupage = baiduIndexPage.BaiduIndexPage(self.dr)
        baidupage.into_baidu_page()
        baidupage.input_search_key(searchKey)
        baidupage.click_search_button()
        sleep(2)
        self.assertIn(searchKey, baidupage.return_title())

    def test_search(self):
        """直接搜索"""
        baidupage = baiduIndexPage.BaiduIndexPage(self.dr)
        baidupage.into_baidu_page()
        baidupage.input_search_key('小石头tester')
        baidupage.click_search_button()
        sleep(2)
        self.assertIn('小石头',baidupage.return_title())


