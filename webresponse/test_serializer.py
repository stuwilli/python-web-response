from webresponse import Serializer


def fixtures():
    class TestClass(Serializer):
        def __init__(self, x, y, z):
            self.val_x = x
            self.val_y = y
            self.val_z = z
            self.val_none = None
            self.val_object = TestClass2(x, y)

    class TestClass2(Serializer):
        def __init__(self, a, b):
            self.val_a = a
            self.val_b = b

    return TestClass("string_1", True, 2)


def test_serializer():
    tc = fixtures()

    assert tc.serialize() == {"val_x": "string_1", "val_y": True, "val_z": 2,
                              "val_none": None, "val_object": {"val_a": "string_1", "val_b": True}}


def test_serializer_ignore_none():
    tc = fixtures()

    assert tc.serialize(ignore_none=True) == {"val_x": "string_1", "val_y": True, "val_z": 2,
                                              "val_object": {"val_a": "string_1", "val_b": True}}


def test_serializer_to_camel_case():
    assert Serializer.to_camel_case("this_should_be_camel_case") == "thisShouldBeCamelCase"


def test_serializer_camel_case():
    tc = fixtures()

    assert tc.serialize(ignore_none=True, camel_case=True) == {"valX": "string_1", "valY": True, "valZ": 2,
                                                               "valObject": {"valA": "string_1", "valB": True}}
