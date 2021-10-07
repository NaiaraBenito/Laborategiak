#eskuzDeszifratu.py antzekoa, baina askoz txukunagoa
def sustituir (texto,mod,original,nuevo) :
	pos = 0
	for i in texto :
		if i == original and mod[pos] == False :
			texto = texto[:pos] + nuevo + texto[pos+1:]
			mod[pos] = True
		pos = pos + 1
	return texto

#------------------------------------------------------------------
def modificados (texto) :
	tamaño = len(texto)
	mod = [False] * tamaño
	pos = 0
	for i in texto :
		if ord(i) < 65 or ord(i) > 90 :
			mod[pos] = True
		pos = pos + 1
	return mod
#------------------------------------------------------------------
texto = input ("Dame el texto a traducir:\n")
print ("\n")

mod = modificados (texto)

texto = sustituir (texto,mod,'A','D')
texto = sustituir (texto,mod,'C','I')
texto = sustituir (texto,mod,'D','P')
texto = sustituir (texto,mod,'E','A')
texto = sustituir (texto,mod,'F','X')
texto = sustituir (texto,mod,'G','J')
texto = sustituir (texto,mod,'H','T')
texto = sustituir (texto,mod,'I','O')
texto = sustituir (texto,mod,'J','N')
texto = sustituir (texto,mod,'K','R')
texto = sustituir (texto,mod,'L','Z')
texto = sustituir (texto,mod,'N','S')
texto = sustituir (texto,mod,'M','H')
texto = sustituir (texto,mod,'O','F')
texto = sustituir (texto,mod,'P','M')
texto = sustituir (texto,mod,'Q','B')
texto = sustituir (texto,mod,'R','C')
texto = sustituir (texto,mod,'S','Q')
texto = sustituir (texto,mod,'T','L')
texto = sustituir (texto,mod,'U','G')
texto = sustituir (texto,mod,'V','Y')
texto = sustituir (texto,mod,'X','E')
texto = sustituir (texto,mod,'Z','U')

print (texto)
