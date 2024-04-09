class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", "a") as file:
            file.write(f"Error: {msg}\n")


try:
    raise CustomException("Custom error massage.")
except CustomException as e:
    print("Custom exeption occured: ", e.msg)
