import calendar

class myCalendarException(Exception):
    def __str__(self):
        return "Invalid weekday number. "


class myCalendar(calendar.Calendar):
    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self, year, weekday):
        if weekday < 0 or weekday > 6:
            raise myCalendarException
        
        self.__counts = 0
        for mnum in range(1, 13):
            mon = self.monthdays2calendar(year, mnum)
            for week in mon:
                for day in week:
                    if day[0] != 0 and day[1] == weekday:
                        self.__counts += 1
        return self.__counts



c = myCalendar()
print(c.count_weekday_in_year(2000, 6))
