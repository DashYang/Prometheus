#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  

import os
source_path = r"cppsource"
target_path = r"bin"
 #
class compile:
	def run(self):
		if not os.path.exists(source_path):
			print 'not exists this directory %s' % source_path
			os._exit(0)
	
		if not os.path.exists(target_path):
			os.makedirs(target_path)
			print 'directory is created!'
	
		filenames = os.listdir(source_path)

		for fn in filenames:
			infilepath = source_path + "\\" + fn
			outfilepath = target_path + "\\" + fn.split('.')[0] + ".exe"
			compile_string = "g++ %s -o %s" % (infilepath , outfilepath)
			#print compile_string
			if not os.system(compile_string):
				print "%s already been compiled as %s" %(infilepath , outfilepath)
			else:
				print "compile failure"

if __name__ == "__main__":  
	c = compile()
	c.run()

