"""
@author: Samuel Tregea
@date: 8/14/2019
@description:
    This program was intended to write generate a random password.

    On the commandline a user has the option to enter:
        -s x

    Arguments are then checked, and the script generate a password of size 'x'.
    If x equals 0, or there are no command arguments, the default password size
    is set to 8 characters.
"""
import random
import argparse


def random_password(char_length):
    """
    Helper function that takes a character length to determine
    the length a new password
    :param char_length: The wanted password length
    :return: a newly generated password
    """
    password = ""
    chars_str = "abcdefghijklmnopqrstuvwxyz@%+\/'!#$^?:.(){}[]~-_.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, char_length):
        char = random.randrange(len(chars_str))
        password = password + chars_str[char]
    return password


def main():
    """
    The main method to this program. A user, on the command line will enter "-s x", where x is a number.
    If a user enters '0' or doesn't enter parameters, the default password size will be set to 8 characters.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', help="The wanted size of the password.", type=int)

    args = parser.parse_args()
    char_size = args.size

    print("*** Password Generator ***")
    if char_size:
        password = random_password(char_size)
    else:
        password = random_password(8)
    print("Your newly generated password: " + password)


if __name__ == '__main__':
    main()
