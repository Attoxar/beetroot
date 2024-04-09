def arg_rules(type_, max_length, contains):
    def decorator(func):
        def wrapper(name):
            checks = [
                (isinstance(name, type_), f"Argument '{name}' is not of type {type_.__name__}."),
                (len(name) <= max_length, f"Length of argument '{name}' exceeds maximum length of {max_length}."),
                (all(symbol in name for symbol in contains), f"Argument '{name}' does not contain all required symbols: {contains}.")
            ]
            failed_checks = [reason for condition, reason in checks if not condition]
            if failed_checks:
                for reason in failed_checks:
                    print(f"Validation failed: {reason}")
                return False
            return func(name)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'


# same code just with an iinput to try some stuff out
# def arg_rules(type_, max_length, contains):
#     def decorator(func):
#         def wrapper(name):
#             checks = [
#                 (isinstance(name, type_), f"Argument '{name}' is not of type {type_.__name__}."),
#                 (len(name) <= max_length, f"Length of argument '{name}' exceeds maximum length of {max_length}."),
#                 (all(symbol in name for symbol in contains), f"Argument '{name}' does not contain all required symbols: {contains}.")
#             ]
#             failed_checks = [reason for condition, reason in checks if not condition]
#             if failed_checks:
#                 for reason in failed_checks:
#                     print(f"Validation failed: {reason}")
#                 retry = input("Do you want to retry? (yes/no): ")
#                 if retry.lower() == 'yes':
#                     new_name = input("Enter a new value: ")
#                     return wrapper(new_name)
#                 else:
#                     return False
#             return func(name)
#         return wrapper
#     return decorator
#
#
# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
#
#
# assert create_slogan('johndoe05@gmail.com') is False
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
