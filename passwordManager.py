#! python3
# --TODO secure the passwords
import sys
import paperclip

PASSWORDS={'email': 'paralyze123', 'facebook': 'paralyze123'}
if(len(sys.argv)<2):
    print('Usage: python passwordManager [account]')
    sys.exit()

account= sys.argv[1]
if(account in PASSWORDS):
    paperclip.copy(PASSWORDS[account])
    print('Password copied to clipboard')
else:
    print('There is no account named ' + account)
