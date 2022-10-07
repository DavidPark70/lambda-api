import json
from decimal import Decimal


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
        if isinstance(obj, Decimal):
            return float(obj)

        return json.JSONEncoder.default(self, obj)
