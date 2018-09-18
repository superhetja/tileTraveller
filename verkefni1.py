#Við byrjum á því að gera ráð fyrir að við getum farið í hvaða átt sem er er, og byrjum á 1,1
# Við útilokum þær átti sem notandinn má ekki fara á s.s allir útveggir og miðju vegginir sem eru lokaðir.
# Við byðjum notandann um input þangað til hann slær in valid input. og færum notandann á viðeigandi reit.
# þangað til notandinn er kominn á reit 3,1 þá lýkur forritið

x = 1
y = 1
while not ((x == 3) and ( y == 1)):

#Outer walls
    North = True
    West = True
    East = True
    South = True
    if x == 1:
        West = False
    if x == 3:
        East = False
    if y == 1:
        South = False
    if y == 3:
        North = False
#Wall restrintions
    if (y == 1):
        West = False
        East = False
    elif (x == 2) and (y == 2):
        East = False
        North = False
    elif (x == 3) and (y == 2):
        West = False
    elif (x == 2) and (y == 3):
        South = False

#Prints which direction you can travel in
    print ('You can travel: ',end='')
    if North:
        print ('(N)orth' ,end='')
        if East or West or South:
            print (' or' ,end=' ')
    if East:
        print ('(E)ast', end='')
        if West or South:
            print (' or' ,end=' ')
    if South:
        print('(S)outh', end='')
        if West:
            print (' or' ,end=' ')
    if West:
        print ('(W)est',end='')
    print('.')
    
#Impements the new value of x and y and asks for directions
    while True:
        direction = input('Direction: ').upper()

        if direction == 'N' and North:
            y += 1
            break
        elif direction == 'S' and South:
            y -= 1
            break
        elif direction == 'E' and East:
            x += 1
            break
        elif direction == 'W' and West:
            x -=1
            break
        else:
            print('Not a valid direction!')

print ('Victory!')







    



