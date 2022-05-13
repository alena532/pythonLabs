from tests import templates as t
import unittest
from Serializer import serializer as s


class TestClass(unittest.TestCase):
    def __init__(self, method):
        super().__init__(method)
        self.serializer_json = s.Serializer()
        path = self.serializer_json.path
        self.serializer_json.path = "../test.json"
        ext = self.serializer_json.name
        self.serializer_json.name = "json"
        self.serializer_toml = s.Serializer(path='../test.toml', name='toml')
        self.serializer_yaml = s.Serializer(path='../test.yaml', name='yaml')

    # tests primitives
    def test_int(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.num_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.num_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.num_temp))

        self.assertEqual(json_test, t.num_temp)
        self.assertEqual(toml_test, t.num_temp)
        self.assertEqual(yaml_test, t.num_temp)

    def test_float(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.float_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.float_temp))
        yaml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.float_temp))

        self.assertEqual(json_test, t.float_temp)
        self.assertEqual(toml_test, t.float_temp)
        self.assertEqual(yaml_test, t.float_temp)

    def test_string(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.str_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.str_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.str_temp))

        self.assertEqual(json_test, t.str_temp)
        self.assertEqual(toml_test, t.str_temp)
        self.assertEqual(yaml_test, t.str_temp)

    def test_byte(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.bytes_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.bytes_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.bytes_temp))

        self.assertEqual(json_test, t.bytes_temp)
        self.assertEqual(toml_test, t.bytes_temp)
        self.assertEqual(yaml_test, t.bytes_temp)

    def test_byte_array(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.bytes_arr_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.bytes_arr_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.bytes_arr_temp))

        self.assertEqual(json_test, t.bytes_arr_temp)
        self.assertEqual(toml_test, t.bytes_arr_temp)
        self.assertEqual(yaml_test, t.bytes_arr_temp)

    def test_bool(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.bool_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.bool_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.bool_temp))

        self.assertEqual(json_test, t.bool_temp)
        self.assertEqual(toml_test, t.bool_temp)
        self.assertEqual(yaml_test, t.bool_temp)


    def test_buitin_func(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.buitin_func_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.buitin_func_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.buitin_func_temp))

        self.assertEqual(json_test, t.buitin_func_temp)
        self.assertEqual(toml_test, t.buitin_func_temp)
        self.assertEqual(yaml_test, t.buitin_func_temp)

    def test_list(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.list_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.list_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.list_temp))

        self.assertEqual(json_test, t.list_temp)
        self.assertEqual(toml_test, t.list_temp)
        self.assertEqual(yaml_test, t.list_temp)

    def test_set(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.set_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.set_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.set_temp))

        self.assertEqual(json_test, t.set_temp)
        self.assertEqual(toml_test, t.set_temp)
        self.assertEqual(yaml_test, t.set_temp)

    def test_frozenset(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.frozenset_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.frozenset_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.frozenset_temp))

        self.assertEqual(json_test, t.frozenset_temp)
        self.assertEqual(toml_test, t.frozenset_temp)
        self.assertEqual(yaml_test, t.frozenset_temp)

    def test_tuple(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.tuple_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.tuple_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.tuple_temp))

        self.assertEqual(json_test, t.tuple_temp)
        self.assertEqual(toml_test, t.tuple_temp)
        self.assertEqual(yaml_test, t.tuple_temp)

    def test_dict(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.dict_temp))
        toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.dict_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.dict_temp))

        self.assertEqual(json_test, t.dict_temp)
        self.assertEqual(toml_test, t.dict_temp)
        self.assertEqual(yaml_test, t.dict_temp)

    def test_object(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.obj_temp))
        #toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.obj_temp))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.obj_temp))

        self.assertEqual(json_test.el1, t.obj_temp.el1)
        self.assertEqual(json_test.el2, t.obj_temp.el2)
        #self.assertEqual(toml_test.el1, t.obj_temp.el1)
        #self.assertEqual(toml_test.el2, t.obj_temp.el2)
        self.assertEqual(yaml_test.el1, t.obj_temp.el1)
        self.assertEqual(yaml_test.el2, t.obj_temp.el2)


    #class tests
    def test_class(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.TempClass))
        #toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.TempClass))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.TempClass))

        self.assertEqual(json_test.__bases__[0].__name__, t.TempClass.__bases__[0].__name__)
        #self.assertEqual(toml_test.__bases__[0].__name__, t.TempClass.__bases__[0].__name__)
        self.assertEqual(yaml_test.__bases__[0].__name__, t.TempClass.__bases__[0].__name__)

    def test_function(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.question_temp_func))
        #toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.question_temp_func))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.question_temp_func))

        self.assertEqual(json_test(), t.test_question)
        #self.assertEqual(toml_test, t.test_question)
        self.assertEqual(yaml_test(), t.test_question)

    def test_function_with_global_func(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.my_age_question))
        #toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.my_age_question))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.my_age_question))

        self.assertEqual(json_test(), t.test_age_answer)
        #self.assertEqual(toml_test, t.test_age_answer)
        self.assertEqual(yaml_test(), t.test_age_answer)

    def test_function_with_params(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.mul_params))
        #toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.mul_params))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.mul_params))

        self.assertEqual(json_test(2, 5), t.test_multiple)
        # self.assertEqual(toml_test(2, 5), t.test_multiple)
        self.assertEqual(yaml_test(2, 5), t.test_multiple)

    def test_lambda(self):
        json_test = self.serializer_json.loads(self.serializer_json.dumps(t.multiple))
       # toml_test = self.serializer_toml.loads(self.serializer_toml.dumps(t.multiple))
        yaml_test = self.serializer_yaml.loads(self.serializer_yaml.dumps(t.multiple))

        self.assertEqual(json_test(2, 5), t.test_multiple)
        #self.assertEqual(toml_test(2, 5), t.test_multiple)
        self.assertEqual(yaml_test(2, 5), t.test_multiple)
