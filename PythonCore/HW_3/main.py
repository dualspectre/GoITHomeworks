# task 1
from datetime import datetime

#function finding of difference between today and input date
def get_days_from_today(date:str)->int:
    """
    function get_days_from_today

    Input:
    date - str in format 'YYYY-MM-DD'

    Return:
    int
    """
    today = datetime.today()
    try:
        input_date = datetime.strptime(date,'%Y-%m-%d')
    except Exception:
        print('Incorrect data format')
        return
    return (today - input_date).days
    

# input_date_str = '2020-10-09'

# diff_days = get_days_from_today(input_date_str)
# print(diff_days)

#task 2

from random import randint


#function generating of list with winner lottery numbers
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    function get_numbers_ticket
    Input:
    min - int greater that 1
    max - int less than 1000
    quantity: int - numbers of generated random numbers

    Return:
    list of length quantity
    """
    result_tickets = set()
    try:
        if min < 1:
            return []
        elif max > 1000:
            return []
        elif quantity > (max - min + 1):
            return []
    except Exception:
        print("incorrect input values data")
        return []
    while len(result_tickets)<quantity:
        result_tickets.add(randint(min,max))
    return list(result_tickets)
    
   
# lottery_numbers = get_numbers_ticket(5,'10','50')
# print(lottery_numbers)


import re

def normalize_phone(phone_number: str) ->str:
    cleaned_number = re.sub(r'[^0-9+]','',phone_number)
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    return cleaned_number
    

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# norm_numbers = [normalize_phone(num) for num in raw_numbers]
# print(norm_numbers)