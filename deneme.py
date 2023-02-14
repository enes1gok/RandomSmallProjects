"""
while True:
    try:
        soru1 = input("->Evet / ->Hayır ").lower()
    except:
        print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
        continue
    
    if soru1 == "evet" or soru1 == "hayır":
        break
    else:
        print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
        continue

file = open("deneme.txt", "a+")
file.write("Enes ADAMDIR\n")
file.close()
"""


numbers = ["0","1","2","3","4","5","6","7","8","9"]

"""
while True:
    z = 0
    isim = input("isim: ").lower()
    for i in isim:
        if i in harfler:
            z+=1
            continue
        else:
            break
    if z == len(isim):
        break
"""
try:
    soru1 = input("Telefonda mesajlaşma uygulamalarını müzik uygulamalarından daha az kullanırım.\n( ->Evet / ->Hayır ): ").lower()
    
    if soru1 == "hayir":
        soru1 = "hayır"
    print(soru1)
except:
    print("~~~~Lütfen evet veya hayır cevabını giriniz.~~~~")
"""
a = "ISTANBUL".lower()
a[0] = "ı"
"""