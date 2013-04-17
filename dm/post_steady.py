#!/bin/python

import random
import numpy as np
import numpy.linalg as lg
ans = ''

def extract(filen,bed1,or1,eff1,avol1):
	filename = open(filen)
	print "fsuidhiosdjgf",filename
	# no_of_OR , beds and hospital efficiency
	data_number = 15
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
	a_vol = []
	orMeff = []			#cross multiply
	bedsMeff = []
	bedsMor = []
	orMavol = []
	bedsMavol = []
	effMavol = []
	ors = []			#squares of each term
	bedss = []
	effs = []
	avols = []
	waiting_time = []
	for lines in filename:
		# takei out random 15 pairs of data
		if(lines_left > data_number):
			if (data_number < 0):
				break
			line_choice = random.randint(0,1)
			if (line_choice == 1):
				pass
#				data_number += 1
			else:
				lines_left -= 1
				continue
			
		values = lines.split(' ')
		values[0] = int(values[0])
		values[1] = int(values[1])
		values[2] = float(values[2])
		values[3] = float(values[3].split('\n')[0])
		values[4] = float(values[4].split('\n')[0])
		no_of_or.append(values[0])
		beds.append(values[1])
		h_eff.append(values[2])
		a_vol.append(values[4])
		orMeff.append(values[0] * values[2])			#cross multiply
		bedsMeff.append(values[1] * values[2])
		bedsMor.append(values[1] * values[0])
		orMavol.append(values[0] * values[4])			#cross multiply
		bedsMavol.append(values[1] * values[4])
		effMavol.append(values[2] * values[4])
		ors.append(values[0] * values[0])			#squares of each term
		bedss.append(values[1] * values[1])
		effs.append(values[2] * values[2])
		avols.append(values[4] * values[4])
		waiting_time.append(values[3])
		lines_left -= 1
		data_number -= 1
#	print  "HHEHEHE",no_of_or

	filename.close()
		
		#### compute matrices

		### data matrix
		
	data_matrix = np.array(np.ones(15))
	data_matrix = np.vstack([data_matrix,no_of_or])	
	data_matrix = np.vstack([data_matrix,beds])	
	data_matrix = np.vstack([data_matrix,h_eff])	
	data_matrix = np.vstack([data_matrix,a_vol])	
	data_matrix = np.vstack([data_matrix,orMeff])	
	data_matrix = np.vstack([data_matrix,bedsMeff])	
	data_matrix = np.vstack([data_matrix,bedsMor])	
	data_matrix = np.vstack([data_matrix,orMavol])	
	data_matrix = np.vstack([data_matrix,bedsMavol])	
	data_matrix = np.vstack([data_matrix,effMavol])	
	data_matrix = np.vstack([data_matrix,ors])	
	data_matrix = np.vstack([data_matrix,bedss])	
	data_matrix = np.vstack([data_matrix,effs])	
	data_matrix = np.vstack([data_matrix,avols])	
#	print data_matrix

	
		### final waiting time matrix
	wtime_matrix = np.array(waiting_time)
#	print wtime_matrix
	
		### compute inverse of data_matrix
	inverted_data = lg.inv(data_matrix)
#	print inverted_data
	
#	inverted_data = data_matrix
		### multiply inverted with wtime
	ans = np.dot(wtime_matrix,inverted_data)
	ans = np.dot(inverted_data,wtime_matrix)
#	print ans		### the generated coefficients
#	calculate_wait(100,10,600,ans,31)
#	calculate_wait(500,10,600,ans,31)
#	calculate_wait(100,5,1200,ans,31)
#	calculate_wait(500,5,1200,ans,31)
#	calculate_wait(500,5,600,ans,31)
	final,ans = calculate_wait(or1,bed1,eff1,ans,avol1)
	print final,ans
	return final,ans


def calculate_wait(no_of_or, beds, h_eff,ans,a_vol):
	wait_time = (ans[0] + ans[1]*no_of_or + ans[2]*beds + ans[3]*h_eff +ans[4]*a_vol+ ans[5]*no_of_or*h_eff + ans[6]*beds*h_eff + ans[7] *no_of_or*beds + ans[8] * no_of_or * a_vol  + ans[9] * beds * a_vol + ans[10] * a_vol * h_eff + ans[11] * no_of_or * no_of_or + ans[12] * beds * beds + ans[13] * h_eff * h_eff + ans[14] * a_vol * a_vol )/(2400000*3600000*10000000)
	final =  wait_time/100000000
	final =  1/(final/100000000)*100
	return final,ans


def main():
	extract('data.txt',100,5,600,31)
	extract('data.txt',100,5,600,132)
	extract('data.txt',100,5,1200,31)

if __name__ == '__main__':
	main()

