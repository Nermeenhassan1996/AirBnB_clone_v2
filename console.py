#!/usr/bin/python3
"""
Airbnb Console
"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    The entry point for the command interpreter
    """
    prompt = ("(hbnb)")
    classes = ['BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review']

    def do_EOF(self, args):
        """EOF command to exit the program.
        """
        return True

    def do_quit(self, args):
        """ Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """method to do nothing when an empty line is inputed.
        """
        pass

    def do_create(self, line):
        """
        Usage: create <class name>

        Creates a new instance of BaseModel, saves it (JSON file) & prints id

        Ex: $ create BaseModel
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if line[0] == 'BaseModel':
                obj = BaseModel()
            elif line[0] == 'User':
                obj = User()
            elif line[0] == 'Place':
                obj = Place()
            elif line[0] == 'State':
                obj = State()
            elif line[0] == 'City':
                obj = City()
            elif line[0] == 'Amenity':
                obj = Amenity()
            elif line[0] == 'Review':
                obj = Review()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """
        Usage: show <class name> <id>

        Prints the string rep. of an instance based on the class name & id.

        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objects.keys():
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, line):
        """
        Usage: destroy <class name> <id>

        Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objects.keys():
                print("** no instance found **")
            else:
                del objects[key]
                models.storage.save()

    def do_all(self, line):
        """
        Usage: all <class name>

        Prints all string rep. of all instances based or not on the class name

        Ex: $ all BaseModel or $ all.
        """
        args = line.split()
        objects = models.storage.all()
        obj_list = []
        if len(args) == 0:
            for value in objects.values():
                obj_list.append(str(value))
        elif args[0] in HBNBCommand.classes:
            for key, value in objects.items():
                if args[0] in key:
                    obj_list.append(str(value))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Updates an instance based on the class name and id by adding or
        updating attribute(name & value) or using a dictionary representation
        save the change into the JSON file)

        Example:
        $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        $ update User 1234-1234-1234-1234 {'first_name': 'John', 'age': 89}
        """
        args = line.split()
        objects = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        if args[0] in HBNBCommand.classes:
            if len(args) > 1:
                key = "{}.{}".format(args[0], args[1])
                if key in objects.keys():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(objects[key], args[3], args[4])
                            models.storage.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
