import random

print("================================")
print("       🤖 БОЙОВІ РОБОТИ 🤖")
print("================================")

print()
print("Обери свого робота:")
print("1 - STEEL   ❤️ 100  ⚔️ 20")
print("2 - TITAN   ❤️ 130  ⚔️ 16")
print("3 - PHANTOM ❤️ 85   ⚔️ 28")

choice = input("Твій вибір: ")

if choice == "1":
    robot = "STEEL"
    hp = 100
    attack = 20

elif choice == "2":
    robot = "TITAN"
    hp = 130
    attack = 16

elif choice == "3":
    robot = "PHANTOM"
    hp = 85
    attack = 28

else:
    print("Неправильний вибір!")
    exit()

# Ворог
enemies = [
    ["SCRAP-X", 90, 15],
    ["DESTROYER", 110, 18],
    ["MEGA BOT", 140, 20],
    ["DARK MACHINE", 120, 23]
]

enemy = random.choice(enemies)

enemy_name = enemy[0]
enemy_hp = enemy[1]
enemy_attack = enemy[2]

energy = 100

print()
print("================================")
print("⚔️ БІЙ ПОЧИНАЄТЬСЯ!")
print("================================")
print()

print(robot, "VS", enemy_name)
print()

while hp > 0 and enemy_hp > 0:

    print("--------------------------------")
    print(robot, "❤️", hp, "⚡", energy)
    print(enemy_name, "❤️", enemy_hp)
    print("--------------------------------")

    print()
    print("1 - ⚔️ Атака")
    print("2 - 💥 Суперудар")
    print("3 - 🔧 Ремонт")
    print("4 - ⚡ Відновити енергію")

    action = input("Твоя дія: ")

    print()

    # Звичайна атака
    if action == "1":

        damage = random.randint(
            attack - 5,
            attack + 5
        )

        critical = random.randint(1, 100)

        if critical <= 15:
            damage = damage * 2
            print("🔥 КРИТИЧНИЙ УДАР!")

        enemy_hp = enemy_hp - damage

        print("⚔️ Ти завдав", damage, "шкоди!")

    # Суперудар
    elif action == "2":

        if energy >= 30:

            damage = random.randint(30, 50)

            enemy_hp = enemy_hp - damage
            energy = energy - 30

            print("💥 СУПЕРУДАР!")
            print("Ти завдав", damage, "шкоди!")

        else:
            print("❌ Недостатньо енергії!")

            continue

    # Ремонт
    elif action == "3":

        if energy >= 20:

            heal = random.randint(15, 30)

            hp = hp + heal
            energy = energy - 20

            print("🔧 Робота відремонтовано на", heal, "HP!")

        else:
            print("❌ Недостатньо енергії!")

            continue

    # Енергія
    elif action == "4":

        energy = energy + 30

        if energy > 100:
            energy = 100

        print("⚡ Енергію відновлено!")

    else:

        print("❌ Невідома команда!")
        continue

    # Перевірка перемоги
    if enemy_hp <= 0:
        break

    # Хід ворога
    print()
    print("👾 Хід ворога...")

    damage = random.randint(
        enemy_attack - 5,
        enemy_attack + 5
    )

    hp = hp - damage

    print(
        "👾",
        enemy_name,
        "завдав тобі",
        damage,
        "шкоди!"
    )

    # Відновлення енергії
    energy = energy + 10

    if energy > 100:
        energy = 100

    print()

# Кінець гри

print()
print("================================")

if hp <= 0:
    print("💀 ТИ ПРОГРАВ!")
    print("Твого робота знищено!")

else:
    print("🏆 ТИ ПЕРЕМІГ!")
    print("🤖", robot, "знищив", enemy_name)

print("================================")
print()
print("Дякую за гру! 🤖")
