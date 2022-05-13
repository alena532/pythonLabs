from math import sin
from Serializer.json_serializer import serializer_json
c = 42


def araa(x):
    a = 123
    return sin(x * a * c)


js = serializer_json.JsonSerializer('json')

obj = serializer_json.JsonSerializer.dumps(js, araa(10))
print(obj)
obj_ = serializer_json.JsonSerializer.loads(js, obj)
print(obj_)
