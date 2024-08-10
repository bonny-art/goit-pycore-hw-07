from datetime import datetime, timedelta, date
from typing import List, Dict
from collections import UserDict

from .record import Record

class AddressBook(UserDict):

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name, None)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

    def __str__(self) -> str:
        return "\n".join(str(record) for record in self.data.values())

    def _is_date_within_days(self, target_date: datetime, days: int) -> bool:
        today_date = datetime.now().date()
        date_this_year = date(today_date.year, target_date.month, target_date.day)

        if date_this_year < today_date:
            target_date = date(today_date.year + 1, target_date.month, target_date.day)
        else:
            target_date = date_this_year

        return today_date <= target_date <= (today_date + timedelta(days=days))

    def _adjust_to_weekday(self, date_obj: date) -> date:
        if date_obj.weekday() == 5:  # Saturday
            return date_obj + timedelta(days=2)

        if date_obj.weekday() == 6:  # Sunday
            return date_obj + timedelta(days=1)

        return date_obj

    def get_upcoming_birthdays(self) -> List[Dict[str, str]]:
        upcoming_birthdays_list = []
        days = 7

        for record in self.data.values():
            if record.birthday:
                try:
                    user_birthday = record.birthday.value

                    if self._is_date_within_days(user_birthday, days):
                        current_year = datetime.now().year
                        congratulation_date = date(current_year, user_birthday.month, user_birthday.day)

                        congratulation_date = self._adjust_to_weekday(congratulation_date)

                        upcoming_birthdays_list.append({
                            "name": record.name.value,
                            "birthday": congratulation_date.strftime("%d.%m.%Y")
                        })

                except ValueError:
                    pass

        return upcoming_birthdays_list