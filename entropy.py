#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  

import os
source_path = r"stopdoc"
target_path = r"data\LdaOriginalDocs"

if not os.path.exists(source_path):
	print 'not exists this directory %s' % source_path
	os._exit(0)

filenames = os.listdir(source_path)

cnt = 0
for fn in filenames:
	infilepath = source_path + "\\" + fn
	outfilepath = target_path + "\\" + fn
	os.system("entropy <%s >%s" % (infilepath , outfilepath))
