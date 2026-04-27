import string
import secrets
import sys
from pathlib import Path

generator = string.ascii_letters + string.digits
username = sys.argv[1]
password = ''.join(secrets.choice(generator) for i in range(int(sys.argv[2])))

try:
	with open(f'{username}.txt', 'x') as index:
		with open(f'{username}.txt', 'w') as index:
			index.write(f'Username: {username}\nPassword: {password}\n')
			print(f'Password for username "{username}" created successfully!"')

except FileExistsError:
	print(f'Error! Username "{username}" already exist!')
