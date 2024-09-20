#Task 1
import re
text = "Rbbr RBBrr rbbbrr Rbr RbbR"
pattern = r"[Rr]b+r"
matches = re.findall(pattern, text)
print(matches)
# Task 2
import re
def validate_credit_card(card_number):
    pattern = r"^\d{4}-\d{4}-\d{4}-\d{4}$"
    if re.match(pattern, card_number):
        return True
    else:
        return False
card_number = "1234-5678-9876-5432"
if validate_credit_card(card_number):
    print("Номер картки валідний.")
else:
    print("Номер картки не відповідає формату.")
#Task 3
import re
def validate_email(email):
    pattern = r"^[A-Za-z0-9]+([_-][A-Za-z0-9]+)*@[A-Za-z]+\.[A-Za-z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False
email = "example-email@mail.com"
if validate_email(email):
    print("Email валідний.")
else:
    print("Email не відповідає вимогам.")
#Task 4
import re
def validate_login(login):
    pattern = r"^[A-Za-z0-9]{2,10}$"
    if re.match(pattern, login):
        return True
    else:
        return False
login = "user123"
if validate_login(login):
    print("Логін валідний.")
else:
    print("Логін не відповідає вимогам.")
