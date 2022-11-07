import json
from functools import reduce
from request import guard
from operator import itemgetter, attrgetter


def init(wb_write, wb_data, g_d):
    """
    refactoring : dict{guard:quality} -> guard_dict[guard_objects1,2,3,,]

    get tow xl file
    :param wb_write:
    :param wb_data:
    :return: dict quality peer guard
    """
    sheet_write = wb_write.worksheets[1]  # quality page
    names_list = wb_data.sheetnames  # list of all sheet's names in wb_data
    dict_quality = {}
    guards_dict = {}

    for i in range(len(names_list)):
        sheet_new_data = wb_data.worksheets[i]
        sum_morning = 0
        for k in [5, 11]:
            for j in range(6):
                if sheet_new_data.cell(row=k, column=3 + j).value is not None:
                    sum_morning += 1
        c2 = sheet_write.cell(row=5 + i, column=3)
        c2.value = sum_morning
        dict_quality[names_list[i]] = sum_morning

        # guards_dict[names_list[i]]=guard.Guard(names_list[i], sum_morning=sum_morning)

    suMorning = reduce(lambda x, y: x + y, dict_quality.values())
    # final_quality_dict = quality_dict(dict_quality, suMorning)
    # sort_qua(quality_dict(guards_dict, suMorning))
    return quality_dict(dict_quality, suMorning, g_d)  # guards_dict, suMorning)


def quality_dict(quality_dict, accont, g_d):
    """
    This func calculates the solution

    :param quality_dict: key = name = guard.Guard
    :param accont: sum of all mornning
    :param g_d  : the original dict of guard
    :return:
    """
    # ave = accont / guard_dict.keys()
    morning_quality_ratio = round(16000 / accont, 1)
    for grd in g_d:
        if grd not in quality_dict:
            continue
        final_qual = round(quality_dict[grd] * morning_quality_ratio)  # sum_morning -> quality
        #quality_dict[grd].quality = round_nearest_large(final_qual)
        g_d[grd].quality = round_nearest_large(final_qual)
    return g_d


def sort_qua(grd_dict):  # key=attrgetter('grade', 'age')
    # a= sorted(grd_lst,key=lambda guard: guard.quality)
    return dict(sorted(grd_dict, key=lambda guard: guard.quality))
    # return sorted(grd_lst, key=guard.Guard.religion == True, )


def round_nearest_large(x, num=25):
    return ((x + num // 2) // num) * num


def open_jsonfile():
    account = {}
    # Opening JSON file
    f = open('gurd.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    # Iterating through the json
    # list
    for name in data:
        account[name] = 0
        account[name] += len(data[name]["full_morning"])
        account[name] += len(data[name]["half_morning"])
    return account
    # Closing file
    f.close()
