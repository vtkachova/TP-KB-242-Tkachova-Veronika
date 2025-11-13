import random

options = ["stone", "scissor", "paper"]

user_choice = input("Введіть stone, scissor або paper: ")

print("Ваш вибір:", user_choice)

if user_choice not in options:
    print("Неправильний вибір!")
else:
    computer_choice = random.choice(options)
    print(f"Вибір комп'ютера: {computer_choice}")

    
    if user_choice == computer_choice:
        print("Нічия!")
    elif user_choice == "stone" and computer_choice == "scissor":
        print("Ви виграли! Камінь ламає ножиці.")
    elif user_choice == "scissor" and computer_choice == "paper":
        print("Ви виграли! Ножиці ріжуть папір.")
    elif user_choice == "paper" and computer_choice == "stone":
        print("Ви виграли! Папір накриває камінь.")
    else:
        print("Ви програли...")

