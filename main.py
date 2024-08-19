import random

def rock_papert_scissors_arif_sahin():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Oyun kuralları:")
    print("Taş, kağıdı yener.")
    print("Kağıt, makası yener.")
    print("Makas, taşı yener.")
    print("İlk iki turu kazanan oyunu kazanır.")

    

    choice_list = ['taş', 'kağıt', 'makas']

    # sayaçlar
    played_game = 1

    while True:
        
        player_win = 0
        computer_win = 0
        played_round = 0

        print(f"{played_game}. oyun başladı!\n")

        while player_win < 2 and computer_win < 2:
            played_round += 1
            print(f"{played_game}. oyun {played_round}. tur")

            player_choice = input("Taş, Kağıt, Makas seçin (veya çıkmak için 'exit' yazınız): ").lower()

            if player_choice == 'exit':
                if played_game == 1 and played_round == 1:
                    print("Oyuna başlamadan vazgeçilir mi? Ayıp oldu ama.")
                print("Oyun bitti. Çıkış yapılıyor...")
                return

            if player_choice not in choice_list:
                print("Geçersiz bir seçim yaptınız, lütfen tekrar deneyin.")
                played_round -= 1
                continue

            computer_choice = random.choice(choice_list)
            print(f"Bilgisayarın seçimi: {computer_choice}")

            if player_choice == computer_choice:
                print("Berabere!\n")
            elif player_choice == 'taş' and computer_choice == 'makas':
                print("Şanslısın bu turu sen kazandın")
                player_win += 1
            elif player_choice == 'makas' and computer_choice == 'kağıt':
                print("Şanslısın sen kazandın!")
                player_win +=1
            elif player_choice == 'kağıt' and computer_choice == 'taş':
                print("Sen kazandın!!")
                player_win += 1
            else:
                print("Bu turu ben kazandım, öğrende gel!\n")
                computer_win += 1

            print(f"Skor: Oyuncu {player_win} - Bilgisayar {computer_win}\n")

        if player_win == 2:
            print(f"Tebrikler, {played_game}. oyunu kazandınız!")
        else:
            print(f"{played_game}. oyunu bilgisayar kazandı.")

        
        c_list = ['e', 'h']

        while True:
            another_game = input("Başka bir oyun oynamak ister misiniz? (Evet için 'e', Hayır için 'h'): ").lower()
            if another_game in c_list:
                break
            else:
                print("Lütfen geçerli bir seçim yapın: 'e' veya 'h'")
            
        c_another_game = random.choice(c_list)
        if another_game == 'e' and c_another_game == 'e':
            print("Yeni oyuna başlıyoruz.")
            played_game += 1
        elif another_game == 'e' and c_another_game == 'h':
            print("Benden bu kadar, daha sonra tekrar oynayalım")
            break
        else:
            print("Tekrar görüşmek üzere")
            

# Fonksiyonu çağırarak oyunu başlatabilirsiniz
rock_papert_scissors_arif_sahin()
