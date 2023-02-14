dicti = {}
sayı_list = ["0","1","2","3","4","5","6","7","8","9"]
sayılar2 = ["1", "2", "3","4","5","6"]
sayılar1 = ["1", "2", "3","4","5","6","7"]
kurs_isimler = ["YÜZME","FİTNESS","YOGA","TEKVANDO","JUDO","BOKS","PİLATES"]
ID = 100
id_liste = []
kurs_dicti = {
    '1000' : 'Yüzme',
    '1010' : 'Fitness',
    '1020' : 'Yoga',
    '1030' : 'Tekvando',
    '1040' : 'Judo',
    '1050' : 'Boks',
    '1060' : 'Pilates'
}


def Kursiyer_Ekle():
    liste = []
    global ID
    z = 0
    id_liste.append(ID)
    while True:   
        ad = input("Ad :")
        for i in ad:
            
            if i in sayı_list:
                print("Lütfen harf giriniz.")
                break
            else:
                z += 1
                continue
        if z == len(ad):
            z=0
            break
        

    liste.append(ad)

    
    while True:   
        soyad = input("Soyad :")
        for i in soyad:
            
            if i in sayı_list:
                print("Lütfen harf giriniz.")
                break
            else:
                z += 1
                continue
        if z == len(soyad):
            z=0
            break
        
    liste.append(soyad)

    
    while True:   
        yas = input("Yaş : ")
        for i in yas:
            
            if i not in sayı_list:
                print("Lütfen sayı giriniz.")
                break
            else:
                z += 1
                continue
        if z == len(yas):
            z=0
            break


    liste.append(yas)

    while True:        
        z = 0
        
        while True:    
            soru = input("Kaç tane kursa kayıt olmak istiyorsunuz?: ")    
                       
            if soru not in sayılar1:
                print("Lütfen geçerli bir rakam giriniz.")
                continue  
            else:
                break
                      
        liste.append(soru)
        soru = int(soru)
        print("KURS ID          KURS ADI")              #id ve adları birleştir
        print("________         _________")   
        print("1000             Yüzme")
        print("1010             Fitness")      
        print("1020             Yoga")
        print("1030             Tekvando")
        print("1040             Judo")
        print("1050             Boks")
        print("1060             Pilates")
        print(" ")

        if soru == 1:
            while True:
                while True:
                    z = 0
                    a = input("Lütfen KursID giriniz: ")
                    if a in kurs_dicti:                    
                        break
                    else:
                        print("Lütfen geçerli bir ID giriniz.")
                        continue
                    break


                b = input("Lütfen KursAd giriniz: ")
                if kurs_dicti[a].upper() == b.upper():
                    liste.append(a)
                    liste.append(b)
                    break
                else:
                    print("Kurs ID ve isim değerleri uyuşmamaktadır.")

            soru -= 1  
            break
        else: 
            while soru != 0:
                while True:            
                    while True:   
                        a = input("Lütfen KursID giriniz: ")
                        for i in a:
                            
                            if i not in sayı_list:
                                print("Lütfen sayı giriniz.")
                                break
                            else:
                                z += 1
                                continue
                        if z == len(a):
                            z=0
                            break
                    while True:    
                        b = input("Lütfen KursAd giriniz: ")
                        if b.upper() in kurs_isimler:
                            break
                    if kurs_dicti[a].upper() == b.upper():
                        liste.append(a)
                        liste.append(b)
                        break
                    else:
                        print("Kurs ID ve isim değerleri uyuşmamaktadır.")
                        
                soru -= 1

        if soru == 0:
            break     

    dicti[ID] = liste
    ID += 1
        
    return dicti

while True:
    print("1-Kursiyer Ekle")
    print("2-Kursiyerleri Listele")
    print("3-Kursiyer Ara")
    print("4-Kursiyer Sil")
    print("5-Kursiyer Ücret Hesapla")
    print("6-Çıkış")
    while True:
        x = input("1-6 : ")    
        if x in sayılar2:
            break
            
        else:
            print("Lütfen geçerli bir rakam giriniz.")
    x = int(x)
    if x == 1:
        print(Kursiyer_Ekle())
    elif x == 2:
        print(dicti)
    elif x == 3: 
        
        while True:
            k = input("Aranan ID: ")
            z = 0    
            for i in k: 
                if i not in sayı_list:
                    print("Lütfen sayı giriniz.")
                    break
                else:
                    z += 1
                    continue
            if k not in id_liste:
                pass
            if z == len(k):
                z=0
                break
        l = 0
        for i in id_liste:
            k = int(k)
            if i == k:
                m = id_liste.index(k)
                print(dicti[id_liste[m]])
                l+=1
            else:
                continue
        if l == 1:
            pass
        elif l == 0:
            print("Aradığınız kullanıcı bulunamadı.")

    elif x == 4:
        
        while True:   
            z = 0
            v = input("Hangi kursiyeri silmek istiyorsunuz?(ID giriniz): ")

            if int(v) not in id_liste:
                print("Lütfen geçerli bir ID giriniz.")
            else:
                break
        dicti.pop(int(v))

    elif x == 5:    
        
        while True:   
            z = 0
            u = input(" Borcunu Hesaplamak İstediğiniz Kişi'nin ID'sini giriniz: ")  

            if int(u) not in id_liste:
                print("Lütfen geçerli bir ID giriniz.")
            else:
                break
        
        t = dicti[int(u)][3]
        t = int(t)
        
        if t == 1:
            ucret = 100
            print("Tek kurs alımında kampanya bulunmamaktadır. ")
            print(f"Borcunuz {ucret} liradır. ")
        elif t == 2:
            ucret = 100 + 100 - 100*15/100
            print("İki kurs alımında ikinci kursta %15 indirim bulunmaktadır. ")
            print(f"Borcunuz {ucret} liradır. ")
        elif t == 3:
            ucret = 100 + 100 + 100 - 100*25/100
            print("Üç kurs alımında üçüncü kursta %25 indirim bulunmaktadır. ")
            print(f"Borcunuz {ucret} liradır. ")
        elif t >= 4:
            ucret = (100 - 100*10/100) * int(t)
            print("Üç kurstan fazla alan kişilere her kurstan %10 indirim bulunmaktadır. ")
            print(f"Borcunuz {ucret} liradır. ")       
            
    elif x == 6:
        break
