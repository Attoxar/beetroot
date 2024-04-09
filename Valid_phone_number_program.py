def phone_number_check(phone_number):
    if len(phone_number) != 10 or not phone_number.isdigit():
        return False
    else:
        return True


userinput = input("input phone number here: ")
if phone_number_check(userinput):
    print("Looks Good")
else:
    print("wrong Format")
