import os
from datetime import date

print(f"The files and folders in {os.getcwd()} are:")
items = os.listdir('.')
for item in items:
    prefix = "(d) " if os.path.isdir(item) else "(f) "
    print(f"{prefix}\t{item}")

date_of_programming = date.today()
print(f"date: {date_of_programming}")