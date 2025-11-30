# Explicit imports: evita poluir o namespace
from functions import greetings, register_player, choose_class, battle, clear_screen


# 1. Mensagem de boas-vindas
greetings()

# 2. Registrar jogadores
j1_name, j2_name = register_player()
clear_screen()

# 3. Escolha de classes
print(f"\n{j1_name}, é a sua vez de escolher sua classe!")
personagem_1 = choose_class(j1_name)
clear_screen()

print(f"\n{j2_name}, é a sua vez de escolher sua classe!")
personagem_2 = choose_class(j2_name)
clear_screen()

# 4. Confirmação de nomes e classes.
print(f"\n{personagem_1.name} escolheu a classe {personagem_1.__class__.__name__}.")
print(f"{personagem_2.name} escolheu a classe {personagem_2.__class__.__name__}.")

# 5. Iniciar jogo
battle(personagem_1, personagem_2)






