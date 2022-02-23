import re


class Date:
    def __init__(self, date):
        self.date = date
        self.date = Date.valid(self)

    @classmethod
    def extract_int(cls, date):
        dd = int(date[:2])
        mm = int(date[3:5])
        yy = int(date[6:])
        return dd, mm, yy

    @staticmethod
    def valid(obj):
        re_date = re.compile("([0-3][0-9]-[0-1][0-9]-[0-9]{4})")
        while not re_date.findall(obj.date):
            obj.date = input("please, enter date format DD-MM-YYYY: ")
        return obj.date


a = Date(date=input("please, enter date format DD-MM-YYYY: "))
print(a.date)
print(a.extract_int(a.date))

