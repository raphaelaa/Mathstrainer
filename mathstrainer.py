import random
import time

titles = ["Baby", "Crawlers", "Kindergarten child","elementary student","College student","High school student","Student","Professor","Super genius" ]

rank = 0

points=0
while True:
    print("You have {} points".format(points))
    # ---- Genie-Beförderung -----
    if points > 2:
        rank = 1  
    if points > 4:
        rank = 2
    if points > 6:
        rank = 3
    if points > 8:
        rank = 4
    if points > 10:
        rank = 5
    if points > 12:
        rank = 6
    if points > 14:
        rank = 7
    if points > 20:
        rank = 8
        
    if points > 100:
        print("You are too good for this game")
        break     
    
    
    
    # ---- neue Aufgabe ausdenke -----
    x=random.randint(-50,10)
    y=random.randint(1,10)
    op = random.choice(("*", "+","-","/"))
    if op == "/":
        z = x * y
        print("What is the result for {} {} {} ?".format(z, op, x))
    else:
        print("What is the result for {} {} {} ?".format(x, op, y))
    now1 = time.time()
    e1=input("Go on you {}, show what you can do >>>".format(titles[rank]))
    now2 = time.time()
    duration = now2-now1
    if e1=="End":
        break
    try:
        e2 = int(e1) # versuche eine zahl aus der eingabe zu machen
    except:
        print("really???.... a number from -1000 to 1000 please")
        continue # am Anfang der while schleife weitermachen
    if op == "*":
        if e2 == x * y:
            print("Multiplication is correct, very good.")
            print("You have needed {:.3f} seconds".format(duration))
            if duration < 2:
                points += 10
            elif duration < 10:
                points += 5
            else:
                points += 3
        else:
            print("false. The correct answer would be {}".format(x*y))
            points -= 1
    if op == "+":
        if e2 == x + y:
            print("Addition correct, very good")
            print("You have needed {:.3f} seconds".format(duration))
            if duration < 2:
                points +=5
            elif duration < 10:
                points += 3
            else:
                points +=1
        else:
            print("false. The correct answer would be {}".format(x+y)) 
            points -= 2
    if op == "-":
        if e2 == x - y:
            print("correct,very good")
            print("You have needed{:.3f}seconds".format(duration))
            if duration < 2:
                points += 5
            elif duration < 10:
                points += 3
            else:
                points += 1
        else:
            print("false. The correct answer would be {}".format(x-y))
            points -= 1
    if op == "/":
        if e2 == y:
            print("super,division correkt")
            print("You have needed {:.3f} seconds".format(duration))
            if duration < 2:
                points += 10
            elif duration < 10:
                points += 5
            else:
                points += 3
        else:
            print("false. The correct answer would be {}".format(x/y))
            points -= 1
             
print("Game over")

