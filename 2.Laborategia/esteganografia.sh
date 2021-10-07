#1.irudia aldagaian, mezua duen irudi baten izena gordeko du (imagen22.jpg hain zuzen ere)
#md5sum -> irudien hash-a aterako du.
#grep -> hash berdina duten irudien bilaketa egingo du.
#head -n 1 -> geratzen diren irudi guztien artean, lehenengoa hartu
#cut -d -f -> irudiko izena atera
irudia=$(md5sum irudia/* | grep "e5ed313192776744b9b93b1320b5e268" | head -n 1 | cut -d " " -f 3)

#Behin irudiko izena edukita, stegosuite programa exekutatu lortutako irudiarekin
stegosuite $irudia
