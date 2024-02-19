# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
birinciSayi=1
ikinciSayi=1

dizi= []
dizi.append(birinciSayi)
dizi.append(ikinciSayi)
for i in range(1,19):
    geciciToplam= birinciSayi + ikinciSayi 
    dizi.append(geciciToplam) 
    birinciSayi= ikinciSayi
    ikinciSayi=geciciToplam
print(dizi)


# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

bolenler= 0

sayi= int(input("bir sayı giriniz: "))
for i in range(1,sayi):
    if sayi%i==0:
        bolenler+= i
if sayi== bolenler:
    print(f"girdiğiniz sayı {sayi} mukemmel sayıdır.")
else:
    print(f"girdiğiniz sayı {sayi} mükemmel sayı değildir.")


# 3- Kullanıcıdan girilen sayıların EBOB ve EKOK'unu bulan programı yazınız.

sayi1= int(input("birinci sayiyi giriniz: "))
sayi2= int(input("ikinci sayiyi giriniz: "))

if sayi1<sayi2:
    kucukSayi= sayi1
else:
    kucukSayi=sayi2

for i in range(1, kucukSayi+1):
    if sayi1%i ==0 and sayi2%i ==0:
        ebob= i
        ekok= (sayi1*sayi2)//ebob 

print("ebob: ", ebob)  
print("ekok: ", ekok)

# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
sayi= int( input("Bir sayi girin: "))
i =2
asalmi= True

if sayi==1 or sayi==0 :
    asalmi = False

while i<sayi:
    if sayi %i == 0:
        asalmi = False
        break
    else:
        i+= 1

if asalmi:
    print("sayi asaldir")
else:
    print("sayi asal degildir")

#veya for döngüsüyle :
sayi=int(input("Sayıyı Girin : "))
if sayi > 1:
   
   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(sayi," Asal Sayı Değildir.")
           break
   else:
       print(sayi," Asal Sayıdır.")

else:
   print(sayi," Asal Sayı Değildir.")



# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
sayi = int(input("Bir sayı girin: "))
i = 2
print(sayi, "sayısının asal çarpanları:")
while i <= sayi:
    if sayi % i == 0:
        print(i)
        sayi //= i
    else:
        i += 1