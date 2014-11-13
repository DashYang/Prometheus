#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import os
import numpy
import math
import string
import matplotlib.pyplot as plt
import re

class Model:
	PATH = r"result"
	TIME = r"210735"
	
	def preProcess(self):
		PARAPATH = r"%s\%s\LdaParameter\LdaParameters.txt" % (self.PATH,self.TIME)
		
		file_object = open(PARAPATH)
		try:
			all_the_text = file_object.read()
			alpha = float(all_the_text.split('\n')[0].split('\t')[1])
			beta = float(all_the_text.split('\n')[1].split('\t')[1])
		finally:
			file_object.close()

 #��ģ��ѵ�������Ĵ�ת����һ����ΪKEY,����Ϊֵ���ֵ䡣
	def dictionary_found(wordlist):
		word_dictionary1={}
     	for i in xrange(len(wordlist)):
        	if i%2==0:
            	if word_dictionary1.has_key(wordlist[i])==True:
                	word_probability=word_dictionary1.get(wordlist[i])
                	word_probability=float(word_probability)+float(wordlist[i+1])
                	word_dictionary1.update({wordlist[i]:word_probability})
             	else:
                	word_dictionary1.update({wordlist[i]:wordlist[i+1]})
         	else:
            	pass
     	return word_dictionary1
	
	#���ڲ��Լ���ÿһ���ʣ����ֵ��в�������ʡ�
	def look_into_dic(dictionary,testset):         
     '''Calculates the TF-list for perplexity'''    
		frequency=[]
		letter_list=[]
		a=0.0
	   	for letter in testset.split():
       		if letter not in letter_list:
        		letter_list.append(letter)
        		letter_frequency=(dictionary.get(letter))
       			frequency.append(letter_frequency)
        	else:
            	pass

    	for each in frequency:
        	if each!=None:
            	a+=float(each)
         	else:
            	pass
     	return a
	
	def f_testset_word_count(testset):                                     #���Լ��Ĵ���ͳ��
    	'''reture the sum of words in testset which is the denominator of the formula of Perplexity'''
		testset_clean=testset.split()
    	return (len(testset_clean)-testset.count("\n"))

	def f_perplexity(word_frequency,word_count):             #���������
     '''Search the probability of each word in dictionary
     Calculates the perplexity of the LDA model for every parameter T'''
    	duishu=-math.log(word_frequency)
    	kuohaoli=duishu/word_count
    	perplexity=math.exp(kuohaoli)
    	return perplexity
	
	def graph_draw(topic,perplexity):             #��������������ȵ�����ͼ
    	x=topic
    	y=perplexity
    	plt.plot(x,y,color="red",linewidth=2)
     	plt.xlabel("Number of Topic")
    	plt.ylabel("Perplexity")
    	plt.show()
	
	def getPerplexity(self , time):
		self.preProcess()
		DOCPATH = r"%s%s\LdaResults\lda_2000.twords"
		file_object = open(PARAPATH)
		try:
			all_the_text = file_object.read()
			alpha = float(all_the_text.split('\n')[0].split('\t')[1])
			beta = float(all_the_text.split('\n')[1].split('\t')[1])
		finally:
			file_object.close()
		
		filenames = os.listdir(self.source_path)


if __name__ == "__main__":
	r = Model()
	topic=[]
	perplexity_list=[]
	f1=open('/home/alber/lda/GibbsLDA/jd/test.txt','r')      #���Լ�Ŀ¼
	testset=f1.read()
	testset_word_count=f_testset_word_count(testset)         #call the function to count the sum-words in testset
	for i in xrange(14):
  		dictionary={}
    	topic.append(5*(3i+1))                                                       #ģ���ļ����ĵ�����ʽ
    	trace="/home/alber/lda/GibbsLDA/jd/stats/model-final-"+str(5*(i+1))+".txt"   #ģ��Ŀ¼
     	f=open(trace,'r')
     	text=f.readlines()
    	word_list=[]
    	for line in text:
        	if "Topic" not in line:
            	line_clean=line.split()
            	word_list.extend(line_clean)    
        	else:
            	pass
    	word_dictionary=dictionary_found(word_list)
    	frequency=look_into_dic(word_dictionary,testset)      
    	perplexity=f_perplexity(frequency,testset_word_count)       
    	perplexity_list.append(perplexity)        
 	graph_draw(topic,perplexity_list)
	
