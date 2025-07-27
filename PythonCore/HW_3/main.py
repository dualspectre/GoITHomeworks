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
    result_tickets = {}
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
    
   

