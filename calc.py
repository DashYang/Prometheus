#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import os

DocPath = r"data\LdaOriginalDocs"
Binpath = r"bin"
SUMMARY = 21
WEIBO = 80

doc = len(os.listdir(DocPath))

print 'doc %d' % doc
ParaPath = r"data\LdaParameter\LdaParameters.txt"
file_object = open(ParaPath)

try:
	all_the_text = file_object.read()
	topic = int(all_the_text.split('\n')[2].split('\t')[1])
finally:
     file_object.close( )

jsd_cmd = r"%s\jsd %d %d %d <%s >result_jsd_%d.txt" %(Binpath , SUMMARY , WEIBO , topic,"data\LdaResults\lda_2000.theta",topic)
#print cmd
cos_cmd = r"%s\cos %d %d %d <%s >result_cos_%d.txt" %(Binpath , SUMMARY , WEIBO , topic,"data\LdaResults\lda_2000.theta",topic)

os.system(jsd_cmd)
os.system(cos_cmd)
