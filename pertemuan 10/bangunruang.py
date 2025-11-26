import math

#kubus 
def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil

#BALOK
def balok(p,l,t):
    hasil = p * l * t
    return hasil

#prisma
def prisma(alas,tinggi_segitiga,tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil    

#TABUNG 
def tabung(jari_jari, tinggi):
    hasil = math.pi * math.pow(jari_jari,2) * tinggi
    return hasil

#kerucut 
def kerucut(jari_jari,tinggi):
    hasil = (1/3) *math.pi *math.pow(jari_jari,2) * tinggi
    return hasil