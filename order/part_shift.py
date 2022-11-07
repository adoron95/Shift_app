class PartShift:
    """

    """

    def __init__(self, beg_time,end_time, armed=False, achmash=False, achsan_shift=False, controler=False,
                 full=False, semi1=False, semi2=False, driver_shift=False):
        # self.day_at_week = day # deleted

        self.beg_time = beg_time
        self.end_time = end_time

        self.arme = armed
        self.controler = controler  # בקר
        self.achmash = achmash
        self.achsan = achsan_shift
        self.full_shift = full
        self.semi_shift_1 = semi1
        self.semi_shift_2 = semi2
        self.driver = driver_shift
        self.guard = None

    def set_guard(self, guard):
        self.guard = guard  # .append(guard)


    def __repr__(self):
        return self


def func():
    a = 1
