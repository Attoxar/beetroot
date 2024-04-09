from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                int_result = int(result)
                print(f"Converted {result} to integer: {int_result}")
                return int_result
            except (ValueError, TypeError):
                print(f"Unable to convert {result} to integer")
                return result
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                bool_result = result.lower() in ['true', '1', 't', 'yes', 'y']
                print(f"Converted {result} to boolean: {bool_result}")
                return bool_result
            bool_result = bool(result)
            print(f"Converted {result} to boolean: {bool_result}")
            return bool_result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            str_result = str(func(*args, **kwargs))
            print(f"Converted result to string: {str_result}")
            return str_result
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                float_result = float(result)
                print(f"Converted {result} to float: {float_result}")
                return float_result
            except (ValueError, TypeError):
                print(f"Unable to convert {result} to float")
                return result
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
