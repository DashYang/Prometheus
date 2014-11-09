#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  

import os
import compile

class extract:
	source_path = r"segmentDoc"
	target_path = r"stopdoc"
	bin_path = r"bin"

	def run(self):
		if not os.path.exists(self.source_path):
			print 'not exists this directory %s' % self.source_path
			os._exit(0)

		filenames = os.listdir(self.source_path)
		binfilepath = self.bin_path + "\\" + 'extract'
		for fn in filenames:
			infilepath = self.source_path + "\\" + fn
			outfilepath = self.target_path + "\\" + fn
			
			os.system("%s <%s >%s" % (binfilepath , infilepath , outfilepath))
			print "%s already been extracted as %s" %(infilepath , outfilepath)
	
if __name__ == "__main__":  
#	c = compile.compile()
#	c.run()
	e = extract()
	e.run()

