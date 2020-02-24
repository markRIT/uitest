#coding=utf-8

import unittest
from public.until import HTMLTestRunner
import time
import schedule
from config import globalparam
from public.common import sendmail

def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = globalparam.report_path + '/' + 'TestResult' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    mail = sendmail.SendMail()
    mail.send()

if __name__=='__main__':
    print("--------------")
    print( time.strftime('%Y-%m-%d_%H_%M_%S'))
    schedule.every().day.at("17:22").do(run)  # 每天十点半执行
    while True:
        schedule.run_pending()  # 运行所有可运行的任务
        time.sleep(1)
    # run()   #只运行一次

