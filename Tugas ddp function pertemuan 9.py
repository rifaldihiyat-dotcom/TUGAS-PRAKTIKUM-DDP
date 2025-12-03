#celcius ke fahrenheit
print("SOAL NO 1")
def celcius_ke_fahrenheit(celcius):
    return (celcius*9/5) + 32

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

#IS_GENAP
print("SOAL NO 2")
def is_genap(bilangan):
    return bilangan % 2==0

print(is_genap(4))
print(is_genap(7))

#trus or false 
print("SOAL NO 3")
def nilai(n):
    if n <=75 :
        return "lulus"
    else:
        return "gagal"
print(nilai(80))
print(nilai(60))

#bilangan ganjil 
print("SOAL NO 4")
def bilangan(n):
    for i in range (1,n):
        if i % 2 !=0:
            print (i,end=",")
bilangan(20)

def bilangan(angka):
    for i in range (1,angka):
        if i % 2 != 0:
            print(i)
bilangan(20)

def nilai (n=0):
    if n <= 60:
        print("tidak lulus ")
    else: