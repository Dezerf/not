with open("NOTES.txt.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)
author= input("Введи автора")
with open("NOTES.txt.txt", "a", encoding="UTF-8") as file:
    file.write(f"({author})\n")
while True:
    answer=input("Бажаєте додати цитату?(так/ні)")
    aswer=answer.lower()
    if answer == "так":
        quote=input("Введіть цитату")
        author= input("Введи автора")
        file=open("NOTES.txt.txt", "a", encoding="UTF-8")
        file.write(f"{quote}\n({author})\n")
        file.close()
    else:
        break
with open("NOTES.txt.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)
