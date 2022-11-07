from order import dict_shifts as ds
from order import week


def init():
    shifts = ds.init(1)
    return {1: week.week(shifts), 2: week.week(shifts, driver=True)}
