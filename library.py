#function for splitind book informattion
def listSplit():
    global bookname
    global authorname
    global quantity
    global cost
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    with open("stock.txt","r") as f:

        lines=f.readlines()
        #print(lines)
        lines=[x.strip('\n') for x in lines]
        #print(lines)
        for i in range(len(lines)):
            #priwnt(lines[i])
            ind=0
            for a in lines[i].split(','):
                #print(a)
                if(ind==0):
                    bookname.append(a)
                elif(ind==1):
                    authorname.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    cost.append(a)
                ind+=1
    print(" _____________________________________________________________________")
    print("|  %-25s |  %-14s |  %-8s  |  %-7s|"%("Book Name","Author Name","Quantity","Cost"))
    print("|____________________________|_________________|____________|_________|")
    for each in range(3):
        print("|  %-25s | %-15s |  %-8s  |  %-7s|"%(bookname[each],authorname[each],quantity[each],"$"+cost[each]))
        print("|____________________________|_________________|____________|_________|")



#importing date,time and day
import datetime
import time
dT= datetime.datetime.now()
borrowDate = str(dT.strftime("%d/%B/%Y")) #date
borrowTime = str(dT.strftime("%I:%M %p")) #12 hour format / PM:AM
borrowDay = str(dT.strftime("%A")) #Day
timestamp = int(time.time())  #Epoch time: 1970 now in sec


#function for borrowing book
def borrowBook():
    #coding related to borrowing book
    print("")
    name=input(" Enter the name of the borrower: ")

    t="Borrow-"+name+".txt"
    with open(t,"w+") as f:
        f.write("+=========================================================+"+"\n")
        f.write("|               Informatics College Pokhara               |  \n")
        f.write("+=========================================================+"+"\n")
        f.write("              Borrowed By: "+ name+"\n")
        f.write(" Date: " + borrowDate+"\n")
        f.write(" Time-"+ borrowTime+"\n")
        f.write(" Day: "+borrowDay+"\n")
        f.write(" _________________________________________________________"+"\n")
        f.write("| S.N.\t |   %-28s|   %-13s|"%("Book Name","Author Name")+"\n" )
        f.write("|________|_______________________________|________________|"+"\n")
    print()
    print(" Please select a option below:")
    for i in range(len(bookname)):
        print(" Enter [", i, "] to borrow book", bookname[i])
    while True:#error handellng
        try:
            a = int(input())
            if (a>=0 and a<3):
                break
            else:
                print(" Invalied!!! Please select a number from the option")
        except:
            print(" Invalied!!! Please select a number from the option")
    if(int(quantity[a])>0):
        print(" Book is available")
        print()
        with open(t,"a") as f:
            f.write("| 1. \t |   %-28s|   %-13s|"%(bookname[a],authorname[a])+"\n")
            f.write("|________|_______________________________|________________|"+"\n")

        quantity[a]=int(quantity[a])-1
        with open("Stock.txt","w+") as f:
            for i in range(3):
                f.write(bookname[i]+","+authorname[i]+","+str(quantity[i])+","+cost[i]+"\n")
        #multiple book borrowing code
        for j in range(2):
            print(" Do you want to borrow next book?")
            print(" Press Y for Yes")
            choice=input()
            if(choice.upper()=="Y"):
                print()
                print(" Please select a option below:")
                for i in range(len(bookname)):
                    print(" Enter [", i, "] to borrow book", bookname[i])
                while True:#error handelling
                    try:
                        a = int(input())
                        if (a>=0 and a<3):
                             break
                        else:
                            print(" Invalied!!! Please select a number from the option")
                    except:
                         print(" Invalied!!! Please select a number from the option")

                if(int(quantity[a])>0):
                    print(" Book is available")
                    with open(t,"a") as f:
                        f.write("| "+str(j+2) +".\t |   %-28s|   %-13s|"%(bookname[a],authorname[a])+"\n")
                        f.write("|________|_______________________________|________________|"+"\n")

                    quantity[a]=int(quantity[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(bookname[i]+","+authorname[i]+","+str(quantity[i])+","+cost[i]+"\n")

            else:
                break



    else:
        print(" Book is not available choose next book!")
        print("_______________________________________")
        borrowBook()

# function for returning book
def returnBook():
    print()
    name=input(" Enter name of borrower: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            data=f.read()
            print(data)


        b="Return-"+name+".txt"
        with open(b,"w+")as f:
            f.write("+=======================================================+"+"\n")
            f.write("|              Informatics College Pokhara              |"+"\n")
            f.write("+=======================================================+"+"\n")
            f.write("              Returned By: "+ name+"\n")
            f.write(" Date: " + borrowDate+"\n")
            f.write(" Time: "+borrowTime+"\n")
            f.write(" Day: "+borrowDay+"\n")
            f.write(" _______________________________________________________"+"\n")
            f.write("| S.N.\t |    %-29s |     %-6s|"%("Book Name","Cost")+"\n")
            f.write("|________|__________________________________|___________|"+"\n")


        total=0.0
        with open(a,"r") as f:
            data=f.read()

            for i in range(3):
                if bookname[i] in data:
                    with open(b,"a") as f:
                        f.write("| "+str(i+1)+" \t |    %-29s |    %-7s|"%(bookname[i],"$"+cost[i])+"\n")
                        f.write("|________|__________________________________|___________|"+"\n")


                        quantity[i]=int(quantity[i])+1
                    total+=float(cost[i])

        print(" Total: ",total)
        print(" Is the book return date expired?")
        print(" Press [ Y ] for Yes and [ N ] for No:")
        stat=input()
        if(stat.upper()=="Y"):
            print(" By how many days was the book returned late?")
            while True:#excepton handeling/error handeling
                try:
                    day = int(input())
                    break
                except:
                    print( "Error!! Enter a valid number")
            fine=2*day
            with open(b,"a")as f:
                f.write("|\t\t\t\t      %-7s%-11s|"%("Fine: $",str(fine))+"\n")
                f.write("|_______________________________________________________|"+"\n")
            total=total+fine

        print("Final Total:", total)
        with open(b,"a")as f:
            f.write("|\t\t\t\t     %-8s%-10s |" %("Total: $", str(total))+"\n")
            f.write("|_______________________________________________________|"+"\n")
        with open("Stock.txt","w+") as f:
                for i in range(3):
                    f.write(bookname[i]+","+authorname[i]+","+str(quantity[i])+","+cost[i]+"\n")
    except:
        print("The borrower name is incorrect.")
        returnBook()

#Main function to start the program
def start():
    while (True):
            print(" ============================================================")
            print(" |          Welcome to the library management system        |")
            print(" ============================================================")
            print(" Enter 1. To Display")
            print(" Enter 2. To Borrow a book")
            print(" Enter 3. To return a book")
            print(" Enter 4. To exit")
            while True:#error handelling
                try:
                    a = int(input(" Select a choice from 1-4: "))
                    break
                except:
                    print(" Please enter a valid choice from 1-4")
                    print()
            if(a==1):
                print()
                print(" Do read the information here")
                listSplit()
                print()

            elif(a==2):
                listSplit()
                borrowBook()

            elif(a==3):
                listSplit()
                returnBook()

            elif(a==4):
                print(" Thank you for using library management system")
                break
            else:
                print(" Please enter a valid choice from 1-4")

start()
