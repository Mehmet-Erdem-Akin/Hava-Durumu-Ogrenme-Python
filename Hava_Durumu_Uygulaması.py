# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 02:19:35 2020

@author: mehmet
"""



import time
import webbrowser

while True:
    print("""
              ############################
              Kamil İle Güncel Hava Durumu
              ###########################
          """)
    
    
    print("""
          Merhaba Ben Mahallenin Çocuğu KAMİL
          Sana Hava Durumu Hakkında Bilgi Verebilirim
          Söyle Bakalım Neyi Merak Ediyorsun :) 
           """)
        
    print("""
          1 = İllere Göre Hava Durumu 
          2 = Türkiye Geneli Hava Durumu
          3 = Denize Açılabilecek Miyim ?
          """)
        
        
    cevap = input("Söyle Bakalım : ")
    if cevap == "1":
        sehir = input("Merak Ettiğin İli Baş Harfi Büyük Olacak Şekilde Yaz : ")
        time.sleep(1.5)
        webbrowser.open("https://www.mgm.gov.tr/?il={}".format(sehir))
        break
        
    elif cevap == "2":
        print("Türkiye Geneli Hava Durumu Açılıyor")
        time.sleep(1.5)
        webbrowser.open("https://www.mgm.gov.tr/tahmin/turkiye.aspx")
        break
     
    elif cevap == "3":
        print("Dur Hemen Açılma, Bakalım Bi !!!")
        time.sleep(1.5)
        webbrowser.open("https://www.mgm.gov.tr/deniz/24saatlik.aspx")
        break
        
     
    













