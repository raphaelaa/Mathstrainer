import random
import time
import easygui
#import subprocess

titles = ["Baby", "Crawlers", "Kindergarten child","elementary student","College student","High school student","Student","Professor","Super genius" ]
images = ["babybild400.gif",  "krablerbild400.gif",   "kindergartenkind400.gif",  "volkschulkind400.gif",  "unterstufenkind400.gif",  "oberstufenkind400.gif",  "student400.gif",   "proffesorbild400.gif",   "super genie400.gif"] 
rank = 0

very_good = ["smiley sehr gut.gif", "Smiley sehr gut.gif", "Smiley sehr gut 1.gif", "Smiley sehr gut 2.gif"]
good=["smiley gut.gif", "Smiley gut 2.gif", "Smiley gut 1.gif", "Smiley gut.gif"]
not_bad=["Smiley befriedigend.gif", "Smiley befriedigend1.gif", "Smiley befriedigend3.gif", "Smiley befriedigend 2.gif", "Smiley befriedigend 4.gif"]
bad=[ "smiley schlecht.gif", "Smiley schlecht1.gif", "Smiley schlecht 2.gif"]      

points=0
while True:
    status = "You have {} points".format(points)
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
        easygui.msgbox("You are too good for this game")
        break     
    
    
    
    # ---- neue Aufgabe ausdenke -----
    x=random.randint(-50,10)
    y=random.randint(1,10)
    op = random.choice(("*", "+","-","/"))
    if op == "/":
        z = x * y
        question = "What is the result for {} {} {} ?".format(z, op, x)
    else:
        question = "What is the result for {} {} {} ?".format(x, op, y)
    now1 = time.time()
    ###subprocess.Popen(("espeak", question))
    p = "Go on you {}, show what you can do >>>".format(titles[rank])
    e2 = easygui.integerbox(msg = question + "\n" + p, title= status, image = images[rank],
                            lowerbound=-500, upperbound = 500)
    if e2 is None:
        break
    #print(e2, type(e2))
    now2 = time.time()
    duration = now2-now1
    #if e1=="End":
    #    break
    #try:
    #    e2 = int(e1) # versuche eine zahl aus der eingabe zu machen
    #except:
    #    print("really???.... a number from -1000 to 1000 please")
    #    continue # am Anfang der while schleife weitermachen
    if op == "*":
        pic = None
        if e2 == x * y:
            status1 = "Multiplication is correct!"
            #status1 = status1 + "\n" + "You have needed {:.3f} seconds".format(duration)
            if duration < 2:
                points += 10
                pic = random.choice(very_good)
                status1 += "\n **** Very good ! ******"
            elif duration < 10:
                points += 5
                pic = random.choice(good)
                status1 += "\n **** Good ! ******"
                
            else:
                points += 3
                pic = random.choice(not_bad)
                status1 += "\n **** Not bad ! ******"
        else:
            status1 = "False. The correct answer would be {}".format(x*y)
            points -= 1
            pic = random.choice(bad)
            status1 += "\n **** Bad ! ******"
        #print(status1)
        status1 = status1 + "\n" + "You have needed {:.3f} seconds".format(duration)
        easygui.msgbox(status1, "you have now {} points".format(points), image=pic)
    if op == "+":
        pic = None
        if e2 == x + y:
            status1 ="Addition correct"
            #status1 = status1 + "\n" +"You have needed {:.3f} seconds".format(duration)
            if duration < 2:
                points +=5
                pic = random.choice(very_good)
                status1 += "\n **** Very good ! ******"
            elif duration < 10:
                points += 3
                pic = random.choice(good)
                status1 += "\n **** Good ! ******"
            else:
                points +=1
                pic = random.choice(not_bad)
                status1 += "\n **** Not bad ! ******"
        else:
            status1 ="false. The correct answer would be {}".format(x+y) 
            points -= 2
            pic = random.choice(bad)
            status1 += "\n **** Bad ! ******"
        status1 = status1 + "\n" + "You have needed {:.3f} seconds".format(duration)
        easygui.msgbox(status1, "you have now {} points".format(points), image=pic)  
    if op == "-":
        pic = None
        if e2 == x - y:
            status1 ="correct"
            #status1 = status1 + "\n" +"You have needed {:.3f}seconds".format(duration)
            if duration < 2:
                points += 5
                pic = random.choice(very_good)
                status1 += "\n **** Very good ! ******"
            elif duration < 10:
                points += 3
                pic = random.choice(good)
                status1 += "\n **** Good ! ******"
            else:
                points += 1
                pic = random.choice(not_bad)
                status1 += "\n **** Not bad ! ******"
        else:
            status1 ="false. The correct answer would be {}".format(x-y)
            points -= 1
            pic = random.choice(bad)
            status1 += "\n **** Bad ! ******"
        status1 = status1 + "\n" +"You have needed {:.3f}seconds".format(duration)
        easygui.msgbox(status1, "you have now {} points".format(points), image=pic)
            
    if op == "/":
        pic== None
        if e2 == y:
            status1 ="super,division correkt"
            #status1 = status1 + "\n" +"You have needed {:.3f} seconds".format(duration)
            if duration < 2:
                points += 10
                pic = random.choice(very_good)
                status1 += "\n **** Very good ! ******"
            elif duration < 10:
                points += 5
                pic = random.choice(good)
                status1 += "\n **** Good ! ******"
            else:
                points += 3
                pic = random.choice(not_bad)
                status1 += "\n **** Not bad ! ******"
        else:
            status1 ="false. The correct answer would be {}".format(x/y)
            points -= 1
            pic = random.choice(bad)
            status1 += "\n **** Bad ! ******"
        status1 = status1 + "\n" +"You have needed {:.3f}seconds".format(duration)
        easygui.msgbox(status1, "you have now {} points".format(points), image=pic)
             
easygui.msgbox("Game over")

