	#TUPRO 3
	# NI LUH MADE DITA ANJANI
	# 1301174676
	# IFIK-41-01

import csv

idfolnano = []
idfolmicro = []
idfolmedium = []
idengnano =[]
idengmicro = []
idengmedium = []
aray = []
arrayhasil = []
hasilarray = []
arraynilai = []
hasilno = []
hasilyes = []
hasilmaybe = []
hasilarr=[]
hasil=[]
arrsort = []
arayynilai = []
idhasil = []
hasilyes= []
def Folnano():
	for i in range(len(rows)):
		if ((rows[i][1] >=1526) and (rows[i][1] <=25000)):
			idf = 1
		elif ((rows[i][1] >25000) and (rows[i][1] <=95117)):
			idf = ((maksf - (rows[i][1]))/(maksf-minf))
		idfolnano.append(idf)
	print("===Followers nano===\n",idfolnano)

def Folmicro():
	for i in range(len(rows)):
		if ((rows[i][1] >=1526) and (rows[i][1] <=25000)):
			idf = ((rows[i][1] - minf)/(25000 - minf))
		elif ((rows[i][1] >25000) and (rows[i][1] <=75000)):
			idf = 1
		elif ((rows[i][1] >75000) and (rows[i][1]<=95117)):
			idf = (maksf-(rows[i][1]))/(maksf-75000)
		idfolmicro.append(idf)
	print("===Followers micro===\n", idfolmicro)

def Folmedium():
	for i in range(len(rows)):
		if((rows[i][1] >=1526) and (rows[i][1] <=75000)):
			idf = ((rows[i][1]) - minf)/(75000-minf)
		elif((rows[i][1]>75000) and (rows[i][1] <=95117)):
			idf = 1
		idfolmedium.append(idf)
	print("===Followers medium===\n", idfolmedium)

def Engnano():
	for i in range(len(rows)):
		if((rows[i][2] >= 0.1) and (rows[i][2] <=2.5)):
			ide = 1
		elif((rows[i][2] >2.5) and (rows[i][2] <=9.4)):
			ide = ((makse - (rows[i][2]))/(makse-mine))
		idengnano.append(ide)
	print("===Engagement Rate nano===\n", idengnano)

def Engmicro():
	for i in range(len(rows)):
		if((rows[i][2] >=0.1) and (rows[i][2] <=2.5)):
			ide = (rows[i][2]-mine)/(2.5-mine)
		elif((rows[i][2] >2.5) and (rows[i][2] <=7.5)):
			ide = 1
		elif((rows[i][2] >7.5) and (rows[i][2] <=9.4)):
			ide = (makse-(rows[i][2]))/(makse-7.5)
		idengmicro.append(ide)
	print("===Engagement Rate micro===\n", idengmicro)

def Engmedium():
	for i in range(len(rows)):
		if((rows[i][2] >0.1) and (rows[i][2] <=7.5)):
			ide = (rows[i][2] - mine) / (makse - mine)
		elif((rows[i][2]>7.5) and (rows[i][2] <=9.4)):
			ide = 1
		idengmedium.append(ide)
	print("===Engagement Rate medium===\n", idengmedium)

def Array():
	for i in range(len(rows)):
		arr = [idfolnano[i]] + [idfolmicro[i]] + [idfolmedium[i]] + [idengnano[i]] + [idengmicro[i]] + [idengmedium[i]]
		aray.append(arr)
	print("array\n", aray)

def Inferensi():
	
	# FC nano = 0, micro = 1, medium = 2
	# ER nano = 3, micro = 4, medium = 5
	for i in range(len(rows)):
	# KONDISI NO
		nano_nano = min(aray[i][0],aray[i][3])
		nano_micro = min(aray[i][0],aray[i][4])
		micro_nano = min(aray[i][1],aray[i][3])

	# KONDISI MAYBE
		medium_nano = min(aray[i][2],aray[i][3])
		nano_medium = min(aray[i][0],aray[i][5])

	# KONDISI YES
		micro_micro = min(aray[i][1],aray[i][4])
		micro_medium = min(aray[i][1],aray[i][5])
		medium_micro = min(aray[i][2],aray[i][4])
		medium_medium = min(aray[i][2],aray[i][5])

		yes = max(micro_micro, micro_medium, medium_micro, medium_medium)
		no = max(nano_nano, nano_micro, micro_nano)
		maybe = max(nano_medium, medium_nano)


		hasil = [yes] + [maybe] + [no]
		hasilarray.append(hasil)

	print("YES MAYBE NO\n", hasilarray)


def Defuzzy(hasilarray):
	for i in range(len(hasilarray)):
		y = ((40*hasilarray[i][2])+(60*hasilarray[i][1])+(80*hasilarray[i][0])) / (hasilarray[i][0] + hasilarray[i][1] + hasilarray[i][2])
		arraynilai.append(y)
		arayynilai.append(y)

	print("ARRAY NILAI\n", arayynilai)

	arraynilai.sort(reverse = True)
	# print("SORT\n", arraynilai)

	for i in range(len(arayynilai)):
		for j in range(len(arraynilai)):
			if (arayynilai[i] != arraynilai[j]):
				j = j+1
			elif (arayynilai[i] == arraynilai[j]):
				id = j+1
				idhasil.append(id)
		i+=1
	hasilyes = idhasil[0:20]
	print("CHOSEN = \n",hasilyes)
	print("jumlah yang terpilih = \n", len(hasilyes))
	with open('chosen.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		for i in (hasilyes) :
			writer.writerow([i])
	f.close()
if __name__ == '__main__':

	file = open('influencers2.csv', 'r')
	reader = csv.reader(file)
	rows = [[int(row[0]), int(row[1]), float(row[2])] for row in reader]
	print ("==== DATA DARI FILE UJI .CSV ====")
	for row in rows:
		print (row)

	maksf = 95117
	minf = 1526
	makse = 9.4
	mine = 0.1

	Folnano()
	Folmicro()
	Folmedium()

	Engnano()
	Engmicro()
	Engmedium()
	Array()
	Inferensi()
	Defuzzy(hasilarray)
	
