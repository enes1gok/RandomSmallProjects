harfler = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]

while True:
    z = 0
    name = input("Lütfen adınızı giriniz: ").lower()
    for i in name:
        if i in harfler:
            z+=1
            continue
        else:
            print("~~~~GEÇERSİZ DEĞER!!! Lütfen string bir ifade giriniz.~~~~")
            break
    if z == len(name):
        break
while True:
    z = 0
    surname = input("Lütfen soyadınızı giriniz: ").lower()
    for i in surname:
        if i in harfler:
            z+=1
            continue
        else:
            print("~~~~GEÇERSİZ DEĞER!!! Lütfen string bir ifade giriniz.~~~~")
            break
    if z == len(surname):
        break


while True:
    try:
        gender = input("Lütfen cinsiyetinizi giriniz(K/E): ").lower()
    except:
        print("~~~~GEÇERSİZ DEĞER!!! Lütfen K veya E cevabını giriniz.~~~~")
        continue
    
    if gender == "k" or gender == "e":
        break
    else:
        print("~~~~GEÇERSİZ DEĞER!!! Lütfen K veya E cevabını giriniz.~~~~")
        continue

while True:
    try:
        age = int(input("Lütfen yaşınızı giriniz: "))
        break
    except:
        print("~~~~GEÇERSİZ DEĞER!!! Lütfen bir sayı  değeri giriniz.~~~~")
    
        





#dışa dönük / içe dönük 
#gerçekçi   / sezgisel  
#düşünen    / hassas    Büyük bir problemle karşılaştığımda yoğun bir moral bozukluğu yaşamak yerine hemen mantıklı bir çözüm ararım.
#sorgulayan / algıları açık Arkadaşlarımla tatile giderken her şeyi planlayıp yola çıkmak yerine, plansız, spontane bir şekilde yola çıkmak isterim.
while True:
    try:
        soru1 = input("Telefonda mesajlaşma uygulamalarını müzik uygulamalarından daha az kullanırım.\n( ->Evet / ->Hayır ): ").lower()
        if soru1 == "hayir":
            soru1 = "hayır"
    except:
        print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
        continue
    
    if soru1 == "evet" or soru1 == "hayır":
        break
    else:
        print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
        continue


if soru1 == "evet":
    while True:
        try:
            soru2 = input("Kötü geçen bir sınavdan çıkınca kendini kötü sonuca hazırlamak yerine, salladıklarımın tutma ihtimalini düşünürüm.\n( ->Evet / ->Hayır ): ").lower()
            if soru2 == "hayir":
                soru2 = "hayır"
        except:
            print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
            continue
        
        if soru2 == "evet" or soru2 == "hayır":
            break
        else:
            print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
            continue
    
    if soru2 == "evet":
        while True:
            try:
                soru4 = input("Büyük bir problemle karşılaştığımda yoğun bir moral bozukluğu yaşamak yerine hemen mantıklı bir çözüm ararım.\n( ->Evet / ->Hayır ): ").lower()
                if soru4 == "hayir":
                    soru4 = "hayır"
            except:
                print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                continue
            
            if soru4 == "evet" or soru4 == "hayır":
                break
            else:
                print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                continue
        
        if soru4 == "evet":
            while True:
                try:
                    soru8 = input("Arkadaşlarımla tatile giderken her şeyi planlayıp yola çıkmak yerine, plansız, spontane bir şekilde yola çıkmak isterim.\n( ->Evet / ->Hayır): ").lower()
                    if soru8 == "hayir":
                        soru8 = "hayır"
                except:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
                
                if soru8 == "evet" or soru8 == "hayır":
                    break
                else:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
            if soru8 == "evet":
                yournumber = "1"
                result = "**********Dışa dönük / Gerçekçi / Düşünen / Sorgulayan**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Enerjik\n-->>İletişimci\n-->>Çoklu görevleri seven\n-->>Multitasking'de başarılı\n\n\n___ÖRNEK MESLEKLER___:\n=>Avukat\n=>Eczacı\n=>Sigortacı ya da satış personeli\n=>Yargıç\n=>Proje yöneticisi"
            elif soru8 == "Hayır":
                yournumber = "2"
                result = "**********İçe dönük / Gerçekçi / Düşünen / Sorgulayan**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Çalışkan, sorumluluk sahibi\n-->>Kalabalık gruplardan hoşlanmayan\n-->>Vitrinde olmayı sevmeyen\n-->>Tek seferde bir işi yapmaktan hoşlanan\n\n\n___ÖRNEK MESLEKLER___:\n=>Denetçi\n=>Muhasebeci\n=>Finans yöneticisi\n=>Web geliştirme mühendisi\n=>Kamu çalışanı"
        
        elif soru4 == "hayır":
            while True:
                try:
                    soru9 = input("Arkadaşlarımla tatile giderken her şeyi planlayıp yola çıkmak yerine, plansız, spontane bir şekilde yola çıkmak isterim.\n( ->Evet / ->Hayır): ").lower()
                    if soru9 == "hayir":
                        soru9 = "hayır"    
                except:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
                
                if soru9 == "evet" or soru9 == "hayır":
                    break
                else:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
            if soru9 == "evet":
                yournumber = "3"
                result = "**********Dışa dönük / Gerçekçi / Hassas / Sorgulayan**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>İnsanlara yardım etmeyi seven\n-->>Sosyal rollerden hoşlanan\n-->>Geleneklerini önemseyen\n\n\n___ÖRNEK MESLEKLER___:\n=>Satış temsilcisi\n=>Hemşire, sağlık çalışanı\n=>Sosyal hizmet sorumlusu\n=>Halkla ilişkiler çalışanı\n=>Kredi yöneticisi"
            elif soru9 == "Hayır":
                yournumber = "4"
                result = "**********İçe dönük / Gerçekçi / Hassas / Sorgulayan**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Alçakgönüllü ve kararlı\n-->>İnsanlara yardım etmeyi seven\n-->>Otoriter pozisyonlardan pek hoşlanmayan\n\n\n___ÖRNEK MESLEKLER___:\n=>Diş hekimi\n=>İlköğretim öğretmeni\n=>Kütüphaneci\n=>Franchise işletmecisi\n=>Müşteri hizmetleri temsilcisi"
    elif soru2 == "hayır":
        
        while True:
            try:
                soru5 = input("Büyük bir problemle karşılaştığımda yoğun bir moral bozukluğu yaşamak yerine hemen mantıklı bir çözüm ararım.\n( ->Evet / ->Hayır ): ").lower()
                if soru5 == "hayir":
                    soru5 = "hayır"
            except:
                print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                continue
            
            if soru5 == "evet" or soru5 == "hayır":
                break
            else:
                print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                continue
        
        if soru5 == "evet":
            while True:
                try:
                    soru10 = input("Arkadaşlarımla tatile giderken her şeyi planlayıp yola çıkmak yerine, plansız, spontane bir şekilde yola çıkmak isterim.\n( ->Evet / ->Hayır): ").lower()
                    if soru10 == "hayir":
                        soru10 = "hayır" 
                except:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
                
                if soru10 == "evet" or soru10 == "hayır":
                    break
                else:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
            if soru10 == "evet":
                yournumber = "5"
                result = "**********Dışa dönük / Gerçekçi / Düşünen / Algıları açık***********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Pragmatist\n-->>Heyecanı ve kriz yönetimini seven\n-->>Zorlu ve karmaşık görevlerden hoşlanan\n\n\n___ÖRNEK MESLEKLER___:\n=>Dedektif\n=>Bankacı\n=>Yatırımcı\n=>Eğlence sektörü çalışanı\n=>Spor antrenörü"
            elif soru10 == "hayır":
                yournumber = "6"
                result = "**********İçe dönük / Gerçekçi / Düşünen / Algıları açık**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Açıksözlü, dürüst\n-->>Aksiyon almayı konuşmaya tercih eden\n-->>El ve motor becerileri gelişkin\n\n\n___ÖRNEK MESLEKLER___:\n=>İnşaat mühendisi\n=>Ekonomist\n=>Pilot\n=>Veri iletişim analisti\n=>Acil servis teknisyeni"
        
        elif soru5 == "hayır":
            while True:
                try:
                    soru11 = input("Arkadaşlarımla tatile giderken her şeyi planlayıp yola çıkmak yerine, plansız, spontane bir şekilde yola çıkmak isterim.\n( ->Evet / ->Hayır): ").lower()
                    if soru11 == "hayir":
                        soru11 = "hayır"
                except:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
                
                if soru11 == "evet" or soru11 == "hayır":
                    break
                else:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
            if soru11 == "evet":
                yournumber = "7"
                result = "**********Dışa dönük / Gerçekçi / Hassas / Algıları açık**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Hayat dolu, girişken, neşeli\n-->>Sağduyuyu önemseyen\n-->>Kendini ifade edebileceği pozisyonları seven\n-->>İletişimci\n\n\n___ÖRNEK MESLEKLER___:\n=>Çocuk bakım uzmanı\n=>Pratisyen hekim, aile hekimi\n=>Aktör\n=>İç mimar, dekoratör\n=>Çevre mühendisi"
            elif soru11 == "hayır":
                yournumber = "8"
                result = "**********İçe dönük / Gerçekçi / Hassas / Algıları açık**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Hassas, duyarlı, cana yakın\n-->>İnsanlara yardım etmeyi seven\n-->>Empati yeteneği kuvvetli\n\n\n___ÖRNEK MESLEKLER___:\n=>Moda tasarımcısı\n=>Fizik tedavi uzmanı\n=>Masaj terapisti\n=>Peyzaj mimarı\n=>Küçük işletme sahibi"






elif soru1 == "hayır":
    while True:
        try:
            soru3 = input("Kötü geçen bir sınavdan çıkınca kendini kötü sonuca hazırlamak yerine, salladıklarımın tutma ihtimalini düşünürüm.\n( ->Evet / ->Hayır ): ").lower()
            if soru3 == "hayir":
                soru3 = "hayır"
        except:
            print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
            continue
        
        if soru3 == "evet" or soru3 == "hayır":
            break
        else:
            print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
            continue
    
    if soru3 == "evet":
        while True:
            try:
                soru6 = input("Büyük bir problemle karşılaştığımda yoğun bir moral bozukluğu yaşamak yerine hemen mantıklı bir çözüm ararım.\n( ->Evet / ->Hayır ): ").lower()
                if soru6 == "hayir":
                    soru6 = "hayır"
            except:
                print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                continue
            
            if soru6 == "evet" or soru6 == "hayır":
                break
            else:
                print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                continue
        
        if soru6 == "evet":
            while True:
                try:
                    soru12 = input("Arkadaşlarımla tatile giderken her şeyi planlayıp yola çıkmak yerine, plansız, spontane bir şekilde yola çıkmak isterim.\n( ->Evet / ->Hayır): ").lower()
                    if soru12 == "hayir":
                        soru12 = "hayır"
                except:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
                
                if soru12 == "evet" or soru12 == "hayır":
                    break
                else:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
            if soru12 == "evet":
                yournumber = "9"
                result = "**********Dışa dönük / Sezgisel / Düşünen / Sorgulayan**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Mantıklı, analitik, stratejik\n-->>Doğuştan lider\n-->>Organize\n-->>Otoriter rolleri seven\n\n\n___ÖRNEK MESLEKLER___:\n=>Üst düzey yönetici\n=>Avukat\n=>Pazar araştırma analisti\n=>Yönetim danışmanı\n=>Yatırımcı"
            elif soru12 == "hayır":
                yournumber = "10"
                result = "**********İçe dönük / Sezgisel / Düşünen / Sorgulayan**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Yaratıcı, mükemmelliyetçi\n-->>İşleri kendi yöntemleriyle halletmeyi seven\n-->>Göz önünde rollerden hoşlanmayan\n\n\n___ÖRNEK MESLEKLER___:\n=>Yatırım bankacısı\n=>Kişisel finans danışmanı\n=>Yazılım geliştirici\n=>Ekonomist\n=>Yönetici"
        
        elif soru6 == "hayır":
            while True:
                try:
                    soru13 = input("Arkadaşlarımla tatile giderken her şeyi planlayıp yola çıkmak yerine, plansız, spontane bir şekilde yola çıkmak isterim.\n( ->Evet / ->Hayır): ").lower()
                    if soru13 == "hayir":
                        soru13 = "hayır"
                except:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
                
                if soru13 == "evet" or soru13 == "hayır":
                    break
                else:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
            if soru13 == "evet":
                yournumber = "11"
                result = "**********Dışa dönük / Sezgisel / Hassas / Sorgulayan**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>İnsan canlısı, enerjik\n-->>Diplomatik, iş birlikçi\n-->>Kendini ifade etmeyi seven\n-->Mantıklı\n\n\n___ÖRNEK MESLEKLER___:\n=>Reklam yöneticisi\n=>Halkla ilişkiler uzmanı\n=>Kurumsal koç / eğitmen\n=>Satış yöneticisi\n=>İşe alım uzmanı"
            elif soru13 == "hayır":
                yournumber = "12"
                result = "**********İçe dönük / Sezgisel / Hassas / Sorgulayan**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Düşünceli, yaratıcı\n-->>Kişisel prensiplerine bağlı\n-->>Bire bir iletişimde başarılı\n\n\n___ÖRNEK MESLEKLER___:\n=>Avukat\n=>Eczacı\n=>Sigortacı ya da satış personeli\n=>Yargıç\n=>Müşteri ilişkileri yöneticisi"
    elif soru3 == "hayır":
        
        while True:
            try:
                soru7 = input("Büyük bir problemle karşılaştığımda yoğun bir moral bozukluğu yaşamak yerine hemen mantıklı bir çözüm ararım.\n( ->Evet / ->Hayır ): ").lower()
                if soru7 == "hayir":
                    soru7 = "hayır"
            except:
                print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                continue
            
            if soru7 == "evet" or soru7 == "hayır":
                break
            else:
                print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                continue
        
        if soru7 == "evet":
            while True:
                try:
                    soru14 = input("Arkadaşlarımla tatile giderken her şeyi planlayıp yola çıkmak yerine, plansız, spontane bir şekilde yola çıkmak isterim.\n( ->Evet / ->Hayır): ").lower()
                    if soru14 == "hayir":
                        soru14 = "hayır" 
                except:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
                
                if soru14 == "evet" or soru14 == "hayır":
                    break
                else:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
            if soru14 == "evet":
                yournumber = "13"
                result = "**********Dışa dönük / Sezgisel / Düşünen / Algıları açık**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Yaratıcı, mücadeleci\n-->>Riskli rolleri seven\n-->>İstikrarlı\n-->>Kalıpların dışına çıkabilen\n\n\n___ÖRNEK MESLEKLER___:\n=>Girişimci\n=>Emlakçı\n=>Reklam yaratıcı sektörü\n=>Pazarlama direktörü\n=>Siyatsetçi / siyaset danışmanı"
            elif soru14 == "hayır":
                yournumber = "14"
                result = "**********İçe dönük / Sezgisel / Düşünen / Algıları açık**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Özgürlüğüne düşkün\n-->>Yaratıcı, problem çözücü\n-->>Dakik ve dikkatli\n\n\n___ÖRNEK MESLEKLER___:\n=>Bilgisayar programcısı\n=>Finans analisti\n=>Mimar\n=>Öğretim görevlisi\n=>Ekonomist"
        
        elif soru7 == "hayır":
            while True:
                try:
                    soru15 = input("Arkadaşlarımla tatile giderken her şeyi planlayıp yola çıkmak yerine, plansız, spontane bir şekilde yola çıkmak isterim.\n( ->Evet / ->Hayır): ").lower()
                    if soru15 == "hayir":
                        soru15 = "hayır"
                except:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
                
                if soru15 == "evet" or soru15 == "hayır":
                    break
                else:
                    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
                    continue
            if soru15 == "evet":
                yournumber = "15"
                result = "**********Dışa dönük / Sezgisel / Hassas / Algıları açık**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Meraklı, kendine güvenen\n-->>Olasılıkları değerlendiren\n-->>Kendini ifade edebilen\n-->>Açık ve iletişimci\n\n\n___ÖRNEK MESLEKLER___:\n=>Gazeteci\n=>Reklam yaratıcı direktörü\n=>Danışman\n=>Restoran işletmecisi\n=>Etkinlik organizetörü"
            elif soru15 == "hayır":
                yournumber = "16"
                result = "**********İçe dönük / Sezgisel / Hassas / Algıları açık**********\n___KİŞİSEL ÖZELLİKLER___:\n-->>Duyarlı, idealist\n-->>İç görü sahibi\n-->>Kişisel değerleri önemseyen\n-->>Şefkatli\n\n\n___ÖRNEK MESLEKLER___:\n=>Grafik tasarımcı\n=>Psikolog / terapist\n=>Yazar / editör\n=>Fizik tedavi uzmanı\n=>İnsan kaynakları eğitmeni"
print(result)
evaluation = input("Lütfen anket sonucunu 1 ile 10 puan arasında değerlendirebilir misiniz?: ")

file = open("sonuç.txt", "a+")
file.write("Isim: {}\nSoyisim: {}\nYas: {}\nCinsiyet: {}\nKisilik sonucunuz: {}\nAnkete verdiginiz puan: {}".format(name,surname,age,gender,yournumber,evaluation))
file.close()