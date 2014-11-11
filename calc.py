#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import os
import time

DocPath = r"data\LdaOriginalDocs"
Binpath = r"bin"
nowtime = time.strftime('%H%M%S',time.localtime(time.time()))
ResultPath = "result\\" +  nowtime
#书简介和微博的参数
SUMMARY = 21
WEIBO = 80

#以实验时间建立文件夹
if not os.path.exists(ResultPath):
	os.makedirs(ResultPath)
else:
	print "exists same name directory!"


doc = len(os.listdir(DocPath))

print 'doc %d' % doc
ParaPath = r"data\LdaParameter\LdaParameters.txt"
file_object = open(ParaPath)

try:
	all_the_text = file_object.read()
	topic = int(all_the_text.split('\n')[2].split('\t')[1])
finally:
     file_object.close()

jsd_cmd = r"%s\jsd %d %d %d <%s >%s\result_jsd_%d.txt" %(Binpath , SUMMARY , WEIBO , topic,"data\LdaResults\lda_2000.theta" , ResultPath , topic)
#print cmd
cos_cmd = r"%s\cos %d %d %d <%s >%s\result_cos_%d.txt" %(Binpath , SUMMARY , WEIBO , topic,"data\LdaResults\lda_2000.theta" , ResultPath , topic)

copy_cmd = r"XCOPY data %s/s" % ResultPath

print nowtime


os.system(jsd_cmd)
os.system(cos_cmd)
os.system(copy_cmd)
