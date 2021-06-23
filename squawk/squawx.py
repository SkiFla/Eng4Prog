# Shipheus
# 4/10/18
# MicroDon.py

import datetime

###################START FUNCTIONS###################################
def newPage():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def inquire():
    area = int(input('''\nPlease choose work area.
    *********
    1. MGB
    2. Topcoat
    3. Dress
    **********
    '''))
    if (area == 2):
        booth = input('What booth? ')
    else:
        booth = ''
    if(area == 1):
        mask = input('How many parts did you mask? \n')
        grit = input('How many parts did you grit blast? \n')
        bond = input('How many parts did you bond coat? \n')
        eos = ''
        bos = ''
        p_s = ''
        p_f = ''
    else:
        bos = int(input('''\nWas there a part in process at the beginning of shift?
    **********
    1- yes
    2- no
    **********
    '''))
        p_s = int(input('How many parts did you start? \n')) #parts_start
        p_f = int(input('How many parts did you finish? \n'))#parts_finish
        eos = int(input('''\nWas there a part in process at the end of shift?
    **********
    1- yes
    2- no
    **********
    '''))
        mask = ''
        grit = ''
        bond = ''
    return area, bos, p_s, p_f, eos, mask, grit, bond, booth

def decode(shift, area, bos, p_s, p_f, eos, mask, grit, bond, booth):
    shift = shift + ' shift'
    if(area == 1):
        area = 'MGB'
        mask = mask + ' parts masked.'
        grit = grit + ' parts gritblasted.'
        bond = bond + ' parts bondcoated.'
        p_s = ''
        p_f = ''
    elif(area == 2):
        area = 'Topcoat'
        booth = 'Booth ' + str(booth)
    else:
        area = 'Dress'
    if(bos == 1):
        bos = 'There was part in progress at bos.'
    elif(bos == 2):
        bos = ''
    if(eos == 1):
        eos = 'There was a part in progress at eos.'
    elif(eos == 2):
        eos = ''
    if(area != 'MGB'):
        p_s = str(p_s) + ' parts started.'
        p_f = str(p_f) + ' parts finished.'
    return area, bos, eos, mask, grit, bond, p_s, p_f, booth
        
def preview(shift, area, bos, p_s, p_f, eos, mask, grit, bond, booth):
    print('\n************************************\n\n' \
    + str(datetime.date.today()) + ' \n' + shift)
    print('Area: ' + area)
    if(area == 'Topcoat'):
        print(booth)
    print()
    if(area == 'MGB'):
        print(mask)
        print(grit)
        print(bond)
    if(bos != ''):
        print(bos)
    if(area != 'MGB'):
        print(p_s)
        print(p_f)
    if(eos != ''):
        print(eos)
    print('\n************************************')
       
def output(shift, trapdoor, gdopt, area, bos, p_s, p_f, eos, mask, grit, bond, booth, fileName):
   if(trapdoor == '' and gdopt == 1):    
        f = open(fileName + '.txt','a')
        outPut = (str(datetime.date.today()) \
          + ' :: '  + shift + ' :: Area: ' + area + ':: ' + booth +'\n\n' + mask + ': '\
          + grit + ': ' + bond + ': ' + bos + ': ' + p_s + ': ' + p_f + ': ' + eos \
          + '\n' + '************************************\n')
        f.write(outPut)
        f.close()

def admin(fileName):
    boss = input('''\nWelcome Leadman,
What would you like to do?\n
1- View production
2- clear all\n''')
    
    if(boss == '1'):
        f = open(fileName + '.txt', 'r')
        show = f.read()
        print('\n************************************\n' + show)
        f.close()
    elif(boss == '2'):
        safe = input("\nAre you sure?\n1 = yes\n2 = no\n")
        if(safe == '1'):
            f = open(fileName + '.txt', 'w')
            f.write('')
            f.close()
        else:
            print('clear all aborted.')    

def main():
    gdopt = 2
    
    # Name file
    if (datetime.datetime.now().hour >= 0 and datetime.datetime.now().hour < 7):
        shift = '3rd Shift'
    elif (datetime.datetime.now().hour >= 7 and datetime.datetime.now().hour <= 15 ):
        if (datetime.datetime.now().hour == 15 and datetime.datetime.now().minute >= 30):
            shift = '2nd Shift'
        else:
            shift = '1st Shift'
    else:
        shift = '2nd Shift'
    
    fileName = str(datetime.date.today()) + '-' + shift
    
    trapdoor = 'pizza'
    
    print("Let's see what you've done today.")
    trapdoor = input("Press enter to continue.\n")
    while (trapdoor != "" and trapdoor != 'theprodigaldon'):
            trapdoor = input("\nError: try again.\nPress enter to continue.")
    while (trapdoor != "theprodigaldon" and gdopt != 1):
        area, bos, p_s, p_f, eos, mask, grit, bond, booth = inquire()
        area, bos, eos, mask, grit, bond, p_s, p_f, booth = decode(shift, area, bos, p_s, p_f, eos, mask, grit, bond, booth)
        preview(shift, area, bos, p_s, p_f, eos, mask, grit, bond, booth)
        gdopt = int(input('''\nDoes this look right?
    **********
    1- yes
    2- no
    **********
    '''))
        if(gdopt == 1):
            output(shift, trapdoor, gdopt, area, bos, p_s, p_f, eos, mask, grit, bond, booth, fileName)
    
    if(trapdoor == "theprodigaldon"):
        admin(fileName)
    lchance = input('\nWhat would you like to do next?\n1 = Exit\n2 = Rerun\n')
    if(lchance == '1'):
        print('\nThanks for using MicroDon, Goodbye.')
    return lchance
    
##############################END FUNCTIONS####################################

lchance = '2'
while(lchance == '2'):
   lchance = main()
