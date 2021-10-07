#Frekuentziaz testua desenkriptatuko duen kodea
def desenkriptatufrekuentziaz(testua) :
	#Textuko hutsuneak kendu
	testu2 = testua.replace(" ","")
	guztira = len(testu2)
	#Frekuentziako array-a eta hizki bakoitzeko kopurua gordeko duen matrizea sortu
	frecuencia = ['E','A','O','L','S','N','D','R','U','I','T','C','P','M','Y','Q','B','H','G','F','V','J','Ñ','Z','X','K','W']
	kontadorea = [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
	pos = 0
#65 -> 'A' eta 90 -> 'Z'. Python in range ez du azkenengoa hartzen beraz, 90+1
	for i in range(65,91) :
		karak = chr(i)
		#Kontadorea balioekin bete
		kontadorea[1][pos] = testu2.count(karak)
		pos = pos+1

	letra = '0'
	numero = 0

#Kontadorea matrizeko hizki bakoitza (kopuruaren arabera) dagokion frecuencia array-ko hizkia da esleituko zaio
	for i in range(0,26) :
		for j in range (i,26) :
			if i!=j :
				if kontadorea[1][i] < kontadorea[1][j] :
					letra = kontadorea[0][i]
					numero = kontadorea[1][i]
					kontadorea[0][i] = kontadorea[0][j]
					kontadorea[1][i] = kontadorea[1][j]
					kontadorea[0][j] = letra
					kontadorea[1][j] = numero

	pos = 0
	n = 0
#Testuari aurretik egindako aldaketak esleituko zaizkio
	for i in testua :
		aurkitua = False

		while (pos < 26 and aurkitua == False) :
			if i == kontadorea[0][pos] :
				testua = testua[:n] + frecuencia[pos] + testua[n+1:]
				pos = 0
				aurkitua = True
			else :
				pos = pos+1
		if pos >= 26 :
			pos = 0
		n = n+1
	print (testua)
#-----------------------------------------------------------------------------------------------------------
#Testuan aldaketak egiten dituen funtzioa
def sustituir (texto,mod,original,nueva) :
	for i in range(0,mezuluzera) :
		if texto[i] == original and mod[i] == False :
			texto = texto[:i] + nueva + texto[i+1:]
			mod[i] = True
	return texto, mod
#-----------------------------------------------------------------------------------------------------------
#Testuko karaktereak aldatu daitezkeen ala ez adieraziko duen array-a sortzen duen funtzioa
#modificado = True denean, karaktere hori finkoa izango da (ezin izango dugu aldatu)
#modificado = False denean, karaktere hori aldatu behar izango dugu
def aldatutakoArrayaSortu(texto) :
	#mezuluzera = len(texto)
	modificado = [0] * mezuluzera
	for i in range(0,mezuluzera) :
		if ord(testua[i]) >= 65 and ord(testua[i]) <=90 :
			modificado[i] = False
		else :
			modificado[i] = True
	return modificado
#-----------------------------------------------------------------------------------------------------------

testua = input("Dame texto\n")
mezuluzera = len(testua)
modificado = aldatutakoArrayaSortu(testua)

#testua, modificado = descifratu(testua,modificado)

testua, modificado = sustituir (testua,modificado,'A','D')
testua, modificado = sustituir (testua,modificado,'C','I')
testua, modificado = sustituir (testua,modificado,'D','P')
testua, modificado = sustituir (testua,modificado,'E','A')
testua, modificado = sustituir (testua,modificado,'F','X')
testua, modificado = sustituir (testua,modificado,'G','J')
testua, modificado = sustituir (testua,modificado,'H','T')
testua, modificado = sustituir (testua,modificado,'I','O')
testua, modificado = sustituir (testua,modificado,'J','N')
testua, modificado = sustituir (testua,modificado,'K','R')
testua, modificado = sustituir (testua,modificado,'L','Z')
testua, modificado = sustituir (testua,modificado,'N','S')
testua, modificado = sustituir (testua,modificado,'M','H')
testua, modificado = sustituir (testua,modificado,'O','F')
testua, modificado = sustituir (testua,modificado,'P','M')
testua, modificado = sustituir (testua,modificado,'Q','B')
testua, modificado = sustituir (testua,modificado,'R','C')
testua, modificado = sustituir (testua,modificado,'S','Q')
testua, modificado = sustituir (testua,modificado,'T','L')
testua, modificado = sustituir (testua,modificado,'U','G')
testua, modificado = sustituir (testua,modificado,'V','Y')
testua, modificado = sustituir (testua,modificado,'X','E')
testua, modificado = sustituir (testua,modificado,'Z','U')


print ("\n")
print (testua)
