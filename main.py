print('''






                                ,-.
                               ("O_)
                              / `-/
                             /-. /
                            /   )
                           /   /  
              _           /-. /
             (_)"-._     /   )
               "-._ "-'""( )/    
                   "-/"-._" `. 
                    /     "-.'._
                   /\       /-._"-._
    _,---...__    /  ) _,-"/    "-(_)
___<__(|) _   ""-/  / /   /
 '  `----' ""-.   \/ /   /
               )  ] /   /
       ____..-'   //   /                       )
   ,-""      __.,'/   /   ___                 /,
  /    ,--""/  / /   /,-""   """-.          ,'/
 [    (    /  / /   /  ,.---,_   `._   _,-','
  \    `-./  / /   /  /       `-._  """ ,-'
   `-._  /  / /   /_,'            ""--"
       "/  / /   /"         
       /  / /   /
      /  / /   /  
     /  |,'   /  
    :   /    /  MEGA OYUN 2000 İFTİHARLA SUNAR:
    [  /   ,'                            Hazine Adası 
                                         Bu Bir Meriç Cebeci Projesidir.
    | /  ,'
    |/,-'
    P'

''')

print("Hazine Adasına HoşGeldiniz.")
print('Amacınız Hazineyi Bulmak Ve Hayatta Kalmak. Hazırsanız Başlayalım...')

secim1 = input('Bir\'Yol Ayrımına Geldiniz Ne Tarafa Gitmek İstersiniz "sağ" Yada "sol".').lower()
if secim1 == "sol":
    secim2 = input('Bir\'Göle Vardınız Ne Yapmak İstersiniz "yürü" Yada "yüz"').lower()
    if secim2 == "yürü":
        secim3 = input(
            'Yürüdünüz Bir De Baktınız Karşınızda  Üç Kapısı Olan Bir Ev Var. Eve Vardınız Hangi Kapıyı Seçeceksiniz "Kırmızı" "Mavi" "Yeşil"').lower()
        if secim3 == "kırmızı":
            print(
                "Kırmızı Kapıyı Açtınız Ve Oda Birden Alevler İçinde Kaldı Ve Tahmin Edin Ne Oldu? Tabiki Öldünüz Daha Ne Olsun.")
        elif secim3 == "yeşil":
            print("Yeşil Kapıyı Açtınız Ve Uzayın Sonsuz Boşluğu İçinde Kaybulup Gittiniz Ve Öldünüz.")
        elif secim3 == "mavi":
            print("Mavi Kapıyı Açtınız Ve Hazineyi Buldunuz Tebrikler. Ve Hayatta Kaldınız.")
    else:
        print("Yüzmek İçin Göle Girdiniz Ve dev Bir Alabalık Tarafından Saldırya Uğradınız Ve Öldünüz.")
else:
    print("Yanlış Yol Seçtiniz Ve Kafanıza Bir Kaya Düştü ve Oyun Bitti.")

