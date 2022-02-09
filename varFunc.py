#FILE: varFunc.py
#AUTHOR: Thomas Bennett

#Example 1: Default Argument Values

def ask_ok(prompt, retries = 4, reminder = 'Try again...'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes'):
            return True
        if ok in ('n', 'no'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid entry...')
        print(reminder)

#retries and reminder are given default values
#these values may be overridden

#Example 2: Keyword Arguments

def parrot(volts, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
    print("-- This parrot wouldn't", action, end = ' ')
    print("if you put", volts, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

#volts is a required argument, the rest are optional

b = True
while b:
    parrot(action = 'VOOOOM', volts = 'a million')
    b = ask_ok("Continue?")
