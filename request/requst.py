class Requst:
    def __init__(self, day, shift_num, name, rzf, details):
        self.day = convert_num_to_day(day)
        self.week = week(shift_num)
        self.shift = convert_sh_num_to_name(shift_num)
        self.name = name
        self.rzf = rzf
        self.details = details


def convert_num_to_day(day):
    week = ["sun", "mon", "tue", "wed", "thu", 'fri', 'sat']
    return week[day]


def week(num):
    if num in [5, 6, 7]:
        return 1
    return 2


def convert_sh_num_to_name(num):
    if num == 11 or 5 == num:
        shift_name = 'morning'
    elif num == 12 or 6 == num:
        shift_name = 'evening'
    else:
        shift_name = 'night'
    return shift_name
