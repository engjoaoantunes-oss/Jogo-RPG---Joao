import random

#criando classes de objetos

class Personagem:
    def __init__(self, name, attack_power, defense, life,):
        self.name = name
        self.attack_power = attack_power
        self.defense = defense
        self.life = life
        self.max_life = life
    
    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.life = max(0, target.life - damage)
        print(f"{self.name} ataca {target.name} e causa {damage} de dano. {target.name} agora tem {target.life} de vida.")
    
    def heal(self):
        amount = 10
        # Aumenta a vida, mas garante que não ultrapasse a vida máxima
        self.life = min(self.life + amount, self.max_life)
        print(f"{self.name} curou {amount} pontos de vida! Vida atual: {self.life}")

    def super_attack(self, target):
        lista_aleatoria = [random.randint(1, 10) for _ in range(3)]
        numero_alvo = random.randint(1, 10)
        if numero_alvo in lista_aleatoria:
            damage = int(self.attack_power * 1.4)
            target.life = max(0, target.life - damage)
            print(f"{self.name} conseguiu buffar o ataque em {target.name} e causa {damage} de dano. {target.name} agora tem {target.life} de vida.")
        else:
            print("O ataque falhou!")

class Guerreiro(Personagem):
    def __init__(self, name):
        super().__init__(name, attack_power=18, defense=15, life=120)
        
class Mago(Personagem):
    def __init__(self, name):
        super().__init__(name, attack_power=25, defense=5, life=90)
    
class Arqueiro(Personagem):
    def __init__(self, name):
        super().__init__(name, attack_power=22, defense=10, life=100)
    





