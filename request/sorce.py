import openpyxl

from request import quality_table as q_t
from request import raw_table as r_t


def init(guard_dict):
    data_path = "Blank inlay format.xlsx"
    write_path = "new format.xlsx"
    wb_write = openpyxl.load_workbook(data_path)
    wb_data = openpyxl.load_workbook(write_path)

    #quality_dict = q_t.init(wb_write, wb_data,guard_dict)
    r_t.init(wb_write, wb_data, q_t.init(wb_write, wb_data,guard_dict))  # q_t.init(wb_write, wb_data,guard_dict))
    #account_shifts_dict = r_t.init(wb_write, wb_data,quality_dict)#q_t.init(wb_write, wb_data,guard_dict))

    raw_dict =r_t.dict_raw_table(wb_write,guard_dict)#quality_dict)

    #wb_write.save("request\lank inlay format.xlsx") #  נועד כדי להראות את הטבלה הגולמית בקובץ xl
    return guard_dict,raw_dict
    #return r_t.init(wb_write, wb_data), q_t.init(wb_write, wb_data), r_t.dict_raw_table(wb_write)
