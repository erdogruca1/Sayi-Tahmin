print("Sayi Tahmin Oyununa Hosgeldiniz")

number = 32

playerNumbers = int(input("0 ile 50 arasinda bir sayi tahmin ediniz : "))

change = 5

while True:
    if change != 0:
        if playerNumbers > number:
            change -=  1
            print(change, "Hakkiniz kaldi ")
            playerNumbers = int(input("Daha kucuk bir sayi seciniz : "))
        elif playerNumbers < number:
            change -= 1
            print(change, "Hakkiniz kaldi ")
            playerNumbers = int(input("Daha buyuk bir sayi giriniz : "))

        if playerNumbers == number:
            print("Tebrikler oyunu kazandiniz !")
            break
    if change == 0:
        print("Oyunu kaybettiniz. Tekrar deneyiniz")
        break