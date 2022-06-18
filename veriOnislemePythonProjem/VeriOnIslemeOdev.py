import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt
import  pandas as pd
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
#from PyQt5.uic import loadUi
from qt_designerr_python import *
from qt_designerr_python import Ui_MainWindow
'''

#uygulama olusturma
Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow() #ui ile kullanım kolaylıgı icin kısaltma yaptım
ui.setupUi(penAna)
penAna.show() #tasarladığımız penceriyi sunmus olduk
sys.exit(Uygulama.exec_())

class MyClass(QMainWindow):
    def __init__(self):
        super().__init__()
        #loadUi('qt_designerr.ui',self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.PushButton.setText("denemeee")
        #self.ui.PushButton.setText("Eksik Veri Tamamla")
app=QApplication([])
window=MyClass()
window.show()
app.exec_()
'''
#veri tabani kısmı
import xlrd
import sqlite3 as lite
'''from openpyxl import Workbook,load_workbook
wb = load_workbook("data.xlsx")
ws = wb.active

# Aktif çalışma sayfasının adını yazdırma
print(wb.sheetnames)      # <Worksheet "data">

wb = load_workbook("data.xlsx")
ws = wb.sheetnames
print(ws)
for satir in range(1,20):
    for sutun in range(1,34):
        print(str(ws.cell(satir,sutun).value))
    print()
dosya="data.xlsx"
inputWorkbook=xlrd.open_workbook(dosya)
inputWorksheet = inputWorkbook.sheet_by_index(0)
print(inputWorksheet.nrows)
print(inputWorksheet.ncols) '''

print("---VERİ SETİM--------------------------------------------------------------------------")
df = pd.read_table("veriSeti.TXT")
print(df)
print("---EKSİK VERİLER GOSTERILIYOR--------------------------------------------------------------------------")
df = pd.read_table("data.TXT",sep=",",na_values="?")
print(df)
print("---EKSİK VERİLER TAMAMLANDI------------------------------------------------------------------")
bf=df.fillna(df.mean())
print(bf)
'''b print("---ORTALAMA-STANDART SAPMA-MİN-MAX DEGERLER-YUZDELİK DILIMLER--------------------------")
aralik=bf.describe()
print(aralik)

Q1 = bf.n3.quantile(0.25)
Q3 = bf.n3.quantile(0.75)
IQR = Q3-Q1
yuksekDeger = Q3+1.5*IQR
alcakDeger = Q1-1.5*IQR
print('Olabilecek en kucuk deger')
print(alcakDeger)
print('Olabilecek en buyuk deger')
print(yuksekDeger)
i=0
while(i<19):
    i=i+1
    if (bf.n3[i]<alcakDeger) :
        print('Aykiri deger bulundu')
        print(bf.n3[i])
    elif (bf.n3[i]>yuksekDeger):
        print('Aykiri deger bulundu')
        print(bf.n3[i])
        
print("Histogram")
#set = pd.read_csv("data.TXT",sep=",")
#print(set.head())

#hisGr=frekans.plot.hist(alpha=0.7)
#print(plt.show())

#toplHisGr=frekans.plot.hist(alpha=1,stacked=True,bins=25)
#print(plt.show())

#grafik çizimi
set=bf
hisGr=set["n1"].plot.hist(orientation="horizontal")
print(plt.show())
#kutuGrafigi
renk={"boxes":"Red","whiskers":"blue","medians":"black","caps":"green"}
kutuGra=set.plot.box(color=renk)
print(plt.show())

bf['n33'].plot(kind='box')
print(plt.show()) b'''

def modAl(liste):
    sayac=0
    for i in liste:
        teksa=liste.count(i)
        if teksa>sayac:
            sayac=teksa
            deger=i
    return deger

def ortalamaBul(vektor):
    veriAdedi = len(vektor)
    if veriAdedi <= 1:
        return vektor
    else:
        return sum(vektor) / veriAdedi

def standartSapmaBul(vektor):
    sd = 0.0 # standart sapma
    veriAdedi = len(vektor)
    if veriAdedi <= 1:
        return 0.0
    else:
        for _ in vektor:
            sd += (float(_) - ortalamaBul(vektor)) ** 2
        sd = (sd / float(veriAdedi)) ** 0.5
        return sd

def varyansBul(vektor):
    return standartSapmaBul(vektor) ** 2

def medyanBul(vektor):
    vektor = sorted(vektor)
    veriAdedi = len(vektor)
    if veriAdedi % 2 == 1:
        return vektor[veriAdedi // 2]
    else:
        i = veriAdedi // 2
        return (vektor[i - 1] + vektor[i]) / 2

def cikis():# Çıkış fonksiyonu
    print("Program sonlandırıldı")
    raise SystemExit()
menuSec = 0
while menuSec != 8:
    print("MENU")
    print( ' 1-)Tum sutunlarin hesaplanan degerleri \n '
           '2-)Aykiri deger bulma \n '
           '3-)Frekans-Histogram grafigi\n '
           '4-)Tum niteliklerin kutu grafigi \n '
           '5-)Sutuna gore kutu grafigi \n '
           '6-)Mod bulma \n '
           '7-)Standart Sapma ve Varyans degeri \n '
           '8-)Cikis \n ')
    menuSec = int(input("Menuden Seciminiz: "))
    if menuSec == 1:
        print("---ORTALAMA-STANDART SAPMA-MİN-MAX DEGERLER-YUZDELİK DILIMLER--------------------------")
        aralik = bf.describe()
        print(aralik)
    elif menuSec == 2:
        Q1 = bf.n3.quantile(0.25)
        Q3 = bf.n3.quantile(0.75)
        IQR = Q3 - Q1
        yuksekDeger = Q3 + 1.5 * IQR
        alcakDeger = Q1 - 1.5 * IQR
        print('Olabilecek en kucuk deger')
        print(alcakDeger)
        print('Olabilecek en buyuk deger')
        print(yuksekDeger)
        i = 0
        while (i < 19):
            i = i + 1
            if (bf.n3[i] < alcakDeger):
                print('Aykiri deger bulundu')
                print(bf.n3[i])
            elif (bf.n3[i] > yuksekDeger):
                print('Aykiri deger bulundu')
                print(bf.n3[i])

    elif menuSec == 3:
        # grafik çizimi
        set = bf
        hisGr = set["n1"].plot.hist(orientation="horizontal")
        print(plt.show())

    elif menuSec == 4:
        # kutuGrafigi
        renk = {"boxes": "Red", "whiskers": "blue", "medians": "black", "caps": "green"}
        kutuGra = set.plot.box(color=renk)
        print(plt.show())

    elif menuSec == 5:
        bf['n33'].plot(kind='box')
        print(plt.show())

    elif menuSec == 6:
        dizi=[0,3,2,2,2,2,0,3,1,1,2,0,1,3,3,0,1,3,3,0]
        #tekStn = pd.read_table("veriSeti.TXT",usecols=["n1"],index_col="n1")
        #print(tekStn)
        #print(modAl("veriSeti.TXT",usecols=["n1"],index_col="n1"))
        #dizi.append(tekStn)
        #print(liste)
        print(modAl(dizi))
    elif menuSec == 7:
        dizi = [0, 3, 2, 2, 2, 2, 0, 3, 1, 1, 2, 0, 1, 3, 3, 0, 1, 3, 3, 0]
        print('Standart Sapma')
        print(standartSapmaBul(dizi))
        print('Varyans')
        print(varyansBul(dizi))

    elif menuSec == 8:
        cikis()

    else:
        print("1-8 arasında seçim yapınız!!")
