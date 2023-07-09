from datetime import date, timedelta
from collections import defaultdict

from data_test import users


def change_date_to_monday(same_date: date) -> date:
    """
    принемают дату - видает следующий понедельник
    """
    one_day = timedelta(days=1) # для изменения даты поздравления сб/вс на пн
    while same_date.isoweekday() != 1: # прибавляем по дню пока не получим понедельник 
        same_date += one_day
    return same_date    

def day_name_print(data: dict):
    """
    вивод список имен по д.р. 
    принимает словарь date: [name]
    принтует "day of week : name, name .... "
    """
    for key,val in data.items():
        day = key.strftime('%A') # только день недели (преобразовиваем из дати)
        names = ", ".join(val)   # список в строку через запятую 
        print(f'{day}: {names}')


def get_birthdays_per_week(users: list[dict]) :
    """
    принимает список словарей формата 
    {"name": "name", "birthday": "yyyy-mm-dd"}

    вивод список имен по д.р. ближайшие 7 дней формата
    "day of week : name, name .... "

    исключение сб,вс попадают в следующий понедельник
    """

    current_date = date.today() # сегоднишняя дата
    plus_week_date = current_date + timedelta(weeks=1) # дата через неделю от сегодня
    

    weekly_reminder = defaultdict(list) # словарь в котором не нужно проверять существует ли ключ

    for user in users :
        birthday = date.fromisoformat(user["birthday"]) # получаем дату из словаря
        say_HB = birthday.replace(year=current_date.year) # меняем год - дата напоминания для поздравления(пока без изменения сб/вс на пн)

        if current_date <= say_HB < plus_week_date: # если др в промежутке сегодня включительно + неделя 

            # если дате напоминания сб/вс переносим ее на СЛЕДУЮЩИЙ пн 
            if say_HB.isoweekday() in [6,7]:
               say_HB = change_date_to_monday(say_HB)

            weekly_reminder[say_HB].append(user['name']) # заполняем словарь -  дата : список имен

    sort_weekly_reminder = dict(sorted(weekly_reminder.items())) # сортируем по дате       
   
    day_name_print(sort_weekly_reminder)



def main() :
    get_birthdays_per_week(users) 

if __name__ == '__main__' :
    main()