from datetime import datetime, timedelta, date

from typing import List, Dict



def is_date_within_days(target_date: datetime, days: int) -> bool:

    today_date = datetime.now().date()

    date_this_year = date(today_date.year, target_date.month, target_date.day)

    if date_this_year < today_date:
        target_date = date(today_date.year + 1, target_date.month, target_date.day)
    else:
        target_date = date_this_year

    return today_date <= target_date <= (today_date + timedelta(days=days))



def adjust_to_weekday(date_obj: date) -> date:

    if date_obj.weekday() == 5:  # Saturday
        return date_obj + timedelta(days=2)
    elif date_obj.weekday() == 6:  # Sunday
        return date_obj + timedelta(days=1)
    return date_obj



def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:

    upcoming_birthdays_list = []
    days = 7

    for user in users:
        try:
            user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")

            if is_date_within_days(user_birthday, days):

                current_year = datetime.now().year
                congratulation_date = date(current_year, user_birthday.month, user_birthday.day)

                congratulation_date = adjust_to_weekday(congratulation_date)

                upcoming_birthdays_list.append({
                    "name": user["name"],
                    "birthday": congratulation_date.strftime("%Y.%m.%d")
                })

        except ValueError:
            pass

    return upcoming_birthdays_list