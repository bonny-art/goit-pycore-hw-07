from datetime import datetime

from .field import Field

class Birthday(Field):
    def __init__(self, value: str) -> None:
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y")
            if birthday_date > datetime.now():
                raise ValueError("Birthday date cannot be in the future")
            self.value = birthday_date
        except ValueError as exc:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") from exc
        super().__init__(value)

        
