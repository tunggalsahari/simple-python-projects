import string
import secrets
import sys

def main():

    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(int(sys.argv[1])))
    print(password)

if __name__ == "__main__":
    main()
