from datetime import date as t


class Guard:
    def __init__(self, name, phone=None, quality=0, armed=False,
                 controller=False, religion=False, manager=False,achsan=False
                 , driver=False, seniority=t(year=2022, month=1, day=1),sum_morning=0):
        self.name = name
        self.phone = phone
        self.quality = quality
        self.armed = armed
        self.controller = controller  # בקר
        self.religion = religion
        self.manager = manager
        self.achsan=achsan
        self.driver = driver
        self.seniority = seniority
        self.sum_morning=sum_morning
        self.request={}

    def set_quality(self, qul):
        self.quality = qul

    #def request(self,day,req):

