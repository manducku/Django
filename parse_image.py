# -*- coding: utf-8 -*-                       #인코딩 반드시 필요함
from urllib2 import urlopen
from HTMLParser import HTMLParser

class ImageParser(HTMLParser):                #img 태그를 찾기위해 HTML Parser를 상속
	def handle_starttag(self, tag, attrs):   #handle_starttag를 오버라이딩 
		if tag != 'img':
			return 
		if not hasattr(self, 'result'):
			self.result = []
		for name, value in attrs:
			if name == 'src':
				self.result.append(value)

def parseImage(data):              #이미지를 찾고, 그 리스트를 출력해주는 함수 
	parser = ImageParser()
	parser.feed(data)
	dataSet = set(x for x in parser.result)
	print '\n'.join(sorted(dataSet))

def main():
	url = "http://www.naver.com"

	f = urlopen(url)
	charset = f.info().getparam('charset')
	data = f.read().decode(charset)
	f.close()

	print "\n>>>>>>>>>>> Fetch Image from", url
	parseImage(data)

if __name__ == '__main__':
	main()
