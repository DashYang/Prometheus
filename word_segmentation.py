#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  

import urllib
import urllib2
import re
import os

def reg_match(regex , html):
	pattern = re.compile(regex)
	match = pattern.findall(html)
	if match != []:
		return match
	else:
		return [""]

def extract(mydata):
	url = 'http://www.xunsearch.com/scws/demo/v4.php'
	values = {'mydata':mydata,
		'ignore':'yes',
		'showa':'yes',
		'limit':'10',
		'xattv':'%7Ev'
		}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	regex = r"<textarea .*?>([\s\S]+?)</textarea>"
	m = reg_match(regex , the_page)
	if m:
		return m[1]
	else:
		return "not match"

#需要分词的路径
FindPath = r"testDoc"
OutputPath = r"segmentDoc"
if not os.path.exists(OutputPath):
	os.makedirs(OutputPath)
FileNames=os.listdir(FindPath) 
for fn in FileNames:
	file = open(FindPath+ "\\" +fn)
	line = file.readline()
	mydata = ""
	while line:
		mydata += line
		line = file.readline()
	
	result = extract(mydata)
	file_object = open(OutputPath + "\\" + fn, 'w')
	file_object.write(result.strip())
	file_object.close( )
	print '%s done!' % fn
	
