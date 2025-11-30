from classes import Guerreiro, Mago, Arqueiro
import time
import os

#definindo funções do jogo
def clear_screen():
    os.system("cls")

def greetings():
    print("-"*50)
    print(f"{'BEM-VINDO AO MEU PRIMEIRO RPG':^50}")
    print("-"*50)
    
def register_player():
    player_1_name = input("Digite o nome do primeiro jogador: ")
    player_2_name = input("Digite o nome do segundo jogador: ")
    return player_1_name, player_2_name
   
def choose_class(player_name):
    while True:
        try:
            print("\nClasses disponíveis:")
            print("1 - Guerreiro")
            print("2 - Mago")
            print("3 - Arqueiro")
            
            escolha = int(input(f"{player_name}, escolha sua classe: "))
            
            if escolha == 1:   
                return Guerreiro(player_name)
            elif escolha == 2:
                return Mago(player_name)
            elif escolha == 3:
                return Arqueiro(player_name)
            else:
                print("Opção inválida! Escolha entre 1 e 3.")
        except ValueError:
            print("Entrada inválida! Digite um número entre 1 e 3.")
     
def battle(player1, player2):
    print("\nEstão prontos?")
    print("Iniciando a batalha em:")

    for i in range(5, 0, -1):
        time.sleep(1)
        print(i)
    
    # Lógica de turnos (O resto da função de batalha interativa)
    players = [player1, player2]
    round_count = 1

    while player1.life > 0 and player2.life > 0:
        for i, current_player in enumerate(players):
            target_player = players[1 - i]

            if target_player.life <= 0:
                break

            clear_screen()
            print(f"\n==== ROUND {round_count}, Vez de {current_player.name} ====")
            print(f"Vida de {current_player.name}: {current_player.life}")
            print(f"Vida de {target_player.name}: {target_player.life}")

            while True:
                try:
                    escolha = int(input("O que você quer fazer? (1: Atacar, 2: Curar, 3: Super Ataque (30% de chance de acerto): "))

                    if escolha == 1:
                        current_player.attack(target_player)

                        if target_player.life <= 0:
                            clear_screen()
                            print(f"{target_player.name} foi derrotado!")
                            print(f"🏆 {current_player.name} ({current_player.__class__.__name__}) venceu a batalha! 🏆")
                            return current_player

                        break

                    elif escolha == 2:
                        current_player.heal()
                        break

                    elif escolha == 3:
                        current_player.super_attack(target_player)

                        if target_player.life <= 0:
                            clear_screen()
                            print(f"{target_player.name} foi derrotado!")
                            print(f"🏆 {current_player.name} ({current_player.__class__.__name__}) venceu a batalha! 🏆")
                            return current_player
                        break

                    else:
                        print("Opção inválida! Escolha 1 ou 2 ou 3.")

                except ValueError:
                    print("Entrada inválida! Digite 1 ou 2.")

        round_count += 1