x = 0
names = []
nim = []
tugas = []
uts = []
uas = []
total = []

while True:
    nama = input("Nama    : ")
    names.append(nama)
    Nim = input("Nim     : ")
    nim.append(Nim)
    Tugas = input("Tugas   : ")
    tugas.append(Tugas)
    UTS = input("UTS     : ")
    uts.append(UTS)
    UAS = input("UAS     : ")
    uas.append(UAS)
    Total = (int(Tugas)* .30) + (int(UTS)* .35) + (int(UAS)* .35)
    total.append(Total)

    data=''
    while data != 'y' and data != 't':
        data = input("Tambah Data (y/t)? ")
    
    x += 1
    if data == 't':
        break



print("=====================================================================")
print("| NO |  Nama            |   Nim      |  Tugas   | UTS | UAS | Akhir |")
print("=====================================================================")

for n in range(x):
    print("|",n+1, " | ",names [n],"         |",nim[n]," |",tugas [n], "      |",uts[n], 
    " |",uas[n]," |",total[n],"|")
print("=====================================================================")