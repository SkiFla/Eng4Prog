 != 'quack'):
            trapdoor = input("\nError: try again.\nPress enter to continue.")
    while (trapdoor != "quack" and gdopt != 1):
        task, pn, sn, dscr = inquire(#Squawx

import datetime

###################START FUNCTIONS###################################
def newPage():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def inquire():
    task = int(input('''\nWhat would you like to do?
    *********
    1. Create a squawk
    2. Disposition a squawk
    3. Close a squawk
    4. Just looking
    **********
    '''))

    if(task == 1):
        pn = input('Whats the part number? \n')
        sn = input('Whats the serial number? \n')
        dscr = input('Whats the discrepency? \n')
       
    return task, pn, sn, dscr

def decode(task, pn, sn, dscr):
    if(task == 1):
        pn = 'Part number: '+ pn
        sn = 'Serial number: '+ sn
        dscr = 'Discrepency: '+ dscr

    return task, pn, sn, dscr
        
def preview(task,pn, sn, dscr):
    print('\n************************************\n\n' \
    + str(datetime.date.today()))

    print()
    if(task == 1):
        print(pn)
        print(sn)
        print(dscr)

    print('\n************************************')
       
def output(trapdoor,gdopt,task,pn, sn, dscr, fileName):
   if(trapdoor == '' and gdopt == 1):    
        f = open(fileName + '.txt','a')
        outPut = (str(datetime.date.today()) \
          + ' :: ' + pn + ': '\
          + sn + ': ' + dscr\
          + '\n' + '************************************\n')
        f.write(outPut)
        f.close()

def admin(fileName):
    boss = input('''\nWelcome Q.E.,
What would you like to do?\n
1- View Squawks
2- Go home\n''')
    
    if(boss == '1'):
        f = open(fileName + '.txt', 'r')
        show = f.read()
        print('\n************************************\n' + show)
        f.close()
    elif(boss == '2'):
        print('K, bye.')   

def main():
    gdopt = 2
    
    # Name file
    trapdoor = 'pizza'
    fileName = 'moduleX'
    
   
    
    print("Welcome to Squawk Book")
    trapdoor = input("Press enter to continue.\n")
    while (trapdoor != "" and trapdoor)
        task, pn, sn, dscr = decode(task, pn, sn, dscr)
        preview(task, pn, sn, dscr)
        gdopt = int(input('''\nDoes this look right?
    **********
    1- yes
    2- no
    **********
    '''))
        if(gdopt == 1):
            output(trapdoor,gdopt,task, pn, sn, dscr, fileName)
    
    if(trapdoor == "quack"):
        admin(fileName)
    lchance = input('\nWhat would you like to do next?\n1 = Exit\n2 = Rerun\n')
    if(lchance == '1'):
        print('\nThanks for using Squawx, Goodbye.')
    return lchance
    
##############################END FUNCTIONS####################################

lchance = '2'
while(lchance == '2'):
   lchance = main()
