from sort import night
from operator import itemgetter, attrgetter

def init(raw, quality,  two_weeks):
    dict_only_high_qual = only_high_quality(raw, two_weeks)
    convert(dict_only_high_qual, quality)

    sort = False

    while not sort:
        night.sort_night(sort_by_values_len(dict_only_high_qual), two_weeks)
        #sort_only_high_qual()


def sort_by_values_len(dict):
    """
    sorted dict by smallest len(guards)
    :param dict: shifts with guards
    :return: new dict sorted by len
    """
    test_dict_list = sorted(list(dict.items()), key=lambda key: len(key[1]))
    # reordering to dictionary
    res = {ele[0]: ele[1] for ele in test_dict_list}
    return res

def sort_by_role(re):
    st=list(re)
    return sorted(re, key=attrgetter('controler'), reverse=True)


def convert(dic, guards):
    """
    convert the key in dic from num to name
    :param dic:
    :param guards:
    :return:
    """
    for shift in dic:
        new_list = {}
        for i in dic[shift]:
            new_list[i.name] = guards[i.name]
        dic[shift] = new_list


def only_high_quality(raw, two_weeks):
    """
    filter onky high quality shift
    :param raw:
    :param two_weeks:
    :return:
    """
    d = {}
    for week in two_weeks:
        for day in two_weeks[week]:
            for shift in two_weeks[week][day]:
                if two_weeks[week][day][shift].quality > 100:
                    if shift != 'driver':
                        d[str(day) + '_' + str(week) + '_' + str(shift)] = raw[str(day) + str(week)][shift]
                    # else:
                    # d[str(day) + str(week)] = shift
    return d
