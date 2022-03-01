import argparse
import string
import secrets


def main():
    parser = argparse.ArgumentParser(description='Password generator')
    parser.add_argument("-l", '--length', type=int, default=12, help='sets password length', metavar='')
    parser.add_argument("-c", '--count', type=int, default=1, help='sets the number of passwords to print', metavar='')

    args = parser.parse_args()
    length = args.length
    count = args.count
    
    if(length<=0):
        raise Exception("Must be greater than zero.")
    if (count<=0):
        raise Exception("Must be greater than zero.")

    for i in range(count):
        secure = string.digits + string.ascii_letters + string.punctuation
        secure = "".join(secrets.choice(secure) for i in range(length))        
        print(secure)



if __name__ == "__main__":
    main()