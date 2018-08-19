

class Serializer:

    def serialize(self, ignore_none=False) -> dict:
        d = {}
        for attr in dir(self):
            val = getattr(self, attr)
            if not attr.startswith("__") and not callable(val):
                if ignore_none is True and val is None:
                    continue
                try:
                    d[attr] = getattr(self, attr).serialize(ignore_none=ignore_none)
                except TypeError:
                    d[attr] = getattr(self, attr).serialize()
                except AttributeError:
                    d[attr] = getattr(self, attr)

        return d
