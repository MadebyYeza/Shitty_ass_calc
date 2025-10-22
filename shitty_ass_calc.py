#Dependencies
import time
import random

#-----------------------
#    Joke Lists :
#-----------------------

shitty_namej = ['Is that even a name?? I thought you were smarter, my bad. ]:',
                'I know this is a Shitty ass calc "{name}", but it doesnt mean you gotta use that shitty ass name.',
                'Choose another one', 'bruh', 'Lol?', 'Nice try!']

wrong_inputj = ['You adding letters, huh?', 'Are you trying to break my calculator?? Nuh uh']

resultj = ['Hmm... suspiciously easy numbers :-]', '{name} this sum is sus...','His IQ is more than 9000!!',
           'You must be very smart {name}!. At least if you didnt fail the name thing at the start :(',
           'Math is hard {name}, but you managed to survive!', 'Nice, there is it:']

#Shitty ass calculator
    
print('Shitty ass calc.inc')
print('\n')

while True:
    name = input('YO, dumbass, tell me ur name :)? ')

    if name.lower() in ['n','no','noo','n0','n00','nope','yes', 'ye', 'y','si', 's', 'sii', 'ok', 'okk','k']:
        print(random.choice(shitty_namej).format(name=name))
        time.sleep(1)
    else:
        break
    
#Calculus:
while True:
    try:
        n1 = float(input('Put the first value there: '))
        break
    except ValueError:
        print(random.choice(wrong_inputj).format(name=name))
        time.sleep(1)
    
while True:
    try:
        n2= float(input('Put the second value here: '))
        break
    except ValueError:
        print(random.choice(wrong_inputj).format(name=name))
        time.sleep(2)
    
result = (n1+n2)

ans = input('Would you like your result to be an integer? ')
print(' ')
if ans.lower() in ['yes','si', 'y3s', 's1']:
    result = int(result)
if random.random() <0.1:
    print(random.choice(resultj).format(name=name), result)
else:
    time.sleep(random.uniform(0.5, 1.5))
    print('Well,', name, 'there is it, your shitty ass result:', result)

#Fun stuff
mes1 = 'Who the hell uses a calc just for doing a simple sum?? '

print(' ')

answer = input(mes1)
if answer.lower() in ['me', 'mee', 'meee']:
    print('Who cares?, just shut up and get outta here!')
else:
    print('Just shup up and get outta here!')
print(' ')

time.sleep(1.5)
mes2 = input('(... punch him?) ')
if mes2 in ['NO', 'No', 'no', ' ', '']:
    print(' ')
else:
    print(' ')
    print('     NO. :)     ')
    print(' ')
time.sleep(3)
print('You are still there, huh?')

time.sleep(4)
print('\n')
print('*EXPLODES*')

#Auto_exit:
time.sleep(1)
exit()