from Serializer.json_serializer import serializer_json as json
from Serializer.toml_serializer import serializer_toml as toml
from Serializer.yaml_serializer import serializer_yaml as yaml


class Factory:
    def __init__(self, path: str):
        self.path = path

    def create_serializer(self, name="json"):
        if name.lower() == "json":
            return json.JsonSerializer(self.path)
        elif name.lower() == "yaml":
            return yaml.YamlSerializer(self.path)
        elif name.lower() == "toml":
            return toml.TomlSerializer(self.path)

