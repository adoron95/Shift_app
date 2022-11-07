from request.requst import Requst


def init(wb_write, wb_data, dict_guard):
    """
    Represent a raw table in the form of a dictionary,
    which helps to know which guards submitted requests for which day.

    Dividing the problem into sub-problems
    so that the advantage is easier to understand.
    :param wb_write:
    :param wb_data:
    :param dict_guard:
    :return:
    """
    sheet_write = wb_write.worksheets[2]  # raw page

    names_list = wb_data.sheetnames  # list of all sheet's names in wb_data
    account_per_guard = {}

    for guard in range(len(names_list)):
        if names_list[guard] not in dict_guard:
            continue
        sheet_new_data = wb_data.worksheets[guard]
        name = names_list[guard]
        # guard=name
        account_per_guard[name] = {}
        account_per_guard[name]["morning"] = copy_data(sheet_write, sheet_new_data, 4, 2, 5, dict_guard[name])
        account_per_guard[name]["morning"] += copy_data(sheet_write, sheet_new_data, 4, 9, 11, dict_guard[name])
        account_per_guard[name]["evening"] = copy_data(sheet_write, sheet_new_data, 41, 2, 6, dict_guard[name])
        account_per_guard[name]["evening"] += copy_data(sheet_write, sheet_new_data, 41, 9, 12, dict_guard[name])
        account_per_guard[name]["night"] = copy_data(sheet_write, sheet_new_data, 73, 2, 7, dict_guard[name])
        account_per_guard[name]["night"] += copy_data(sheet_write, sheet_new_data, 73, 9, 13, dict_guard[name])

    # return dict_guard
    # return sort_requ(account_per_guard)


def copy_data(sheet_write, sheet_new_data, row_wr, col_wr, row_da, guard):
    """
    copy data from request file to a uniform file
    :param sheet_write:
    :param sheet_new_data:
    :param row_wr:
    :param col_wr:
    :param row_da: shift 5,11 = mor ; 6,12= evening ; 7,13 = night.
    :param guard: guard
    :return: xl file with raw table
    """
    sum = 0
    for day in range(7):  # 0== sun, 1=mon ...
        cunt = row_wr
        cell_data = sheet_new_data.cell(row=row_da, column=3 + day)
        if cell_data.value is not None:
            # TODO לשלוח בקשות במקום סתם ערך מילוני

            rzf = 'רצף' in cell_data.value  # smaller func
            detaile = check_details(cell_data.value)

            new_re = Requst(day, row_da, guard.name, rzf, detaile)
            sum += 1
            if sheet_write.cell(row=row_wr, column=col_wr + day).value is not None:  # find blank place
                # cunt = row_wr
                while sheet_write.cell(row=cunt, column=col_wr + day).value is not None:
                    cunt += 1
            c = sheet_write.cell(row=cunt, column=col_wr + day)
            c.value = guard.name
            if day not in guard.request:
                #guard.request[day] = [row_da]
                guard.request[day] = [new_re]
            else:
                #guard.request[day].append(row_da)
                guard.request[day].append(new_re)

            # c.value = cell_data.value
    return sum


def dict_raw_table(sheet, gu_dict):
    """
    Feeds a raw table similar to an XL file only in a dict
    :param sheet:
    :param gu_dict
    :return:
    """
    wb = sheet.worksheets[2]  # raw page
    raw_dict = {}
    week_days = ["sun", 'mon', 'tue', 'wed', 'thu', 'fri', "sat"]
    for i in range(1, 3):
        for day in week_days:
            raw_dict[day + str(i)] = {}

    shifts = {'morning': 4, 'evening': 41, 'night': 73}
    col = 0
    for day in raw_dict:
        for shift in shifts:
            # raw_dict[day][shift]=[]
            a = []
            i = 0
            while wb.cell(row=shifts[shift] + i, column=2 + col).value is not None and i <= 34:
                # raw_dict[day][shift].append(wb.cell(row=shifts[shift]+i, column=2+col).value)
                guard = gu_dict[wb.cell(row=shifts[shift] + i, column=2 + col).value]
                a.append(guard)
                i += 1
            raw_dict[day][shift] = a
            # raw_dict[day][shift]=sorted(a, key=len, reverse=False)
        col += 1
        # raw_dict[day + str(i)][shift] =
    return raw_dict


def sort_raw(dic):
    return map(lambda lst: sorted(lst, key=len, reverse=True), )


def sort_requ(dic):
    return dict(sorted(dic.items(), key=lambda item: item[0][2]))


def check_details(cell):
    flag = False
    for i in cell:
        if i.isnumeric():
            flag = i
    return flag


def week(num):
    """
    calculate the week also in requst
    :param num:
    :return: week
    """
    if num in [5, 6, 7]:
        return 1
    return 2