import argparse
from Serializer import serializer as s


def arg_func():
    parser = argparse.ArgumentParser(description="ConsoleArgparse")
    parser.add_argument('original', type=str, help='Original file')
    parser.add_argument('target', type=str, help='Target file') #  путь до папки с 'toml'
    parser.add_argument('extension', type=str, help='New file extension') #  'toml'

    argv = parser.parse_args()

    serializer = s.Serializer(argv.original, argv.original.split('.')[-1])  # took extension
    obj = serializer.load()
    serializer.path = argv.target
    serializer.name = argv.extension.lower()
    serializer.dump(obj)
    print("Success!!!")


if __name__ == "__main__":
    arg_func()
