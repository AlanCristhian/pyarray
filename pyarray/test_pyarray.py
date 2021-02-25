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
        with self.assertRaises(OverflowError):
            pyarray.Int8(-129)
        with self.assertRaises(OverflowError):
            pyarray.Int8(128)

    def test_element_type(self):
        with self.assertRaises(TypeError):
            pyarray.Int8(11.12)


class UInt8Suite(unittest.TestCase):
    def test_repr(self):
        a = pyarray.UInt8(13, 14)
        self.assertEqual(repr(a), "UInt8([13, 14])")

    def test_range(self):
        with self.assertRaises(OverflowError):
            pyarray.UInt8(-1)
        with self.assertRaises(OverflowError):
            pyarray.UInt8(256)

    def test_element_type(self):
        with self.assertRaises(TypeError):
            pyarray.UInt8(15.16)


class Int16Suite(unittest.TestCase):
    def test_repr(self):
        a = pyarray.Int16(17, 18)
        self.assertEqual(repr(a), "Int16([17, 18])")

    def test_range(self):
        with self.assertRaises(OverflowError):
            pyarray.Int16(-32_769)
        with self.assertRaises(OverflowError):
            pyarray.Int16(32_768)

    def test_element_type(self):
        with self.assertRaises(TypeError):
            pyarray.Int16(19.20)


class UInt16Suite(unittest.TestCase):
    def test_repr(self):
        a = pyarray.UInt16(21, 22)
        self.assertEqual(repr(a), "UInt16([21, 22])")

    def test_range(self):
        with self.assertRaises(OverflowError):
            pyarray.UInt16(-1)
        with self.assertRaises(OverflowError):
            pyarray.UInt16(65_536)

    def test_element_type(self):
        with self.assertRaises(TypeError):
            pyarray.UInt16(23.24)


class Int32Suite(unittest.TestCase):
    def test_repr(self):
        a = pyarray.Int32(25, 26)
        self.assertEqual(repr(a), "Int32([25, 26])")

    def test_range(self):
        with self.assertRaises(OverflowError):
            pyarray.Int32(-2_147_483_649)
        with self.assertRaises(OverflowError):
            pyarray.Int32(2_147_483_648)

    def test_element_type(self):
        with self.assertRaises(TypeError):
            pyarray.Int32(27.28)


class UInt32Suite(unittest.TestCase):
    def test_repr(self):
        a = pyarray.UInt32(29, 30)
        self.assertEqual(repr(a), "UInt32([29, 30])")

    def test_range(self):
        with self.assertRaises(OverflowError):
            pyarray.UInt32(-1)
        with self.assertRaises(OverflowError):
            pyarray.UInt32(4_294_967_296)

    def test_element_type(self):
        with self.assertRaises(TypeError):
            pyarray.UInt32(31.32)


class Float32Suite(unittest.TestCase):
    def test_repr(self):
        a = pyarray.Float32(31.1, 32.2)
        self.assertIn("Float32", repr(a))

    def test_element_type(self):
        with self.assertRaises(TypeError):
            pyarray.Float32(33.3 + 1j)


class Float64Suite(unittest.TestCase):
    def test_repr(self):
        a = pyarray.Float64(33.3, 34.4)
        self.assertIn("Float64", repr(a))

    def test_element_type(self):
        with self.assertRaises(TypeError):
            pyarray.Float64(35.5 + 1j)


if __name__ == "__main__":
    unittest.main()
