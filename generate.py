import argparse
import random

numbers = '0123456789'
symbols = '!";#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

parser = argparse.ArgumentParser()
parser.add_argument('len', type=int,
    help='password length')
parser.add_argument('-n', '--numbers',   action='store_true',
    help='exclude numbers')
parser.add_argument('-s', '--symbols',   action='store_true',
    help='exclude symbols')
parser.add_argument('-l', '--lowercase', action='store_true',
    help='exclude lowercase characters')
parser.add_argument('-u', '--uppercase', action='store_true',
    help='exclude uppercase characters')
parser.add_argument('-e', '--exclude', type=str,
    help='set of characters to exclude')
args = parser.parse_args()

if args.numbers:
    numbers = ''
if args.symbols:
    symbols = ''
if args.lowercase:
    lowercase = ''
if args.uppercase:
    uppercase = ''

characters = numbers + symbols + lowercase + uppercase

if args.exclude:
    characters = ''.join([c for c in characters if c not in args.exclude])

if len(characters) == 0:
    print('No valid characters.')
else:
    print(''.join(random.choices(characters, k=args.len)))
