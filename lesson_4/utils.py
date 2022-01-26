from requests import get, utils
from decimal import Decimal
from datetime import date

def currency_rates(argv):
    name, val = argv
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    ind = content.find("Date=")
    day = int(content[ind + 6: ind + 8])
    month = int(content[ind + 9: ind + 11])
    year = int(content[ind + 12: ind + 16])

    my_list = content.split("</Value>")
    for i in my_list:
        if ">" + val.upper() + "<" in i:
            i = i.replace(",", ".")
            num = Decimal(i[-7:])
            print(num.quantize(Decimal("1.00")), date(year, month, day))

if __name__ == "__main__":
    print("Hi!")