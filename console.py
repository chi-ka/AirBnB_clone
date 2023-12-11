#!/usr/bin/python3

'''
a program called console.py that contains the entry
point of the command interpreter:
'''
from cmd import Cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(Cmd):
    '''The Command Line Class'''

    Cmd.prompt = "(hbnb)"
    classes = classes = ["BaseModel", "User"]

    def do_EOF(self, line):
        '''implement quit and EOF to exit the program'''
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line (just pressing ENTER)"""
        pass

    def do_create(self, args):
        '''Creates a new instance of BaseModel'''

        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if class_name == "User":
            my_model = User()
        elif class_name == "BaseModel":
            my_model = BaseModel()
        my_model.save()
        print(my_model.id)

    def do_show(self, args):
        '''Prints the string representation of an instance
        based on the class name and id'''
        args = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_ = args[0]
        if class_ not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) != 2:
            print("** instance id missing **")
            return

        class_id = args[1]

        check = storage.all()
        check = storage.all()
        key = f"{class_}.{class_id}"
        if key in check.keys():
            print(check[key])
        else:
            print("** no instance found **")

    def do_all(self, args):
        '''Prints all string representation of all instances
        based or not on the class name. '''
        args = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_ = args[0]
        if class_ not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        check = storage.all()
        for key, obj in check.items():
            print(obj)

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id
        save the change into the JSON file.'''
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_ = args[0]
        if class_ not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) != 2:
            print("** instance id missing **")
            return
        class_id = args[1]

        check = storage.all()
        serialized_objects = {}
        del_key = f"{class_}.{class_id}"
        if del_key in check.keys():
            del check[del_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]

        key = f"{class_name}.{instance_id}"

        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]

        obj = all_objects[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
