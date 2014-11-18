#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  

import os
import math
from operator import itemgetter, attrgetter  

class parafactory:
	source_path = r"stopdoc"
	target_path = r"data\LdaOriginalDocs"
	docs = []
	limit = 5

	def read_doc_to_dic(self , name):
		raw_dic = {};
		file = open(name)
		line = file.readline()
		length = 0;
		doc_line = ""
		while line:
			line = line.strip('\n')
			for word in line.split(' '):
				raw_dic[word] = raw_dic.get(word, 0) + 1
				doc_line += word + " "
				length += 1
			doc_line += "\n"
			line = file.readline()
		self.docs.append(doc_line)
		dic = {'raw_dic':raw_dic , 'length':length}
		return dic

	def read_folder(self , name):
		filenames = os.listdir(self.source_path)
		dic_list = []
		global_dic = {}

		for fn in filenames:
			filepath = self.source_path + "\\" + fn
			dic = self.read_doc_to_dic(filepath)
			print filepath + " done"
			for key in dic['raw_dic']:
				global_dic[key] = global_dic.get(key , 0) + 1
			dic_list.append(dic)
		
		paralist = {'dic_list':dic_list , 'global_dic':global_dic}
		return paralist
	
	#calculate entropy & TF-IDF 
	def calculate_entropy_and_tf_idf(self):
		paralist = self.read_folder(self.source_path)
		doc_paralist = []
		global_dic = paralist['global_dic']
		dic_list = paralist['dic_list']
		folder_size = len(dic_list)
		print 'folder_size%d' % folder_size
		for para in dic_list:
			kvmap = [];
			raw_dic = para['raw_dic']
			length = int(para['length'])
			for key in raw_dic:
				TF = 1.0 * raw_dic[key] / length #also p
				IDF =  math.log(folder_size / global_dic[key])
				print "%s %f %f" %(key , TF , IDF)
				entropy = - TF * math.log(TF) / math.log(2) 
				kvmap.append((key , TF * IDF * entropy))
			doc_paralist.append(kvmap)
		return doc_paralist
	
	#clear low value word
	def clear_folder(self ):
		list = self.calculate_entropy_and_tf_idf()
		for doc_index in range(len(list)):
			kvmap = list[doc_index]
			doc = self.docs[doc_index]
			newdoc = ""
			sortkvmap = sorted(kvmap , key=itemgetter(1) ,reverse=True)
			for row in doc.split('\n'):
				print "row:" + row
				for word in row.split():
					for index in range(self.limit):
						if word == sortkvmap[index][0]:
							newdoc += word + " "
				newdoc += '\n'
				print doc
				print "after"
				print newdoc

	
	def getDocs(self):
		return self.docs

def cmp(a ,b):
	return a[1] < b[1]

if __name__ == "__main__":
	pf = parafactory()
	pf.clear_folder()

			
