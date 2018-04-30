from math import sqrt #for the distance function

class Point(object):

    def __init__(self, x = 0, y = 0): # Creates new Point object initialized
        ## with the coordinates x, y. 
        """This is the Object Constructor method"""
        self.x, self.y = x, y

    def __repr__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def copy(self):
        """ Creates a new Point object with identical data as
this one."""
        return Point(self.x, self.y)
    
# ***********************************************************
    def distance(self, other):
        """Returns the Euclidean distance from 'this' point
to the 'other' point."""
        def sq(num): # local helper function
            return num **2

        deltaX, deltaY = self.x-other.x, self.y - other.y
        return sqrt(sq(deltaX)+sq(deltaY))
    
# ***********************************************************
    def taxicab_distance(self, other):
        """Gives the distance in the 'Taxicab Metric':
number of city blocks EW + #. of city blocks NS from
self to other point."""
        # Taxicab Geometry makes sense when all coordinates are integers.

        deltaX, deltaY = self.x-other.x, self.y - other.y
        return abs(deltaX)+abs(deltaY)

    # End of definition of Point class

def isclose(a, b, rel_tol=1e-9, abs_tol=0.0):
    """rel_tol = relative tolerance, 1e-9 = 10 to the power -9,
abs_tol = absolute tolerance.
"""
    cond = abs(a-b) <= max(rel_tol * max(abs(a), abs(b)),
                            abs_tol )
    return cond

# Test runs    
if __name__ == '__main__': # code below is ignored if this module
                            # is imported by another module
    p1, p2 = Point(2,3), Point(5,7)
    print(p1, p2)

    print("sqrt(5)=",2.23606797749979)
    print(Point().distance(Point(1,2)) == 2.236)
##    False
    print(isclose(Point().distance(Point(1,2)), 2.236))
##False
    print(isclose(Point().distance(Point(1,2)), 2.23607,rel_tol = 1e-5))
##True
    
