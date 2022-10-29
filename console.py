#!/usr/bin/python3
"""
console module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBComand class
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """handles EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
