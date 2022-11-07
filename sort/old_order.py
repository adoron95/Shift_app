import operator
import json

class order:
    """
    get id's from justes Table like the days at month,
    and change tham to names.
    It's need to order them like the constrains.
    int_size the size of days
    """

    def __init__(self, justes, gard_constraints, wishes_dict,int_size):

        self.gards_id = list(justes.table.keys())[:int_size]  # represent men need to keep in this month by justs table
        self.gards_cons = {}  # by gard_id cons per gard
        self.gards_wish = {}  # by gard_id wish per gard
        self.gards_final = {}  # id per date gard initial as 0
        self.initial_gard_cons_and_wish(gard_constraints, wishes_dict)
        self.sort_size_of()  # sort by largest const and smallest wish

    def initial_gard_cons_and_wish(self, gard_constraints, wishes_dict):
        """
        initial the dict in the gard's request according justice table
        :param gard_constraints:
        :param wishes_dict:
        :return: the request of gards
        """
        for i in self.gards_id:
            self.gards_cons[i] = gard_constraints.gard_const_dic.get(i)
            # self.gards_name.append(dict_name.name_table.get(i)) insert the name in calendar
            self.gards_wish[i] = wishes_dict.id_wish_dict.get(i)
            self.gards_final[i] = 0

    def sort_size_of(self):
        """
        sort the men by the largest const and smalest wish"""
        sort_cons_by_big_size = sorted(self.gards_cons.items(), key=operator.itemgetter(1), reverse=True)
        self.gards_cons = dict(sort_cons_by_big_size)

        sort_wish_by_small_size = sorted(self.gards_wish.items(), key=operator.itemgetter(1), reverse=False)
        self.gards_wish = dict(sort_wish_by_small_size)

    def dead_lock(self, monthDay):
        """

        :param monthDay:
        :return: list of dead lock day
        """
        flag = True
        deads_dates = []
        val = self.gards_cons.values()
        for day in monthDay:
            for i in val:
                if day not in i:
                    flag = False
                    break
            if flag == True:
                deads_dates.append(day)
                flag = False
        return deads_dates

    def __str__(self):
        return str(self.gards_final)

    def add_oneDay_to_justes_table(self,id_list,kept):
        with open("demo.json", "r+") as jsonFile:
            data = json.load(jsonFile)
            for id in data:
                if id in self.gards_id:
                    temp=data[id]
                    temp[kept]+=1

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()


