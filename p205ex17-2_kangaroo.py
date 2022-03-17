# Write a definition for a class named Kangaroo with the following methods:
# 1. An __init__ method that initializes an attribute named pouch_contents to an empty list.
# 2. A method named put_in_pouch that takes an object of any type and adds it to pouch_contents.
# 3. A __str__ method that returns a string representation of the Kangaroo object and the contents of the pouch.
# Test your code by creating two Kangaroo objects, assigning them to variables named kanga and roo,
# and then adding roo to the contents of kanga’s pouch.

class Kangaroo:
    """ Represents a kangaroo.
        Attribute: pouch_contents
        Methods: __str__, put_in_pouch """

    def __init__(self):
        self.pouch_contents = []

    def __str__(self):
        if self.pouch_contents:
            return 'Kangaroo object with content: ' + ' '.join([str(obj) for obj in self.pouch_contents])
        else:
            return 'Empty Kangaroo object.'

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)


kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)
print(kanga)
print(roo)
