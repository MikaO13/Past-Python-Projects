strengths_and_weaknesses = {
  #Type (attacker pokemon): [[strengths list (*2 dam)], [weaknesses list (*.5 dam)],  [resistant list (*1.5 dam)], [vulnerable list (*.75 dam)]]
  "Normal": [[], ["Rock", "Ghost", "Steel"], ["Ghost"], ["Fighting"]],
  "Fighting": [["Normal", "Rock", "Steel", "Ice", "Dark"], ["Flying", "Poison", "Psychic", "Bug", "Ghost", "Fairy"], ["Rock", "Bug", "Dark"], ["Flying", "Psychic", "Fairy"]],
  "Flying": [["Fighting", "Bug", "Grass"], ["Rock", "Steel", "Electric"], ["Fighting", "Ground", "Bug","Grass"], ["Rock", "Electric", "Ice"]],
  "Poison": [['Grass', 'Fairy'], ["Poison", 'Ground', 'Rock', 'Ghost', 'Steel'], ['Fighting', 'Poison', 'Grass', 'Fairy'], ['Ground', 'Psychic']],
  "Ground": [['Poison', 'Rock', 'Steel', 'Fire', 'Electric'], ['Flying', 'Bug', 'Grass'], ['Poison', "rock", 'Electric'], ['Water', 'Grass', 'Ice']],
  "Rock": [['Flying','Bug', 'Fire', 'Ice'], ['Fighting', 'Ground', 'Steel'], ['Normal', 'Flying', 'Poison', 'Fire'], ['Fighting', 'Ground', 'Steel', 'Water', 'Grass']],
  "Bug": [['Grass', 'Psychic', 'Dark'], ['Fighting', 'Flying', 'Poison', 'Ghost', 'Steel', 'Fire', 'Fairy'], ['Fighting', 'Ground', 'Grass'], ['Flying', 'Rock', 'Fire']],
  "Ghost": [['Ghost', 'Psychic'], ['Normal', 'Dark'], ['Normal', 'Fighting', 'Bug', 'Poison'], ['Ghost', 'Dark']],
  "Steel": [['Rock', 'Ice', 'Fairy'], ["Steel", 'Fire', 'Water', 'Electric'], ["Normal", "Flying", "Poison", "Rock", "Bug", "Steel", "Grass", "Psychic", "Ice", "Dragon", "Fairy"], ['Fighting', 'Ground', 'Fire']],
  "Fire": [['Bug', 'Steel', 'Grass', 'Ice'], ["Rock", "Fire", "Water", "Dragon"], ["Bug", "Steel", "Fire", "Grass", "Ice"], ["Ground", "Rock", "Water"]],
  "Water": [["Ground", "Rock", "Fire"], ["Water", "Grass", "Dragon"], ["Steel", "Fire", "Water", "Ice"], ['Grass', 'Electric']],
  "Grass": [["Ground", "Rock", 'Water'], ["Flying", "Poison", "Bug", "Steel", "Fire", "Grass", "Dragon"], ["Ground", "Water", "Grass", "Electric"], ["Flying", "Poison", "Bug", "Fire", "Ice"]],
  "Electric": [["Flying", "Water"], ["Ground", "Grass", "Electric", "Dragon"], ["Flying", "Steel", "Electric"], ["Ground"]],
  "Psychic": [["Fighting", "Poison"], ["Steel", "Psychic", "Dark"], ["Fighting", "Psychic"], ["Bug", "Ghost", "Dark"]],
  "Ice": [["Flying", "Ground", "Grass", "Dragon"], ["Steel", "Fire", "Water", "Ice"], ["Ice"], ["Fighting", "Rock", "Steel", "Fire"]],
  "Dragon": [["Dragon"], ["Steel", "Fairy"], ["Fire", "Water", "Grass", "Electric"], ["Ice", "Dragon", "Fairy"]],
  "Fairy": [["Fighting", "Dragon", "Dark"], ["Poison", "Steel", "Fire"], ["Fighting", "Bug", "Dragon", "Dark"], ["Poison", "Steel"]],
  "Dark": [["Ghost", "Psychic"], ["Fighting", "Dark", "Fairy"], ["Ghost", "Psychic", "Dark"], ["Fighting", "Bug", "Fairy"]]
}

class Pokemon:
  def __init__(self, name, level, health, maxhealth, typepokemon, isknockedout):
    self.name = name
    self.level = level
    self.health = health
    self.max_health = maxhealth
    self.type = typepokemon
    self.is_knocked_out = isknockedout
    
  def lose_health(self, amt):
    self.health -= health
    self.reveal_health()
    
  def gain_health(self, amt):
    self.health += health
    if self.health > self.max_health:
      self.health = self.max_health
    self.reveal_health()
  
  def knock_out(self):
    self.is_knocked_out == True
    print("{} is now knocked out with 0 health.".format(self.name))
  
  def revive(self):
    self.is_knocked_out == False
    print("{} is now revived with {} health.".format(self.name, self.health))
    
  def reveal_health(self):
    print("{} now has {} health.".format(self.name, self.health))
  
  def reveal_status(self):
    print("{} is a level {} {}, and now has {} health with max health {}.".format(self.name, str(self.level), self.type, str(self.health), str(self.max_health)))
    
  def attack(self, target):
    damage = self.level
    for attackerType in self.type:
      asaw = strengths_and_weaknesses[attackerType]
      for targetType in target.type:
        if targetType in asaw[0]:
          damage = damage * 2
        if targetType in asaw[1]:
          damage = damage // 2
        if targetType in asaw[2]:
          damage = damage * 3 // 2
        if targetType in asaw[3]:
          damage = damage * 3 // 4
    print("{} has attacked {} for {} damage.".format(self.name, target.name, damage))
    self.level += 1
    print("{} has leveled up to level {}.".format(self.name, str(self.level)))
    target.lose_health(damage)
    if self.health <= 0:
      target.knock_out()
      
class Trainer:
  def __init__(self, pokemons, name, potions):
    self.pokemons = pokemons
    self.name = name
    self.potions = potions
    self.current_pokemon = 0
  
  def print_pokemons(self):
    print("{}'s POKEMON LIST".format(self.name.upper()))
    for pokemon_num in range(self.current_pokemon, len(self.pokemons) + self.current_pokemon):
      self.pokemons[pokemon_num % len(self.pokemons)].reveal_status()
  
  def use_potion(self):
    current = self.pokemons[self.current_pokemon]
    print("{} used a potion on {} to gain 20 health.".format(self.name, current.name))
    current.gain_health(20)
  
  def attack(self, trainer):
    current = self.pokemons[self.current_pokemon]
    target = trainer.pokemons[trainer.current_pokemon]
    current.attack(target)
  
  def switch_active(self):
    not_in = True
    self.print_pokemons()
    while True:
      to_switch = input("What Pokemon would you like to switch to?  >>")
      for pokemon in self.pokemons:
        if pokemon.name.lower() == to_switch.lower():
          if pokemon.is_knocked_out == False:
            not_in = False
            to_switch_num = index.self.pokemons(pokemon)
          else:
            print("You cannot switch to {}, they are knocked out.".format(pokemon.name))
      if not_in == False:
        break
    self.current_pokemon = to_switch_num
    print("{} has switched their active pokemon to {}.".format(self.name, self.pokemons[self.current_pokemon].name))
        
    
  
    