#!/usr/bin/python3
"""
testing for amenity class
"""


from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """
    testing for the class Amenity
    """
    
    def test_placehold(self):
        """
        placeholder for now
        """
        amen = Amenity()
        self.assertEqual(type(amen), Amenity)


if __name__ == "__main__":
    unittest.main()
