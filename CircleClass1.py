#Muhammad Saad Mujtaba
#March 22, 2017

from PointClass import Point, isclose
from math import pi, radians

class Circle(object):
    """Attributes: Point object center, int or float number __radius
    representing the radius. """
    
    def __init__(self, x = 0, y = 0, radius = 1): #note default center and radius
        self.__center = Point(x,y) #MUST be a Point object!
        self.__rayon = radius
        

    @property
#getter for radius:
    def radius(self):
        """Allows us to write circleObject.radius
as if radius were a public attribute. Which it ISN'T.

This maintains the client's convenient access to the hidden
(private) attribute __rayon (radius in French), removing the need for the cumbersome
circleObject.get_radius() function call each time."""
        return self.__rayon

    @radius.setter
##setter for radius:
    def radius(self, rad):
        """Allows changing the radius with calls like
circleObject.radius = 57, removing the need for the cumbersone
circleObject.set_radius(57)function call."""
        
        self.__rayon = rad
        
    @property
##getter for center:
    def center(self):
        """Returns the circle's center, as a Point object"""
        return self.__center

    @center.setter
##setter for center:
    def center(self, x, y):
        """Puts the center of the circle to the point (x,y)"""
        self.__center = Point(x,y)

    
    def __str__(self): 
        """String representation of a Circle object."""

    # Create the string to be returned for printing(the output string).
        outp = "Center: {}; Radius: {}".format(self.__center,
                                                 self.__rayon)
        return outp

#equals method:
    def __eq__(self, other):
        return (self.center, self.radius) == (other.center, other.radius)

    def circumference(self):
        return 2*pi*self.__rayon
    
    def arc_length(self,alpha_deg):
        ''' Gives length of arc for central angle alpha_deg DEGREES'''
        return self.__rayon * radians(alpha_deg)

    def area(self):
        return pi * self.__rayon ** 2

    def contains_point(self, p):
        """Returns True iff Point object p is on or inside this circle"""
        distance_to_center = p.distance(self.__center)

        return distance_to_center <= self.__rayon
    
    def concentric_with(self, other):
        """ Two circles are concentric iff their centers are the same"""
        return self.__center == other.__center
    
    def intersect(self,other):
        return self.center.distance(other.center) <= self.radius+ other.radius

    def external_tangent(self,other):              
        """Checks that circles are exterally tangent"""
        if not self.intersect(other):                          
            print("Disjoint Circles")
            return False
        else:                                       
            return isclose(self.center.distance(other.center),self.radius + other.radius)
        
    def internal_tangent(self,other):
        """Checks that circles are interally tangent"""
        if not self.intersect(other):
            print("Disjoint Circles")
            return False
        else:
            return isclose(self.center.distance(other.center), abs(self.radius - other.radius))
    
    def tangent(self,other):
        return self.external_tangent(other) or self.internal_tangent(other)

# End of definition of Circle class



