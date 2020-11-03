import unittest

import pyarray


class Int8Suite(unittest.TestCase):
    def test_setattr_and_getattr(self):
        a = pyarray.Int8((0, 1))
        a[0] = 2
        self.assertEqual(a[0], 2)

    def test_explicit_elements(self):
        a = pyarray.Int8(3, 4)
        self.assertEqual(a[0], 3)

    def test_list(self):
        a = pyarray.Int8([5, 6])
        self.assertEqual(a[0], 5)

    def test_repr(self):
        a = pyarray.Int8(7, 8)
        self.assertEqual(repr(a), "Int8([7, 8])")

    def test_subclass(self):
        a = pyarray.Int8(9, 10)
        self.assertIsInstance(a, pyarray.Int8)

    def test_range(self):
        message = "signed char is less than minimum"
        with self.assertRaisesRegex(OverflowError, message):
            pyarray.Int8(-129)
        message = "signed char is greater than maximum"
        with self.assertRaisesRegex(OverflowError, message):
            pyarray.Int8(128)

    def test_element_type(self):
        message = "integer argument expected, got float"
        with self.assertRaisesRegex(TypeError, message):
            pyarray.Int8(11.12)


class UInt8Suite(unittest.TestCase):
    def test_repr(self):
        a = pyarray.UInt8(13, 14)
        self.assertEqual(repr(a), "UInt8([13, 14])")

    def test_range(self):
        message = "unsigned byte integer is less than minimum"
        with self.assertRaisesRegex(OverflowError, message):
            pyarray.UInt8(-1)
        message = "unsigned byte integer is greater than maximum"
        with self.assertRaisesRegex(OverflowError, message):
            pyarray.UInt8(256)

    def test_element_type(self):
        message = "integer argument expected, got float"
        with self.assertRaisesRegex(TypeError, message):
            pyarray.UInt8(15.16)


class Int16Suite(unittest.TestCase):
    def test_repr(self):
        a = pyarray.Int16(17, 18)
        self.assertEqual(repr(a), "Int16([17, 18])")

    def test_range(self):
        message = "signed short integer is less than minimum"
        with self.assertRaisesRegex(OverflowError, message):
            pyarray.Int16(-32_769)
        message = "signed short integer is greater than maximum"
        with self.assertRaisesRegex(OverflowError, message):
            pyarray.Int16(32_768)

    def test_element_type(self):
        message = "integer argument expected, got float"
        with self.assertRaisesRegex(TypeError, message):
            pyarray.Int16(19.20)


class UInt16Suite(unittest.TestCase):
    def test_repr(self):
        a = pyarray.UInt16(21, 22)
        self.assertEqual(repr(a), "UInt16([21, 22])")

    def test_range(self):
        message = "unsigned short is less than minimum"
        with self.assertRaisesRegex(OverflowError, message):
            pyarray.UInt16(-1)
        message = "unsigned short is greater than maximum"
        with self.assertRaisesRegex(OverflowError, message):
            pyarray.UInt16(65_536)

    def test_element_type(self):
        message = "integer argument expected, got float"
        with self.assertRaisesRegex(TypeError, message):
            pyarray.UInt16(19.20)


if __name__ == "__main__":
    unittest.main()
