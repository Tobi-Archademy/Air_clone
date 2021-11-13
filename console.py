#!/usr/bin/python3
"""The Console"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Representation of the console class"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits Console"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Overwrites the emptyline command"""
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()