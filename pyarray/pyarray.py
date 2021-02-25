from array import array


__all__ = ["Int8", "UInt8", "Int16", "UInt16", "Int32", "UInt32", "Int64",
           "UInt64", "Float32", "Float64", ]


_TEMPLATE = """
class {name}Meta(type):
    def __call__(cls, *initializer):
        if len(initializer) == 1:
            if isinstance(initializer[0], (list, tuple)):
                initializer = initializer[0]

        {name}_array = array("{typecode}", initializer)

        class {name}Class:

            # Methods:
            append = {name}_array.append
            buffer_info = {name}_array.buffer_info
            byteswap = {name}_array.byteswap
            count = {name}_array.count
            extend = {name}_array.extend
            fromfile = {name}_array.fromfile
            fromlist = {name}_array.fromlist
            frombytes = {name}_array.frombytes
            index = {name}_array.index
            insert = {name}_array.insert
            pop = {name}_array.pop
            remove = {name}_array.remove
            reverse = {name}_array.reverse
            tofile = {name}_array.tofile
            tolist = {name}_array.tolist
            tobytes = {name}_array.tobytes

            # Attributes:
            typecode = {name}_array.typecode
            itemsize = {name}_array.itemsize

            # Methods defined here:
            __add__ = {name}_array.__add__
            __contains__ = {name}_array.__contains__
            __copy__ = {name}_array.__copy__
            __deepcopy__ = {name}_array.__deepcopy__
            __delitem__ = {name}_array.__delitem__
            __eq__ = {name}_array.__eq__
            __ge__ = {name}_array.__ge__
            __getattribute__ = {name}_array.__getattribute__
            __getitem__ = {name}_array.__getitem__
            __gt__ = {name}_array.__gt__
            __iadd__ = {name}_array.__iadd__
            __imul__ = {name}_array.__imul__
            __iter__ = {name}_array.__iter__
            __le__ = {name}_array.__le__
            __len__ = {name}_array.__len__
            __lt__ = {name}_array.__lt__
            __mul__ = {name}_array.__mul__
            __ne__ = {name}_array.__ne__
            __reduce_ex__ = {name}_array.__reduce_ex__
            __rmul__ = {name}_array.__rmul__
            __setitem__ = {name}_array.__setitem__
            __sizeof__ = {name}_array.__sizeof__

            def __repr__(self):
                return {name}_array.__repr__() \
                    .replace("array('{typecode}', ", "{name}(")

        cls.__parent = {name}Class
        cls.__typecode = {name}_array.__repr__().split("'")[1]
        return {name}Class()

    def __instancecheck__(self, other):
        return (self.__parent in type(other).__mro__) \
            and (self.__typecode == '{typecode}')


class {name}(metaclass={name}Meta):
    pass
"""


# I define this just to calmdown linters. Just ignore the next 10 lines
Int8 = array
UInt8 = array
Int16 = array
UInt16 = array
Int32 = array
UInt32 = array
Int64 = array
UInt64 = array
Float32 = array
Float64 = array


# Here is the real definition
exec(_TEMPLATE.format(name="Int8", typecode="b"))
exec(_TEMPLATE.format(name="UInt8", typecode="B"))
exec(_TEMPLATE.format(name="Int16", typecode="h"))
exec(_TEMPLATE.format(name="UInt16", typecode="H"))
exec(_TEMPLATE.format(name="Int32", typecode="l"))
exec(_TEMPLATE.format(name="UInt32", typecode="L"))
exec(_TEMPLATE.format(name="Int64", typecode="q"))
exec(_TEMPLATE.format(name="UInt64", typecode="Q"))
exec(_TEMPLATE.format(name="Float32", typecode="f"))
exec(_TEMPLATE.format(name="Float64", typecode="d"))
