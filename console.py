#!/usr/bin/python3

'''
a program called console.py that contains the entry
point of the command interpreter:
'''
from cmd import Cmd


class HBNBCommand(Cmd):

    Cmd.prompt = "(hbnb)"

    def do_EOF(self, line):
        '''implement quit and EOF to exit the program'''
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line (just pressing ENTER)"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
