#Hákon Haraldsson
valmynd = 1:
while valmynd != 4:
    print("1: 2 tölur")
    print("2: Nafn")
    print("3: Stafir")
    valmynd = int(input("Veldu verkefni"))
    if valmynd == 1:
        tala1 = int(input("Sláðu inn fyrstu töluna"))
        tala2 = int(input("Sláðu inn seinni töluna"))
        print("Samlagning talnana er :",tala1 + tala2)
        print("Margföldun talnana er :", tala1 * tala2)