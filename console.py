#!/usr/bin/python3
"""
the entry point to the console app
"""


import cmd
from models.base_model import BaseModel
from models import storage
import re


classes = ["BaseModel"]

def parse(line):
    return re.findall(r'"(?:\\"|.)*?"|\S+', line)

class HBNBCommand(cmd.Cmd):
    """
    the man cmd class
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        end of file signal to quit the program
        """
        print()
        return True

    def do_quit(self, line):
        """
        quit command to quit the program
        """
        return True

    #def do_help(self, line):
        #"""
        #helps you know the docstring of a function
        #"""
        #return line.__doc__

    def emptyline(self):
        pass

    def do_create(self, line):
        """
        creates a new instance of BaseModel
        Usuage: create BaseModel
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def do_show(self, line):
        """
        prints the string represntation of an instance based
        on the class name and id
        Usuage: show BaseModel 123123-13-412312-1312
        """
        args = parse(line)
        model_list = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            look_up_model = f"{args[0]}.{args[1]}"
            if look_up_model not in model_list:
                print("** no instance found **")
            else:
                print(model_list[look_up_model])

    def do_destroy(self, line):
        """
        deletes an instance based
        on the class name and id
        Usuage: destroy BaseModel 123123-13-412312-1312
        """
        args = parse(line)
        model_list = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            look_up_model = f"{args[0]}.{args[1]}"
            if look_up_model not in model_list:
                print("** no instance found **")
            else:
                del(model_list[look_up_model])
                storage.save()

    def do_all(self, line):
        """
        prints all instance representation based or not
        Usage: all OR all BaseModel
        """
        args = parse(line)
        model_list = storage.all()

        if len(args) == 0:
            for model in model_list:
                print(model_list[model])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for model in model_list:
                if model.split(".")[0] == args[0]:
                    print(model_list[model])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
