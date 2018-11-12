"""
Notes

 - if you don't add an __eq__ method in the function
 - r in [...,...,...] does not work
 - __eq__ is invoked when '==' is called
 - __init__ is invoked when initialized Rational(5, 8)
 - __str__ is invoked whenever the variable must be converted into a str type i.e. print(Rational)
   r.__str__ or str(r)
 - __mul__ and __it__?
 - module is a name space, the space in which that name is unique is that name space, when used anywhere else you have to import them
 - to avoid name collission we surround names in name spaces and then we check to see if that name is indeed unique
 - doc string delcares what the variables represent
 - right click function name --> run that specific doctest
 - == invokes the __eq__ for already defined classes, but since they are defined, we can use it to check equality of the object

 - __repr__ another repsentation of the string if you do
 >>> r = Rational(5,6)
 r
 (it will return not the str)
 instructor for the equivalent rational, so with repr it returns:
 Rational(5,6)

  - __lt__ is less than returns None by default, this can be used for sorting and tells you whether a defined object is less than the other "You can't sort things that are so called incomprable"
  - ctrl+/ comments multi lines
  - the way you impleement the code is similar to __eq_- except you replace == with <

 - n1/d2 < n2/d2 <=> n1d2 < d1n2
 - if d1 * d2 > 0
   else n1 * d2 > d1 * n2 "functional if that can become a function in it of itself"

 - __mul__ multiplies two objects into one

 - when you're in the middle of defining the class it doesn't know the existence of rational so you need to put it in quotes
 - when docstrings are run they are run in an environemnt outside the class

 - making your program friendly with operators is called syntactic sugar

 - code done by contract, you list the conditions that the input must be under and if anyone breaks those rules and gets an error it's their fault.

 - from file(.py) import class
 - raise errors as soon as possible
 - remember that if a condition doesn't meet certain conditions and you catch it, you can alter the attribute itself after the __init__
 - user property - a secret method that is called to ensure user's cannot change the properties

 private method invariant
 - name starts with an underscore
 - docstring doesn't have '''''' and only has # because it's not meant to be seen by the user
 - note that the _ doesn't protect against using that method, its just an agreement not to use it fam
 -

make public attributes directly accessible (no accessors, aka
getters/setters)
I use assert
I use property to delegate the management of public
attributes behind the scenes

 - you can ensure the privacy of attributes by making it immutable or use the property builtin

############################

building a class using composition
see solitary_shape.py when danny releases it

self.l = l[:] for aliasing

list comprehension
everytime you want to take an old list and make a new list, and you're replacing the old list in the new list

self.corners = [(c + offset_point) for c in self.corners]
#equivalent to...
new_corners = []
for c i self.corners:
    new_corners.append(c.add(offset_point))

###############################
when you write a generic class a super class where you can try to put all the code that is the same among different subclasses
once you find a method that is different we still declare them in the super class as a placeholder so you can extend it

type(object).__name__ --> 'object'

rather than iterating through a list to concatenate a string use the .join() method.

whenever you have a superclass that only has a placeholder you raise an error
raise NotImplementedError('subclass not implemented')

methods in the superclass can be straight inherited from the class

why do we add the error in placeholder methods

"""

class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
