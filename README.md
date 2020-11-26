## Tugas Melengkapi Pertemuan ke 9
Nama	: Syahru Raga Ramdhani <br>
Kelas	: TI.20.A.2 <br>
Nim	: 312010354 <br>
## Daftar Isi
| No | Isi |
| -- | --- |
| 1. | Tugas Praktikum 4 | 
| 2. | Tugas Praktikum 5 | 

### Tugas Praktikum 4

 **Soal** 

        Buat program sederhana untuk menambahkan data kedalam sebuah
        list dengan rincian sebagai berikut:
        • Progam meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
        • Tampilkan pertanyaan untuk menambah data (y/t?), apabila jawaban
          t (Tidak), maka program akan menampilkan daftar datanya.
        • Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%,
          uts: 35%, uas: 35%)
        • Buat flowchart dan penjelasan programnya pada README.md.
        • Commit dan push repository ke github.



## Syntax Sebagai Berikut

![gambar](/gambar/Capture1.PNG)

## Lanjutan Syntax diatas

![gambar](/gambar/Capture2.PNG)


## Hasil dari Output seperti gambar di bawah ini

![gambar](/gambar/Capture3.PNG) 

Berikut *souce code* nya
``` python
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
```     



### Tugas Praktikum 5 

  **Soal**

        Buat program sederhana yang akan menampilkan daftar nilai
        mahasiswa, dengan ketentuan
        • Program dibuat dengan menggunakan Dictionary
        • Tampilkan menu pilihan: (Tambah Data, Ubah Data, Hapus Data,
          Tampilkan Data, Cari Data)
        • Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%,
          uts: 35%, uas: 35%)
        • Buat flowchart dan penjelasan programnya pada README.md.
        • Commit dan push repository ke github.


## Syntax sebagai berikut

![gambar](/gambar/Capture4.PNG)

## Lanjutan syntax diatas

![gambar](/gambar/Capture5.PNG)

## Maka hasil output seperti di gambar ini

![gambar](/gambar/Capture6.PNG)


Berikut *souce code* nya
``` python
            print("====================================")
            print("======>  Program Input Data  <======")
            print("====================================")
            data = {}
            while True:
            print("")
                m = input("===>> (L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : <=== ")
                print("================================================================")
                print("| NO |  Nama     |   Nim    |  Tugas  |  UTS  |  UAS  |   Akir |")
                print("================================================================")
                print(">>>>>>>>>>>>>>>>>>>>>>>> TIDAK ADA DATA <<<<<<<<<<<<<<<<<<<<<<<<")
                if m.lower() == 'k':
                    break

                elif m.lower() == 'l':
                    print("----- DAFTAR NILAI -----")
                    print("==================================================================================")
                    print("| NO |   NAMA     |   NIM        |  TUGAS   |   UTS     |   UAS      |  AKHIR    |")
                    print("==================================================================================")
                    i = 0
                    for x in data.items():
                        i += 1
                        print("|  1 |{0:9}   |{1:9}     |{2:9} |{3:9}  |{4:9}   |{5:9}  |" .format(x[0], x[1][0],
                         x[1][1], x[1][2], x[1][3], x[1][4], i))

                    else:
                         print("====================>>>>>>>>>>>>> Tidak Ada Data <<<<<<<<<<<<<====================")

                elif m.lower() == 't':
                    print("----- Tambah Data -----")
                    nama = input("Nama                  : ")
                    nim = input("Nim                   : ")
                    tugas = float(input("Masukan Nilai Tugas   : "))
                    uts = float(input("Masukan Nilai UTS     : "))
                    uas = float(input("Masukan Nilai UAS     : "))
                    akhir = (int(tugas * .30)) + (int(uts * .35)) + (int(uas * .35))
                    data[nama] = nim, tugas, uts, uas, akhir

                elif m.lower() == 'u':
                    print("----- Ubah Data Mahasiswa -----")
                    nama = input("Nama  : ")
                    if nama in data.keys():
                        nim = input("Nim : ")
                        tugas = float(input("masukan nilai tugas : "))
                        uts = float(input("masukan nilai Uts : "))
                        uas = float(input("masukan nilai uas : "))
                        akhir = (int(tugas)* .30) + (int(uts)* .35) + (int(uas)* .35)
                        data[nama] = nim, tugas, uts, uas, akhir
    
                    else:
                         print("Tidak Ada data")

                elif m.lower() == 'h':
                    print("Hapus Data Mahasiswa")
                    nama = input("nama : ")
                    if nama in data.keys():
                        print("Datanya",nama,"adalah {0}".format(data[nama]))
                    else:
                        print("Tidaak Ada Data")

                else:
                    print("Pilih menu yang tersedia")
```
