from Serializer.picker import picker, unpicker
import pytoml as toml


class TomlSerializer:
    def __init__(self, path: str):
        self.path = path
        self.picker = picker.Picker()
        self.unpicker = unpicker.Unpicker()

    def dump(self, obj: object):
        obj_dict = self.picker.pack(obj)
        with open(self.path, "w") as file:
            toml.dump(obj_dict, file)

    def dumps(self, obj: object):
        obj_dict = self.picker.pack(obj)
        result_string = toml.dumps(obj_dict)
        return result_string

    def load(self):
        obj_dict = {}
        with open(self.path, "r") as file:
            obj_dict = toml.load(file)
        obj = self.unpicker.unpack(obj_dict)
        return obj

    def loads(self, obj_str: str):
        obj_dict = toml.loads(obj_str)
        obj = self.unpicker.unpack(obj_dict)
        return obj