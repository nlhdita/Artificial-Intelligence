# TUGAS PARALEL 1 AI NI LUH MADE DITA ANJANI 1301174676 IFIK-41-01
import random

chrom = []
x1x2 =[]
fitness = []
ortu = []
x1 = []
x2 =[]
x = []
def chromo():
	n = 10
	for i in range (n):
		#pemilihan chromosom dgn cara random antara biner 0,1 namun disini dibagi dua
		#agar dapat dihitung x1 dan x2 secara terpisah
		xx1 = [random.randint(0,1) for i in range(3)]
		xx2 = [random.randint(0,1) for i in range(3)]
		x1.append(xx1)
		x2.append(xx2)
		ch = xx1 + xx2 #ini hasil chromosomnya
		chrom.append(ch)
	print("LIST CHROMOSOME : ",chrom)
	return(chrom)

def hitx(chrom):
	i=0
	for i in range(len(chrom)):
		h1 = (-3 + ((3-(-3))*((chrom[i][0]*(2**-1))+(chrom[i][1]*(2**-2))+(chrom[i][2]*(2**-3)))/((2**-1)+(2**-2)+(2**-3))))
		h2 = (-2 + ((2-(-2))*((chrom[i][3]*(2**-1))+(chrom[i][4]*(2**-2))+(chrom[i][5]*(2**-3)))/((2**-1)+(2**-2)+(2**-3))))	

		x = [h1]+[h2] #ini hasil perhitungan x1 dan x2 dijadikan dalam 1 list 2 dimensi
						# dimana 1 chromosom punya masing-masing x1 dan x2
		x1x2.append(x)
	print("ini list x1x2 : ",x1x2)
	return(x1x2)

def Fitnes(x1x2):
	for i in range (len(x1x2)):
		hitf= ((4-(2.1*x1x2[i][0]**2)+((x1x2[i][0]**4)/3))*x1x2[i][0]**2)+(x1x2[i][0]*x1x2[i][1])+(-4+(4*x1x2[i][1]**2))*(x1x2[i][1]**2)
		fit = 1/(hitf+0.0000001) #hasil fitness dibagi dan ditambah dengan 0.000001 demi menghindari pembagian dengan 0
		fitness.append(fit)
	print("ini fitness : ",fitness)
	return (fitness)

def Parent(fitness,x1x2,chrom):
    for passnum in range(len(fitness)-1,0,-1):
        for i in range(passnum):
            if fitness[i]>fitness[i+1]: #dilakukan sorting untuk mencari nilai fitness terkecil serta dilakukan sorting juga untuk var chrom, x1, x2, x1x2
                temp = fitness[i]
                fitness[i] = fitness[i+1]
                fitness[i+1] = temp
                temp = chrom[i]
                chrom[i] = chrom[i+1]
                chrom[i+1] = temp
                temp = x1x2[i]
                x1x2[i] = x1x2[i+1]
                x1x2[i+1] = temp
                temp = x1[i]
                x1[i] = x1[i+1]
                x1[i+1] = temp
                temp = x2[i]
                x2[i] = x2[i+1]
                x2[i+1] = temp
    print("ini sorted x1 : ", x1)
    print("ini sorted x2 : ",x2)
    a1 = fitness[0]
    print("ini fit parent1: ",a1)
    b1 = chrom[0]
    print("ini chrom parent1: ",b1)
    c1 = x1x2[0]
    print("ini x1x2 parent1: ",c1)

    a2 = fitness[1]
    print("ini fit parent2: ",a2)
    b2 = chrom[1]
    print("ini chrom parent2: ",b2)
    c2 = x1x2[1]
    print("ini x1x2 parent2: ",c2)
    p2 = [a2] + [b2] + [c2]
    par = [b1] + [b2]
    ortu.append(par)
    print("new parent : ")
    return(ortu)

def Crossover(Parent):
	temp = []
	temp = x1[1][0:3]
	x1[1][0:3] = x1[0][0:3]
	x1[0][0:3] = temp[0:3]
	#yang dicross hanya x1
	print("hasil cross sorted x1 : ", x1)
	for i in range (len(ortu)):
		x = x1[i]+x2[i]
		print("ini anak kromosom : ",x)
		return(x)

def Regenerasi(x):
	for i in range(2):
		print("generasi ke-",i)
		xx1 = x
		xx2 = [random.randint(0,1) for i in range(3)]
		x1.append(xx1)
		x2.append(xx2)
		ch = xx1 + xx2 #ini hasil chromosomnya
		chrom.append(ch)
	print("LIST CHROMOSOME : ",chrom)
	

if __name__ == '__main__':

	chromo()
	hitx(chrom)
	Fitnes(x1x2)
	Parent(fitness,x1x2,chrom)
	print(ortu)
	Crossover(Parent)

	Regenerasi(x)
