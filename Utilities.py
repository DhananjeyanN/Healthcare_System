from datetime import date


def input_date(datetype):
    dob = input(f"Enter {datetype}: ")
    day, month, year = dob.split("/")
    if day[0] != "0" and len(day) == 1:
        day = "0" + day
    if month[0] != "0" and len(month) == 1:
        month = "0" + month
    output_date = date.fromisoformat(f"{year}-{month}-{day}")
    return output_date