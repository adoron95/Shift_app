from sort import sorce
def sort_night(dict_req, two_weeks):

    for i in dict_req:

        lis = i.split('_')
        day, week, shif = lis[0], lis[1], lis[2]
        part_shifts = two_weeks[int(week)][day][shif].shift
        if len(dict_req[i]) <= len(part_shifts):  # len of req guard
            part_shifts_keys=list(part_shifts.keys())
            k=0
            for men in dict_req[i]:
                if dict_req[i][men].quality >= two_weeks[int(week)][day][shif].quality:
                    #a=part_shifts_keys[k]   #position name
                    position=part_shifts.get(part_shifts_keys[k])
                    z= position._dict_
                    posi_demand= find_posi_demand(position)
                    if position=="achmash":
                        #TODO
                        #find_achmash()
                        b=1
                    part_shifts[position].set_guard(men)
                    k+=1
        else:
            for s in part_shifts:
                if part_shifts[s].achmash:
                    check_rzf(day,week,dict_req)
                    check_quality()
                    check_last_shift()
                    sort_achmash_night(dict_req[i], part_shifts[s].achmash)
    position=1
def sort_achmash_night(dic_name, shift):
    """
    :return  מחזיר רק אחמש ואם אין אחמש אז אחסן ואם לא וותק
    :param dic_name:
    :param shift:
    :return:
    """
   # sorce.sort_by_role(dic_name)
    a=1

def check_rzf(day,week,dict_req):
    days = ["sun", "mon", "tue", "wed", "thu", 'fri', 'sat']
    yasterday=days[days.index(day)-1]


def find_posi_demand(position):
    if position.achmash==True:
        aa=1
