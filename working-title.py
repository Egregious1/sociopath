#Attempt two at making a text based game. The first one was directionless and more for building foundation this one should prove better than the last.

def titleScreen():
    print('==============================')
    print('=                            =')
    print('=                            =')
    print('=     Working title          =')
    print('=                            =')
    print('=                            =')
    print('=                            =')
    print('=                            =')
    print('==============================')
    print('\n' * 2)
    playerName = input('What is your name? ')
    print()
    print(f'Welcome {playerName}!')

# start of game. always the same when starting game.
def introStory():
    print('     "You are always so full of shit!"')
    print('\n' * 2)
    print('               "Why are you doing this to us?"')
    print('\n' * 2)
    print('      "You only care about yourself!"')
    print('\n' * 2)
    print('"We are not friends anymore..."')
    print('\n' * 2)
    input('press enter')
    print('\n' * 6)
    print('          sociopath sō′sē-ə-păth″')
    print('\n' * 2)
    print('     someone with a sociopathic personality; a person with an antisocial personality disorder [psychopath was once widely used but has now been superseded by sociopath]')
    print('\n' * 2)    
    input('press enter')
    print('\n' * 6)
    print('Its half past noon and you have been asleep for what feels like days.')
    print(' ')
    print('you wake up to a dark room that smells of metal, mold, chemicals,')
    print(' ')
    print(' and a faint smell of rotting food')
    print('\n' * 2)
    input('press enter')
    print('\n' * 6) 
    print('You ask yourself "Why do I keep living like this?"')
    print(' ')
    print('Immediatley you forget about that feeling...')
    print(' ')
    print('Carefully you move through the room past all the tools and bottles')
    print(' ')
    print('You flip the light switch to the bathroom')
    print(' ')
    print('                    Click!')
    input('press enter')

# using old code from frist game to make this simple path input.
def choosePath():
    path = input('What do you choose? [L or R] ')
    if path == 'L' or path == 'l':
        print('predictable')
    elif path == 'R' or path == 'r':
        print('Afraid of change?')
    else:
        if path != 'l' or path != 'L' or path != 'r' or path != 'R':
            print('try again')
            print(' ')
            choosePath()






titleScreen()
print('============================')
print('\n' * 6)
introStory()


