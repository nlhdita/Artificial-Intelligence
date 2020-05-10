import random
import csv

chrom=[]
ch = []
kd = []
data_latih = []
data_uji =[]
chros = []
pop = []
arrbenar = []

print("NI LUH MADE DITA ANJANI")
print("1301174676")
print("IFIK-41-01")


def decode():
	file = open('data_latih_opsi_1.csv', 'r')
	reader = csv.reader(file)
	rows = [[str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])] for row in reader]
	print ("==== DATA DARI FILE .CSV ====")
	for row in rows:
		print (row)
	for row in rows:
		global kd
		kd= []
		if (row[0] == "rendah"):
			kd.append(0)
			kd.append(0)
			kd.append(1)
		elif(row[0] == "normal"):
			kd.append(0)
			kd.append(1)
			kd.append(0)
		elif(row[0] == "tinggi"):
			kd.append(1)
			kd.append(0)
			kd.append(0)
		if(row[1] == "pagi"):
			kd.append(0)
			kd.append(0)
			kd.append(0)
			kd.append(1)
		elif(row[1] == "siang"):
			kd.append(0)
			kd.append(0)
			kd.append(1)
			kd.append(0)
		elif(row[1] == "sore"):
			kd.append(0)
			kd.append(1)
			kd.append(0)
			kd.append(0)
		elif(row[1] == "malam"):
			kd.append(1)
			kd.append(0)
			kd.append(0)
			kd.append(0)
		if(row[2] == "hujan"):
			kd.append(0)
			kd.append(0)
			kd.append(0)
			kd.append(1)
		elif(row[2] == "rintik"):
			kd.append(0)
			kd.append(0)
			kd.append(1)
			kd.append(0)
		elif(row[2] == "berawan"):
			kd.append(0)
			kd.append(1)
			kd.append(0)
			kd.append(0)
		elif(row[2] == "cerah"):
			kd.append(1)
			kd.append(0)
			kd.append(0)
			kd.append(0)
		if(row[3] == "rendah"):
			kd.append(0)
			kd.append(0)
			kd.append(1)
		elif(row[3] == "normal"):
			kd.append(0)
			kd.append(1)
			kd.append(0)
		elif(row[3] == "tinggi"):
			kd.append(1)
			kd.append(0)
			kd.append(0)
		if(row[4] == "ya"):
			kd.append(1)
		elif(row[4] == "tidak"):
			kd.append(0)
		data_latih.append(kd)

	print("\n")
	print("==== HASIL DECODE DATA ==== ")
	print(data_latih)
	return(data_latih)

def krom():
	print("======Kromosom Random======")
	n = random.randint(5,20)
	for i in range (n):
		global chrom
		chrom = []
		chrom = [random.randint(0,1) for i in range(15)]
		chros.append(chrom)
	print(chros)
	return(chros)

def check(data_latih, chros):
	hasil1 = True
	hasil2 = True
	hasil3 = True
	hasil4 = True
	hasil5 = True
	hasil_akhir = True
	benar=0
	for i in range(len(chros)):
		for k in range(len(chros[i])):
			benar_banget =0
			if(((chros[i][0] and data_latih[i][0]) == 1) or ((chros[i][1] and data_latih[i][1]) ==1 ) or ((chros[i][2] and chros[i][2])== 1)):
				hasil1 = True
			if(((chros[i][3] and data_latih[i][3]) == 1) or ((chros[i][4]and data_latih[i][4])== 1) or ((chros[i][5] and data_latih[i][5])== 1) or ((chros[i][6] and data_latih[i][6])== 1)):
				hasil2 = True
			if(((chros[i][7] and data_latih[i][7]) ==1) or ((chros[i][8] and data_latih[i][8])==1) or ((chros[i][9] and data_latih[i][9])==1) or ((chros[i][10] and data_latih[i][10])==1)):
				hasil3 = True
			if(((chros[i][11] and data_latih[i][11])==1) or ((chros[i][12] and data_latih[i][12])==1) or ((chros[i][13] and data_latih[i][13])==1)):
				hasil4 = True
			if((chros[i][14] and data_latih[i][14])==1):
				hasil5 = True
			if((hasil1 == hasil2) and (hasil2 == hasil3) and (hasil3 == hasil4) and (hasil4 == hasil5)):
				hasil_akhir = True
			if(hasil_akhir):
				benar = benar + 1
		print(chros[i])
		benar_banget = benar
		print("jumlah data benar : ",benar_banget)
		print("jumlah data_latih : ",len(data_latih))
		benar_parah = (benar_banget/len(data_latih))*100
		print("fitness : ",benar_parah)
		arrbenar.append(benar_parah)
	print("array fitness : ",arrbenar)
	return(arrbenar)

def Parent(arrbenar):
	print("ARRAY FITNESS")
	print(sorted(arrbenar))
	

def decodeuji():
	file = open('data_uji_opsi_1.csv', 'r')
	reader = csv.reader(file)
	rows = [[str(row[0]), str(row[1]), str(row[2]), str(row[3])] for row in reader]
	print ("==== DATA DARI FILE UJI .CSV ====")
	for row in rows:
		print (row)
	for row in rows:
		global kd
		kd= []
		if (row[0] == "Rendah"):
			kd.append(0)
			kd.append(0)
			kd.append(1)
		elif(row[0] == "Normal"):
			kd.append(0)
			kd.append(1)
			kd.append(0)
		elif(row[0] == "Tinggi"):
			kd.append(1)
			kd.append(0)
			kd.append(0)
		if(row[1] == "Pagi"):
			kd.append(0)
			kd.append(0)
			kd.append(0)
			kd.append(1)
		elif(row[1] == "Siang"):
			kd.append(0)
			kd.append(0)
			kd.append(1)
			kd.append(0)
		elif(row[1] == "Sore"):
			kd.append(0)
			kd.append(1)
			kd.append(0)
			kd.append(0)
		elif(row[1] == "Malam"):
			kd.append(1)
			kd.append(0)
			kd.append(0)
			kd.append(0)
		if(row[2] == "Hujan"):
			kd.append(0)
			kd.append(0)
			kd.append(0)
			kd.append(1)
		elif(row[2] == "Rintik"):
			kd.append(0)
			kd.append(0)
			kd.append(1)
			kd.append(0)
		elif(row[2] == "Berawan"):
			kd.append(0)
			kd.append(1)
			kd.append(0)
			kd.append(0)
		elif(row[2] == "Cerah"):
			kd.append(1)
			kd.append(0)
			kd.append(0)
			kd.append(0)
		if(row[3] == "Rendah"):
			kd.append(0)
			kd.append(0)
			kd.append(1)
		elif(row[3] == "Normal"):
			kd.append(0)
			kd.append(1)
			kd.append(0)
		elif(row[3] == "Tinggi"):
			kd.append(1)
			kd.append(0)
			kd.append(0)
		data_uji.append(kd)

	print("\n")
	print("==== HASIL DECODE DATA UJI==== ")
	print(data_uji)
	return(data_uji)



if __name__ == '__main__':
	decode()
	krom()
	check(data_latih,chros)
	Parent(arrbenar)
	decodeuji()
