def oops():
    # raise IndexError("Oops! Here is an index error")
    raise KeyError("Oops! Here is an index error")


def error_checker():
    try:
        oops()
    except IndexError as error:
        print("here i catch an index error: ", error)


error_checker()

# What happens if you change oops to raise KeyError instead of IndexError?

# "error_checker is only catching index errors, while the oops function is currently raising a
# Keyerror it will not be catched."
# The key error is producing a crash and the unhandled error will be displayed
