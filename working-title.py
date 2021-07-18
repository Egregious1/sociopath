#Attempt two at making a text based game. The first one was directionless and more for building foundation this one should prove better than the last.

# should really consider changing the dialouge to input commands and remove the press enter inputs...

def titleScreen():
    print('==============================')
    print('(                            )')
    print('(                            )')
    print('(     Working title          )')
    print('(                            )')
    print('(                            )')
    print('(                            )')
    print('(                            )')
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
    print('\n' * 6)
    print('Its been 4 months since you have had an actual job')
    print(' ')
    print('Your roommates have told you time and again to "get your shit together"')
    print(' ')
    print('As usual you just ignore it and act like nothing is wrong...')
    print('\n' * 2)
    input('                     press enter')
    print('\n' * 2)
    print('You stand there in your shame and ask yourself what you should do today')
    print('\n' * 2)
    print('"I could go find a job or go across the street and hang out at the garage')


# this should be the first major path choice
def firstPath():
    print('\n' * 2)
    path = input('Do you look for  or go to the garage?(work or garage): ')
    if path == 'work' or path == 'Work':
        print('that will be the day...')
        input('                     press enter')
    elif path == 'garage' or path == 'Garage':
        print('All the time in the world huh?')
        print('\n' * 4)
        garagePath()
    else:
        if path != 'work' or path != 'Work' or path != 'Garage' or path != 'garage':
            print('\n' * 2)
            print('Work or Garage?')
            print(' ')
            firstPath()

# work path
def workPath():
    print('\n' * 2)
    print('You decide you are going to make good on your promise of finding a job')
    print(' ')
    print('you grab your keys after putting on your shoes and head out the door')
    print(' ')
    input('                     press enter')
    print('\n' * 2)
    print('You walk out the door and make your way downstairs to your car')
    print(' ')
    print('You enter you car and put your keys into the ignition')
    print(' ')
    print('                    Click!')
    print(' ')
    input('                     press enter')
    print('\n' * 2)
    print('"Fuck!" you yell out "This shit always happens to me!"')
    print(' ')
    print('You have spent the last 3 months attempting to fix your car but in your')
    print('laziness you just never got around to it')
    print('\n' * 2)
    input('                     press enter')
    print('\n' * 4)
    print('You start cursing at an invisible enemy that has been out to "get" you')
    print(' ')
    print('and you make yourself back up stairs')
    print(' ')
    print('At this point you decide to get high....again.')
    # add next part of path here.


# garagePath section
def garagePath():
    print('\n' * 2)
    print('As usual you make your way down to the garage to waste time')
    print(' ')
    print('You have convinced yourself that the owner is going to give you job')
    print(' ')
    print('In fact he already gave you a chance at a job and you ended up getting high and sleeping in instead')
    print(' ')
    input('                     press enter')
    print('\n' * 4)
    print('                     For some reason you still think you have a chance')
    print('\n' * 4)






titleScreen()
print('============================')
print('\n' * 6)
introStory()
introPath()
firstPath()

