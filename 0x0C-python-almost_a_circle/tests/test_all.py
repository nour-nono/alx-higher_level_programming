#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_A_nb_objects_private(self):
        '''Tests if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        '''Tests constructor signature with 2 notself args.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        '''Tests consecutive ids.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_F_id_synced_more(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        '''Tests custom int id.'''
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_str(self):
        '''Tests custom int id.'''
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_id_keyword(self):
        '''Tests id passed as keyword arg.'''
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

    # ----------------- Tests for #15 ------------------------
    def test_H_to_json_string(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        s = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{"foobarrooo": 989898}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarrooo": 989898}]')

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]')

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}, {}]')

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    # ----------------- Tests for #17 ------------------------
    def test_H_test_from_json_string(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        s = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 312321, "id": 522244, "height": 34340}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(Base.from_json_string(s), d)

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        s = '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{"foobarrooo": 989898}]
        s = '[{"foobarrooo": 989898}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(s), d)

        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        s = '[{"x": 101, "y": 20123, "width": 312321, "id": 522244, \
"height": 34340}]'
        self.assertEqual(Base.from_json_string(s), d)

        list_in = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        list_out = Rectangle.from_json_string(
            Rectangle.to_json_string(list_in))
        self.assertEqual(list_in, list_out)

        # ----------------- Tests for #16 ------------------------
    def test_I_save_to_file(self):
        '''Tests save_to_file() method.'''
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

        # ----------------- Tests for #18 ------------------------
    def test_J_create(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        # ----------------- Tests for #19 ------------------------
    def test_K_load_from_file(self):
        '''Tests load_from_file() method.'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

class TestRectangle(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    # ----------------- Tests for #2 ------------------------

    def test_A_class(self):
        '''Tests Rectangle class type.'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        '''Tests if Rectangle inherits Base.'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_C_constructor_no_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        s = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_one_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Tests instantiation.'''
        r = Rectangle(10, 20)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Rectangle("1", 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, "3")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, "4")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -2)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -3)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -4)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        '''Tests positional instantiation.'''
        r = Rectangle(5, 10, 15, 20)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Rectangle(5, 10, 15, 20, 98)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Tests positional instantiation.'''
        r = Rectangle(100, 200, id=421, y=99, x=101)
        d = {'_Rectangle__height': 200, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Tests if id is inherited from Base.'''
        Base._Base__nb_objects = 98
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''Tests property getters/setters.'''
        r = Rectangle(5, 9)
        r.width = 100
        r.height = 101
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 101, '_Rectangle__width': 100,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 101)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    # ----------------- Tests for #3 ------------------------

    def invalid_types(self):
        '''Returns tuple of types for validation.'''
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_type(self):
        '''Tests property validation.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''Tests property validation.'''
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''Tests property validation.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        '''Tests property validation.'''
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        '''Tests property setting/getting.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        '''Tests property setting/getting.'''
        r = Rectangle(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    # ----------------- Tests for #4 ------------------------
    def test_I_area_no_args(self):
        '''Tests area() method signature.'''
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        '''Tests area() method compuation.'''
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r.width = w
        r.height = h
        self.assertEqual(r.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r = Rectangle(w, h, 7, 8, 9)
        self.assertEqual(r.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r = Rectangle(w, h, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * h)

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    # ----------------- Tests for #5 & #7 ------------------------
    def test_J_display_no_args(self):
        '''Tests display() method signature.'''
        r = Rectangle(9, 8)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_J_display_simple(self):
        '''Tests display() method output.'''
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.width = 3
        r.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(5, 6, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """







       #####
       #####
       #####
       #####
       #####
       #####
"""
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
#########
#########
#########
#########
#########
#########
#########
#########
"""
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(1, 1, 10, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\










          #
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 3, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 3, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\




#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        # ----------------- Tests for #6 ------------------------

    def test_K_str_no_args(self):
        '''Tests __str__() method signature.'''
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_K_str(self):
        '''Tests __str__() method return.'''
        r = Rectangle(5, 2)
        s = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(r), s)
        r = Rectangle(1, 1, 1)
        s = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(r), s)
        r = Rectangle(3, 4, 5, 6)
        s = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(r), s)

        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

        # ----------------- Tests for #8 & #9 ------------------------
    def test_L_update_no_args(self):
        '''Tests update() method signature.'''
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, d)

    def test_L_update_args(self):
        '''Tests update() postional args.'''
        r = Rectangle(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(10, 5)
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 17)
        d["_Rectangle__height"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 17, 20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 17, 20, 25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_L_update_args_bad(self):
        '''Tests update() positional arg fubars.'''
        r = Rectangle(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        with self.assertRaises(ValueError) as e:
            r.update(10, -5)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, -17)
        s = "height must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, 17, -20)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, 17, 20, -25)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

    def test_L_update_kwargs(self):
        '''Tests update() keyword args.'''
        r = Rectangle(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(width=5)
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(height=17)
        d["_Rectangle__height"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_L_update_kwargs_2(self):
        '''Tests update() keyword args.'''
        r = Rectangle(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(id=10, width=5)
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(id=10, width=5, height=17)
        d["_Rectangle__height"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(id=10, width=5, height=17, x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(id=10, width=5, height=17, x=20, y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

        r.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(r.__dict__, d)

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    # ----------------- Tests for #13 ------------------------
    def test_M_to_dictionary(self):
        '''Tests to_dictionary() signature:'''
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r = Rectangle(1, 2)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

        r = Rectangle(1, 2, 3, 4, 5)
        d = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

        r.x = 10
        r.y = 20
        r.width = 30
        r.height = 40
        d = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(r.to_dictionary(), d)

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

class TestSquare(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    # ----------------- Tests for #2 ------------------------

    def test_A_class(self):
        '''Tests Square class type.'''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        '''Tests if Square inherits Base.'''
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Tests instantiation.'''
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Square("1")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        '''Tests positional instantiation.'''
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Tests positional instantiation.'''
        r = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 100, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Tests if id is inherited from Base.'''
        Base._Base__nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''Tests property getters/setters.'''
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 98, '_Rectangle__width': 98,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.size, 98)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    # ----------------- Tests for #3 ------------------------

    def invalid_types(self):
        '''Returns tuple of types for validation.'''
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_type(self):
        '''Tests property validation.'''
        r = Square(1)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)
        s = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as e:
                setattr(r, "width", invalid_type)
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''Tests property validation.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''Tests property validation.'''
        r = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        '''Tests property validation.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        '''Tests property setting/getting.'''
        r = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        '''Tests property setting/getting.'''
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    # ----------------- Tests for #4 ------------------------
    def test_I_area_no_args(self):
        '''Tests area() method signature.'''
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        '''Tests area() method compuation.'''
        r = Square(6)
        self.assertEqual(r.area(), 36)
        w = randrange(10) + 1
        r.size = w
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, 7, 8, 9)
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * w)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as e:
            s1.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    # ----------------- Tests for #5 & #7 ------------------------
    def test_J_display_no_args(self):
        '''Tests display() method signature.'''
        r = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_J_display_simple(self):
        '''Tests display() method output.'''
        r = Square(1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.size = 3
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        r = Square(5, 6, 7)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(1, 1, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\










 #
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 3)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        f = io.StringIO()
        with redirect_stdout(f):
            s2.display()
        s = """\
  ##
  ##
"""
        self.assertEqual(f.getvalue(), s)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        f = io.StringIO()
        with redirect_stdout(f):
            s3.display()
        s = """\



 ###
 ###
 ###
"""
        self.assertEqual(f.getvalue(), s)

        # ----------------- Tests for #6 ------------------------

    def test_K_str_no_args(self):
        '''Tests __str__() method signature.'''
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_K_str(self):
        '''Tests __str__() method return.'''
        r = Square(5)
        s = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(r), s)
        r = Square(1, 1)
        s = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(r), s)
        r = Square(3, 4, 5)
        s = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(r), s)
        r = Square(10, 20, 30, 40)
        s = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(r), s)

        # ----------------- Tests for #8 & #9 ------------------------
    def test_L_update_no_args(self):
        '''Tests update() method signature.'''
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, d)

    def test_L_update_args(self):
        '''Tests update() postional args.'''
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(10, 5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 20, 25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_L_update_args_bad(self):
        '''Tests update() positional arg fubars.'''
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        with self.assertRaises(ValueError) as e:
            r.update(10, -5)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, -17)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, 17, -25)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

    def test_L_update_kwargs(self):
        '''Tests update() keyword args.'''
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(size=17)
        d["_Rectangle__height"] = 17
        d["_Rectangle__width"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_L_update_kwargs_2(self):
        '''Tests update() keyword args.'''
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5, x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5, x=20, y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

        r.update(y=25, id=10, x=20, size=5)
        self.assertEqual(r.__dict__, d)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    # ----------------- Tests for #14 ------------------------
    def test_M_to_dictionary(self):
        '''Tests to_dictionary() signature:'''
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r = Square(1)
        d = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(r.to_dictionary(), d)

        r = Square(9, 2, 3, 4)
        d = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(r.to_dictionary(), d)

        r.x = 10
        r.y = 20
        r.size = 30
        d = {'x': 10, 'y': 20, 'size': 30, 'id': 4}
        self.assertEqual(r.to_dictionary(), d)

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

if __name__ == "__main__":
    unittest.main()
