import requests
import random
import string
import time


time.sleep(2)
print("Генерирование нитро Discord")
time.sleep(0.3)


num = int(input('Сколько вы хотите сгенирировать и проверить нитро: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Ваше нитро генерируется,результаты в файле Nitro Code.txt")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Генерируется {num} кодов | Время: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" [+] Валидное | {nitro} ")
            break
        else:
            print(f" [-] Не валидное | {nitro} ")

input("\nВсё было сгенерировано,нажмите Enter,чтобы закрыть программу.")