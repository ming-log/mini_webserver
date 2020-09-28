# __author__:"Ming Luo"
# date:2020/9/28
# 日志一共分成5个等级，从低到高分别是：
#
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# DEBUG：详细的信息,通常只出现在诊断问题上
# INFO：确认一切按预期运行
# WARNING：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
# ERROR：更严重的问题,软件没能执行一些功能
# CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行

# 这5个等级，也分别对应5种打日志的方法：
# debug 、info 、warning 、error 、critical。
# 默认的是WARNING，当在WARNING或之上时才被跟踪。
import logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.info('这是 loggging info message')
logging.debug('这是 loggging debug message')
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')
