

class Serializer:

    def serialize(self, ignore_none=False) -> dict:
        d = {}
        for attr in dir(self):
            val = getattr(self, attr)
            if not attr.startswith("__") and not callable(val):
                if ignore_none is True and val is None:
                    continue
                if issubclass(val.__class__, Serializer):
                    d[attr] = val.serialize(ignore_none=ignore_none)
                else:
                    d[attr] = val

        return d
