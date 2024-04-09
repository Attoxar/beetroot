from datetime import datetime
name = input("whats your name: ")
dt = datetime.now()
print("Good day ", name, "! ", dt.strftime("%A"), " is a perfect day to learn some python.", sep="")
