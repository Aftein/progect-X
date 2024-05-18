from random import randint
from time import sleep
from data import player,enemies
from helpers import fight, display_enemy, display_player, training, display_inventory, display_shop, display_work



name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0

while True:
    action = input('''Введите действие
 1 - В бой!
 2 - Показать информацию об игроке
 3 - Показать информацию о противнике
 4 - тренеровка 
 5 - инвентарь
 6 - магазин
 7 - работа 
ввод: ''')
    if action == "1":
        fight(current_enemy)
    elif action == "2":
        display_player()
    elif action == "3":
        display_enemy(current_enemy)
    elif action == "4":
        training_type = int(input("введите вид тренеровки:"))
        training(training_type)
    elif action == "5":
        display_inventory()
    elif action == "6":
        display_shop()
    elif action == "7":
        display_work()