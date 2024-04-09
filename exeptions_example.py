import os
# import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(current_dir, "logfile.txt")

dividend = input("please type in the dividend: ")
divisor = input("please type in the divisor: ")
# if not divisor.isdigit() or not dividend.isdigit():
#     sys.exit("wrong input only numbers supported")

result = None

try:
    file_object = open(log_path, "a")
    result = f"the quotient is {float(dividend)/float(divisor)}"
    file_object.write(result)
except ValueError:
    print("wrong input only numbers supported and (optionaly) dots")
    # result = "wrong input"
except ZeroDivisionError:
    print("You cant divide by zero")
    # result = "Zero division"
finally: #cleaning upp the stuff before
    file_object.close()
# else:
#     result = "success"
# file_object = open(log_path, "a")
# file_object.write(result)
# file_object.close()

import request_executer


while True:
    request = request_executer.take_request_from_queue()
    replay = request_executer.execute(request)
    replay_sender.send(replay)
except Exception as error:
logger.log(error)