__author__ = 'cedric'
class TheThing(object):

    def __init__(self):
        self.number = 0

    def some_function(self):
        print "I got called."

    def add_me_up(self,more):
        self.number += more
        return self.number

# two different things
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.number
print b.number

# Study this. This is how you pass a varialbe
# from one class to another. You will need this.
class TheMultiplier(object):

    def __init__(self,base):
        self.base = base

    def do_it(self,m):
        return m * self.base

x = TheMultiplier(a.number)
print x.do_it(b.number)