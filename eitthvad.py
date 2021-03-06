#Við byrjum á því að gera ráð fyrir að við getum farið í hvaða átt sem er er, og byrjum á 1,1
# Við útilokum þær átti sem notandinn má ekki fara á s.s allir útveggir og miðju vegginir sem eru lokaðir.
# Við byðjum notandann um input þangað til hann slær in valid input. og færum notandann á viðeigandi reit.
# þangað til notandinn er kominn á reit 3,1 þá lýkur forritið
# git er skemmtilegt
# 1. Which implementation was easier and why?
# I think it was the same it looks exatcly the same and the code is just as long
# 2. Which implementation is more readable and why?
# Maybe the definition code since the functions are defined and you can read through them
# 3. Which problems in the first implementations were you able to solve with the latter
# implementation?
#Nothing really so I'm not so sure now that I did it right. But if your not using the 
#function more then once then all your doing is moving the functionality, and I can't
#find a way to use the function more than once.
#https://github.com/superhetja/tileTraveller

def walls (x, y):
    """ Defines all the walls of the board"""
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
    return North, South, West, East

def valid_directions(x,y):
    """Prints out the directions the user can inpur"""
    North, South, West, East = walls(x,y)
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
    return North, South, West, East
    

def new_location (x, y):
    """Finds the new locations and returns result"""
    North, South, West, East = walls(x,y)
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
    return x, y

x = 1
y = 1
while not ((x == 3) and ( y == 1)):

    valid_directions(x,y)
    x,y = new_location(x,y)

print ('Victory!')

