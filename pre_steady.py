#!/bin/python

import random
import numpy as np
import numpy.linalg as lg
ans = ''
def extract(filen):
	filename = open(filen)
	# no_of_OR , beds and hospital efficiency
	data_number = 9
	#calculate total lines in file
	for i,val in enumerate(filename):
		pass

	#total number of lines
	lines = i + 1
	lines_left = lines
#	print lines
	filename.close()
	filename = open(filen)
	no_of_or = []
	beds = []
	h_eff = []
	orMeff = []			#cross multiply
	bedsMeff = []
	bedsMor = []
	ors = []			#squares of each term
	bedss = []
	effs = []
	waiting_time = []
	for lines in filename:
		# take out random 9 pairs of data
		if(lines_left > data_number):
			if (data_number > 9):
				break
			line_choice = random.randint(0,1)
			if (line_choice == 1):
				data_number += 1
			else:
				continue
			
		values = lines.split(' ')
		values[0] = int(values[0])
		values[1] = int(values[1])
		values[2] = float(values[2])
		values[3] = float(values[3].split('\n')[0])
		no_of_or.append(values[0])
		beds.append(values[1])
		h_eff.append(values[2])
		orMeff.append(values[0] * values[2])			#cross multiply
		bedsMeff.append(values[1] * values[2])
		bedsMor.append(values[1] * values[0])
		ors.append(values[0] * values[0])			#squares of each term
		bedss.append(values[1] * values[1])
		effs.append(values[2] * values[2])
		waiting_time.append(values[3])
		lines_left -= 1
		data_number += 1
#	print no_of_or, beds, h_eff,orMeff

	filename.close()
		
		#### compute matrices

		### data matrix
	data_matrix = np.array(no_of_or)
	data_matrix = np.vstack([data_matrix,beds])	
	data_matrix = np.vstack([data_matrix,h_eff])	
	data_matrix = np.vstack([data_matrix,orMeff])	
	data_matrix = np.vstack([data_matrix,bedsMeff])	
	data_matrix = np.vstack([data_matrix,bedsMor])	
	data_matrix = np.vstack([data_matrix,ors])	
	data_matrix = np.vstack([data_matrix,bedss])	
	data_matrix = np.vstack([data_matrix,effs])	
	print data_matrix
		### final waiting time matrix
	wtime_matrix = np.array(waiting_time)
	print wtime_matrix

		### compute inverse of data_matrix
	inverted_data = lg.inv(data_matrix)
	print inverted_data

#	inverted_data = data_matrix
		### multiply inverted with wtime
	ans = np.dot(wtime_matrix,inverted_data)
	ans = np.dot(inverted_data,wtime_matrix)
	print "coeff",ans		### the generated coefficients
	calculate_wait(100,5,1200,ans)


def calculate_wait(no_of_or, beds, h_eff,ans):
	wait_time = (ans[0]*no_of_or + ans[1]*beds + ans[2]*h_eff + ans[3]*beds*beds + ans[4]*no_of_or*no_of_or + ans[5] *h_eff*h_eff + ans[6] * beds * no_of_or + ans[7] * beds * h_eff + ans[8] * no_of_or * h_eff )/(24*36000)
	final =  wait_time
	print final


def main():
	extract('data2.txt')

if __name__ == '__main__':
	main()
