questions =[
    ["Which language was used to create Facebook?","Python","French","Javascript","Php","None",4],
    ["Which language was used to create Facebook?","Python","French","Javascript","Php","None",4],
    ["Who created Python?","Denis Ritchie","Guido van Rossum","James Gosling","Bjarne Stroustrup","None",2],
    ["Who created Python?","Denis Ritchie","Guido van Rossum","James Gosling","Bjarne Stroustrup","None",2],
    ["What does HTML stand for?","Hyper Text Markup Language","High Text Markup Language","Home Text Markup Language","Health Text Markup Language","None",1],
    ["What does HTML stand for?","Hyper Text Markup Language","High Text Markup Language","Home Text Markup Language","Health Text Markup Language","None",1],
    ["What does CSS stand for?","Cascading Style Sheets","Creative Style Sheets","Computer Style Sheets","Colorful Style Sheets","None",1],
]

levels = [1000,2000,3000,5000,10000,20000,30000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]

    print(f"\n Question for Rs. {levels[i]}\n")
    print(question[0])

    print(f"1. {question[1]}             2. {question[2]}")  
    print(f"3. {question[3]}             4. {question[4]}")

    reply = int(input("Enter your answer with the option numbers only"))

    if reply ==question[-1]:
        print(f"Correct answer! you have won Rs. {levels[i]}")

        money = levels[i]

        if i == 2:
            money = 3000

        elif i == 4:
            money = 10000

        elif i == 6:
            money = 30000

    else:
        print("Wrong answer! you have won nothing")
        break

print(f"You have won Rs. {money}")


