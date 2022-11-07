from order import shift as sh


def week(shifts,driver=False):
    dict_week = {}
    for i in ["sun", "mon", "tue", "wed", "thu"]:
        dict_week[i] = day(shifts['morning'], shifts['evening'], shifts['night'])

    dict_week["fri"] = day(shifts['friday_morning'], shifts['friday_evening'],
                           shifts['night'], quality_night=300)

    dict_week["sat"] = day(shifts['saturday_morning'], shifts['saturday_evening'],
                           shifts['saturday_night'], quality_night=300,
                           quality_evening=250, quality_mor=250)
    if driver:
        dict_week['sat']['driver']=sh.Shift(shifts['driver'], qulity=375)

    return dict_week


def day(morning, dic_sh_eve, dic_sh_night,
        quality_mor=100, quality_evening=100, quality_night=150):
    return {'morning': sh.Shift(morning, qulity=quality_mor),
            'evening': sh.Shift(dic_sh_eve, qulity=quality_evening),
            'night': sh.Shift(dic_sh_night, qulity=quality_night)}
