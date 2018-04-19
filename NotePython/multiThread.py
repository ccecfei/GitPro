# coding = utf-8




import requests
import time 
import datetime

from pprint import pprint as pprint
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# resp = requests.get('http://www.ip138.com/')
urls = (
	# 'https://github.com/ccecfei/GitPro',
	# 'https://github.com/ccecfei?tab=stars',
	# 'https://github.com/CyC2018/Interview-Notebook',
	# 'https://github.com/gothinkster/realworld',

	'http://www.163.com/',
	'http://news.163.com/',
	'http://sports.163.com/',
	'http://money.163.com/stock/',
)

def timeCost(func):
	def wrapper(*args, **kwargs):
		before = datetime.datetime.now()
		result = func(*args, **kwargs)
		after = datetime.datetime.now()
		print( '%s, Time cost: %s' % (func.__name__, (after -before)) )
		return result
	return wrapper


@timeCost
def alone():
	contents = [requests.get(url) for url in urls]


@timeCost
def multiTh():
	pool = ThreadPoolExecutor(max_workers=4)
	list(pool.map(requests.get, urls))


@timeCost
def multiPr():
	pool = ProcessPoolExecutor(max_workers=4)
	list(pool.map(requests.get, urls))


def main():
	alone()
	multiTh()
	multiPr()


if __name__ == '__main__':
	main()







