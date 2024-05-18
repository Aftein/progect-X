from random import randint
from time import sleep
from data import player, enemies, shop

def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            enemy_hp -= player['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')


def display_player():
    print(f"игрок - {player['name']}")
    print(f"сила атаки - {player['attack']}")
    print(f"броня - {player['armor']}")
    print(f"хп - {player['hp']}")
    print(f"деньги - {player['money']}")
    print()


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f"враг - {enemy['name']}")
    print(f"сила атаки - {enemy['attack']}")
    print(f"броня - {enemy['hp']}")
    print()

def training(training_type):
    for i in range(0, 101, 20):
        print(f"тренеровка завершена на {i}%")
        sleep(1)
    if training_type == 0:
        player['armor'] -= 0.05
        print(f"тренеровка окончена: теперь ваша броня поглощает {(1-player['armor'])*100}%")
    elif training_type == 1:
        player['attack'] += 2
        print(f"тренеровка окончена: теперь ваша атака: {player['attack']}")


def display_inventory():
    if len(player['inventory']) == 0:
        print("инвентарь пуст")
    else:
        for item in player["inventory"]:
            print(item['name'])
            if 'attack' in item.keys():
                print(f"бонус к урону: {item['attack']}")
            if 'armor' in item.keys():
                print(f"бонус к броне: {item['armor']}")
            if 'hp' in item.keys():
                print(f"бонус к здоровью: {item['hp']}")
            print( "однорозовае использование" if item['single_time_use'] else "можно экипировать")
        user_choise = input(" хотитe что-то использовать?(да\ нет)")
        if user_choise == "да":
            user_choise = int(input("введите номер предмета(1, 2, 3, 4, 5, 6)"))
            if user_choise > len(player['inventory']):
                user_choise = len(player['inventory']) 
            if user_choise < 1:
                user_choise = 1
            user_choise -= 1
            print(player['inventory'][user_choise])
            if "attack" in player['inventory'][user_choise]:
                player['attack'] += player['inventory'][user_choise]['attack']
            if "armor" in player['inventory'][user_choise]:
                player['armor'] += player['inventory'][user_choise]['armor']
            if "hp" in player['inventory'][user_choise]:
                player['hp'] += player['inventory'][user_choise]['hp']
            if player['inventory'][user_choise]['single_time_use']:
                del player['inventory'][user_choise]

def display_shop():
    for item in shop:
        print(item['name'])
        if 'attack' in item.keys():
            print(f"бонус к урону: {item['attack']}")
        if 'armor' in item.keys():
            print(f"бонус к броне: {item['armor']}")
        if 'hp' in item.keys():
            print(f"бонус к здоровью: {item['hp']}")
        print( "однорозовае использование" if item['single_time_use'] else "можно экипировать")
        print( f"Цена: {item['price']}")
    user_choise = input(" хотитe что-то купить?(да\ нет)")
    if user_choise == "да":
        user_choise = int(input("введите номер предмета(1, 2, 3, 4, 5, 6)"))
        if user_choise > len(shop):
           user_choise = len(shop) 
        if user_choise < 1:
            user_choise = 1
        user_choise -= 1
        if shop[user_choise]['price'] < player['money']:
            player['money'] -= shop[user_choise]['price']
            player['inventory'].append(shop[user_choise])
        else:
            "недостаточно? Вернись когда будешь побогаче"    

def display_work():
    choice = input("выберите работу: 1, 2, 3")
    if choice == "1":
        print("вы пошли к старому леснику,вам сказали нарубить дров. Вы согласились и сделали работу, за это вам вручили 500 шекелей")
        player['money'] += 500
    elif choice == "2": 
        print("вы пошли на ферму. Вам дали задание собрать урожай. Вы усердно трудились и получили целых 1000 шекелей! Вот это улов!")
        player['money'] += 1000
    elif choice =="3":
        print("вы зашли в таверну.Ваша боевая форма тут...никого не пугает? Ну вот и хорошо!Вы спокойно отработали поваром и получили 1500 шекелей!")
        player['money'] += 1500