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
    input('                     press enter')
    print('\n' * 6)
    print('          sociopath sō′sē-ə-păth″')
    print('\n' * 2)
    print('     someone with a sociopathic personality; a person with an antisocial personality disorder [psychopath was once widely used but has now been superseded by sociopath]')
    print('\n' * 2)    
    input('                     press enter')
    print('\n' * 6)
    print('Its half past noon and you have been asleep for what feels like days.')
    print(' ')
    print('you wake up to a dark room that smells of metal, mold, chemicals,')
    print(' ')
    print(' and a faint smell of rotting food')
    print('\n' * 2)
    input('                     press enter')
    print('\n' * 6) 
    print('You ask yourself "Why do I keep living like this?"')
    print(' ')
    print('Immediatley you forget about that feeling...')
    print(' ')
    print('Carefully you move through the room past all the tools and bottles')
    print(' ')
    print('You flip the light switch to the bathroom')
    print('\n' * 4)
    print('                    Click!')
    print('\n' * 2)
    input('                     press enter')
    print('\n' * 6)
    print('The light blinds you and the smell of shit wafts into your nose')
    print(' ')
    print('The same stale shit thats been stuck to the side of the bowl is still there')
    print(' ')
    print('The familiar words "I will clean that later"')
    print(' ')
    print('You dont even believe your own bullshit anymore...')
    print('\n' * 2)
    input('                     press enter')
    print('\n' * 6)
    print('==============================================')
    print('\n' * 6)

# using old code from frist game to make this simple path input.
def introPath():
    print('\n' * 2)
    path = input('Do you stay inside or try to leave...')
    if path == 'leave' or path == 'Leave':
        print('predictable')
        pathLeave()
    elif path == 'Stay' or path == 'stay':
        print('Afraid of change?')
    else:
        if path != 'Leave' or path != 'leave' or path != 'Stay' or path != 'stay':
            print('\n' * 2)
            print('leave or stay?')
            print(' ')
            introPath()

# first path to be fleshed out. still linear
def pathLeave():
    print('\n' * 2)
    print('You try to make youself as clean as possible with out making much effort')
    print(' ')
    print('You open the door and realize no one is home')
    print(' ')
    print('The rest of the aprtment is dark and lifeless except for a couple cats')
    print(' ')
    print('"I should get my own pet..."')
    print(' ')
    print('The thought leaves you as quickly as it came...')
    print('\n' * 6)
    input('                     press enter')






titleScreen()
print('============================')
print('\n' * 6)
introStory()
introPath()


