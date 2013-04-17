#!/usr/bin/python
from pylab import *
def makegraph():
	x=[120,200,300,350,355,400]
	y=[10,20,65,140,155,850]
	plot(x,y)
	xlabel("Patient Volume/Day")
	ylabel("Patient Wating Time")
	show()
if __name__=='__main__':
    makegraph()

