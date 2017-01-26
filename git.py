#Hákon Haraldsson
#25.1.2017
#Forritun 2
valmynd = 1
while valmynd != 4:
    teljari = 0
    print("1: 2 tölur")
    print("2: Nafn")
    print("3: Stafir")
    valmynd = int(input("Veldu verkefni "))                             #Velja Verkefni
    if valmynd == 1:
        tala1 = int(input("Sláðu inn fyrstu töluna "))                  #slærð inn tölu
        tala2 = int(input("Sláðu inn seinni töluna "))                  #Slærð inn tölu
        print("Samlagning talnana er :",tala1 + tala2)                  #Prentar summu
        print("Margföldun talnana er :", tala1 * tala2)                 #Prentar margföldun tölurnar
    if valmynd == 2:
        fornafn = input("Fornafn? ")                                    #Skrifar fornafn
        eftirnafn = input("Eftirnafn? ")                                #Skrifar eftirnafn
        print("Halló",fornafn,eftirnafn)                                #Prentar út fullt nafn
    if valmynd == 3:
        texti = input("Skrifaðu texta! ")                               #input
        for x in range(len(texti)):                                     #Í lengd textans
            if [x].isalpha or [x].isupper():                            #Ef stór
                if texti[x+1].islower:                                  #Ef næsti stafur er lítill
                    teljari += 1                                        #Hækkar um 1
        print("Stórir stafir : ", sum(1 for x in texti if x.isupper())) #prentar hversu margir stórir stafir
        print("Litlir stafir : ", sum(1 for x in texti if x.islower))   #prentar hversu margir litlir stafir
        print("Lítill stafur eftir stóran staf :", teljari)             #prentar hversu margir litlir stafir koma eftir stórum stöfum