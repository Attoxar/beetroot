def stop_words(words):
    def decorator(func):
        def wrapper(name):
            modified_name = ' '.join('*' if word in words else word for word in name.split())
            return func(modified_name)

        return wrapper

    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return name

assert create_slogan("Steve drinks pepsi in his brand new BMW!") == "Steve drinks * in his brand new *!"
