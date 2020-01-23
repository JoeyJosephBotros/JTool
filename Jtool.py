import watchdir
import logParser
import scanmap
import urlfilter
import Portswatch
import os 

def Menu(lst, inpE):
    inp = -1
    while inp not in range(1, inpE+1):       
        for i in lst:
            print(i)
        try:
            inp = int(input("Input: "))
        except KeyboardInterrupt:
            exit(2)
        except:
            print("Make sure you entered a number!!")
        print("\n\n")
    os.system("clear")
    return inp

JMenu = ["Jtool V0.0.0.0.0 is the best ","1-Parse Your logs","2-Monitor Your Directory","3-Scan The Ports of Your Network","4-Watch Your Device And Prevent Attacks","5-URL Decompose"]
opt = Menu(JMenu,5)

if opt == 1:
    logParser.task1()
elif opt == 2:
    watchdir.task2()
elif opt == 3: 
    scanmap.task3()
elif opt == 4:
    Portswatch.task4()
elif opt == 5:
    urlfilter.task5()



