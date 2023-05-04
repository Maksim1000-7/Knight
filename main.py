import random
import time


# Класс игрока
class Player:
    # Конструктор класса
    def __init__(self, name, hp, damage, class_player, genius_player):
        self.name = name
        self.class_player = class_player
        self.genius = genius_player
        self.hp = hp
        self.damage = damage
        self.lvl = 1
        self.exp = 0


def create_person(name, class_type, genius_type):
    hp = 0
    damage = 0
    if class_type == class_list[0]:
        hp += 100
        damage += 99
    elif class_type == class_list[1]:
        hp += 174
        damage += 130

    else:
        print("Чтото пошло не так , такого класса нет")
        quit()
    if genius_type == genius_list[0]:
        hp += 49
        damage += 30
    elif genius_type == genius_list[1]:
        hp += 1000
        damage += 300
    elif genius_type == genius_list[2]:
        hp += 100
        damage += 9999999
    else:
        print("Чтото пошло не так , такого  рода нет")
        quit()
    return Player(name, hp, damage, class_type, genius_type)


class_list = ["лучник", "рыцарь"]
genius_list = ["эльф", "гном", "человек"]
choice_list = ["weapon", "heal"]
# Создаём список для хранения
# информации об персонаже
person = []

# Сохраняем имя
print("Введите имя: ")
person.append(input())


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


def create_monster():
    monsters_name=["скелет","вампир","оборотень"]
    rnd_name = random.choice(monsters_name)
    rnd_hp = random.randint(10, 20) + player.lvl * 10
    rnd_damage = random.randint(1, 5) + player.lvl * 2.5

    return Enemy(rnd_name, rnd_hp, rnd_damage)


# Сохраняем класс
print("Введите класс игрока. Доступные классы: ")
for x in class_list:
    print(x, end=' ')
print()
person.append(input().lower())

# Сохраняем род
print("Введите род игрока. Доступные рода: ")
for x in genius_list:
    print(x, end=' ')
print()
person.append(input().lower())

player = create_person(person[0],person[1],person[2])
# Очистка списка с информацией персонажа
# для создания новых
person.clear()

# print("Персонаж создан!")
# print(f"Главный герой -> {player.name} \n"
#       f"Класс -> {player.class_player} \n"
#       f"Род -> {player.genius} \n"
#       f"Здоровье -> {player.hp} \n"хх
#       f"Урон -> {player.damage} \n"
#       f"Уровень -> {player.lvl} \n"
#       f"Опыт -> {player.exp} \n")

while True:
    event=random.randint(0,1)
    if event==0:
        print("Вам никто не встретился,идем дальше")
        time.sleep(1)
    elif event == 1:
        enemy=create_monster()
        print(f"Вам вам попался {enemy.name} ")
        break