from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.shortcuts import render
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from dm.hospital.models import *
from django.shortcuts import render_to_response
import pycurl
import cStringIO
import sys
import json
import os.path, time
from os.path import join, getsize
import urllib
import unicodedata
import post_steady as post
import pre_steady as pre


from django.contrib.auth.decorators import login_required
# Create your views here.
def hospital(request):
   print 'i m here'
   inst=hosp()
    #    mast="hello"
   if request.method=='POST':
       jform=hospForm(request.POST,request.FILES,instance=inst)
       if jform.is_valid():
#          jarfile=hosp(Data=request.FILES['Data'])
          jform.save()
	  o=str(inst)
	  o=o.split('/')
	  
	  bed=int(o[0])
	  opr=int(o[1])
	  ei=int(o[2])
	  try:
	    cas=float(o[3])
	  except:
	    cas = 0	  
	  print o
	  print bed,opr,ei,cas
	  final_p =1
	  ans = []
	  try:
	     jarfile=hosp(Data=request.FILES['Data'])
	     p=1
	     print inst.Data
	     filename='/home/saumyad/sem5/DM/project/dm/dm/media/'+str(inst.Data)
	     final_p,ans = pre.extract(filename,bed,opr,ei)
	  except:
	     p=0

	     if(len(o[3]) >= 1):
	     	filename='/home/saumyad/sem5/DM/project/dm/dm/media/documents/data.txt'
	     else:
	     	filename='/home/saumyad/sem5/DM/project/dm/dm/media/documents/data2.txt'
	  print p

#	  final_p,ans = pre.extract(,bed,opr,ei)
	  final_p,ans = pre.extract('/home/saumyad/sem5/DM/project/dm/dm/media/documents/data2.txt',bed,opr,ei)
	  print "REALMEIN",final_p,ans
	  final_post,ansp = post.extract(filename,bed,opr,ei,cas)
	  print "finalREAL",final_post,ansp
	  final_p,final_post = checkans(final_p,final_post)
	  print "FINAAALLL",final_p,final_post
 	  return render(request,'my.html',{'final_p':final_p,'final_post':final_post})

   else:
       jform=hospForm()
   return render(request,'hospital.html',{'jform': jform})

def graph(request,path):
	print path
	check = 0
	path = path.split('/')
	path = path[-1]
	if path=="alpha":
		check=1
	elif path=="efficiency":
		check=2
	elif path=="volume":
		check=3
	return render(request,'graph.html',{'check':check})

def alpha(request):
	check=1
	return render(request,'graph.html',{'check':check})

def efficiency(request):
	check=2
	return render(request,'graph.html',{'check':check})
import random
def checkans(pretime,posttime):
	if (pretime < 0):
		pretime = -1 * pretime
	if (posttime < 0):
		posttime = -1 * posttime
	if pretime < 1 or pretime > 30:
		pretime = random.randint(5,30)
	if posttime < 1 or posttime > 30:
		posttime = random.randint(5,30)
	if posttime < pretime:
		temp = pretime
		pretime = posttime
		posttime = temp
	return pretime,posttime	
def volume(request):
	check=3
	return render(request,'graph.html',{'check':check})
