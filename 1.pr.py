nr = int(input("Introduceti nr culorii curcubeului ce doriti sa aflati (<8) = "))
cul = { 1: "Rosu" ,   2 : "Oranj", 3 : "Galben", 4 : "Verde", 5 : "Indogo", 6:"Albastru",7 : "Violet"}
culc = cul[nr]
if nr<8 and nr>0:
    print(culc)
else:
    pass