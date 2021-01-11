#! python3
# pass_locker.py An insecure password locker program

password = {
    'gmail' : 'trabajarengoogle',
    'platzi' : 'Halo8675',
    'amazon' : 'jeffbezos'
}

import sys, pyperclip

if len(sys.argv < 2):
    print('Usage: python pass_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print(f'Password for {account} copied to clipboard')
else:
    print(f'The account {account} is not aviable')