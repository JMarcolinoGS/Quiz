print("Seja muito Bem Vindo ao quiz do Marc!")
answer_user = input("Você quer começar? (S/N)")

if answer_user != "S":
    quit()

score = 0

print("começando...")
print("Quem desenvolveu o jogo Grand Teft Auto (GTA)?\n (A) RockstarGames \n (B) Ubisoft \n (C) Gameloft \n (D) TheSociet \n" )
answer_user = input("Resposta:")

if answer_user == A:
    print("Parabens voce acertou?")
    score = score + 1
else:
    print(" Voce errou")

    print("Quem é o protagonista do jogo God of War Ascension ?\n (A) Kratos \n (B) Kleiton \n (C) Prometheus \n (D) Atreus \n" )
answer_user = input("Resposta:")

if answer_user == A:
    print("Parabens voce acertou?")
    score = score + 1
else:
    print(" Voce errou")
    
    print("Quem é o protagonista da seríe The Last of Us?\n (A) Ellie \n (B) Abby \n (C) Sara \n (D) Joel \n" )
answer_user = input("Resposta:")

if answer_user == D:
    print("Parabens voce acertou?")
    score = score + 1
else:
    print(" Voce errou")

print(f"Acabou o jogo.....Pontuação: {score}/3")




