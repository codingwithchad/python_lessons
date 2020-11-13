import random

hero_health = 100
hero_name = "Super Girl"
hero_hit = 0

monster_health = 50
monster_name = "The Joker"
monster_hit = 0

while hero_health > 0 and monster_health > 0:
    print(f'{hero_name} has {hero_health}hp')
    print(f'{monster_name} has {monster_health}hp')
    attack = input("Press any key to attack")

    hero_hit = random.randint(10, 20)
    monster_health -= hero_hit

    monster_hit = random.randint(2, 10)
    hero_health -= monster_hit

    print(f'{hero_name} hit {monster_name} and caused {hero_hit}hp damage')
    print(f'{monster_name} hit {hero_name} and caused {monster_hit}hp damage')
    print("\n")

print("------------------------")
if hero_health <= 0:
    print(f'{hero_name} has been defeated by {monster_name}')
elif monster_health <= 0:
    print(f'{hero_name}, you have overcome great odds and defeated {monster_name}')
else:
    print("There has been a mistake")
print("------------------------")


