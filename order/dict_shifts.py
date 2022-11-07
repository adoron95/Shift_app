from order.part_shift import PartShift as ps
from datetime import timedelta as t

"""
singleton factory 
"""
sixfortyfive_am = t(hours=6, minutes=45)
six_fifty_am = t(hours=6, minutes=50)
six_fifty_five_am = t(hours=6, minutes=55)
seven_am = t(hours=7)
seven_twenty_am = t(hours=7, minutes=20)
eight_am = t(hours=8)
eight_quarter_am = t(hours=8, minutes=15)
nine_am = t(hours=9)
eleven_am = t(hours=11)
two_pm = t(hours=14)
two_fifty_pm = t(hours=14, minutes=50)
three_pm = t(hours=15)
five_pm = t(hours=17)
six_pm = t(hours=18)
seven_pm = t(hours=19)
seven_helf_pm = t(hours=19, minutes=30)
eleven_pm = t(hours=23)


def init(size):
    sh_di = {'morning': ctr_morning(size),
             'evening': ctr_evening(size),
             'night': ctr_night(),
             'friday_morning': ctr_fri_mor(),
             'friday_evening': ctr_fri_eve(),
             'saturday_morning': ctr_sat_mor(),
             'saturday_evening': ctr_sat_eve(),
             'saturday_night': ctr_sat_night(),
             'driver': ctr_driver()
             }
    return sh_di


def ctr_driver():
    driver = {}
    driver['achmash'] = ps(eleven_pm, nine_am, full=True)
    return driver


def ctr_sat_night():
    sat_night = ctr_night()

    sat_night['shnhav1'] = ps(eleven_pm, seven_am, full=True)
    sat_night['shnhav2'] = ps(eleven_pm, seven_am, full=True)
    return sat_night


def ctr_sat_eve():
    sat_evening = ctr_fri_eve()
    sat_evening['shalom_4'] = ps(six_pm, t(hours=23, minutes=59), semi2=True)
    return sat_evening


def ctr_sat_mor():
    sat_morning = {}
    sat_morning['achmash'] = ps(sixfortyfive_am, three_pm, achmash=True, full=True)
    sat_morning['achsan'] = ps(sixfortyfive_am, three_pm, full=True)
    sat_morning['zos'] = ps(sixfortyfive_am, three_pm, armed=True, full=True)
    return sat_morning


def ctr_fri_eve():
    fri_evening = {}
    fri_evening['achmash'] = ps(two_fifty_pm, eleven_pm, achmash=True, full=True)
    fri_evening['shalom_1'] = ps(three_pm, eleven_pm, full=True)
    fri_evening['shalom_2'] = ps(three_pm, eleven_pm, full=True)
    fri_evening['shalom_3'] = ps(three_pm, eleven_pm, full=True)
    return fri_evening


def ctr_fri_mor():
    fri_morning = {}
    fri_morning['achmash'] = ps(sixfortyfive_am, three_pm, achmash=True, full=True)
    fri_morning['achsan'] = ps(sixfortyfive_am, three_pm, full=True)
    fri_morning['zos'] = ps(seven_am, two_pm, armed=True, full=True)
    fri_morning['door'] = ps(eight_am, three_pm, full=True)
    fri_morning['library'] = ps(eight_am, three_pm, full=True)
    fri_morning['chshin6_1'] = ps(eight_am, three_pm, full=True)
    fri_morning['chshin6_2'] = ps(eight_am, three_pm, full=True)
    fri_morning['chshin6_3'] = ps(eight_quarter_am, three_pm, semi2=True)
    fri_morning['chshin6_4'] = ps(eight_quarter_am, three_pm, semi2=True)
    return fri_morning


def ctr_night():
    night = {}
    night['achmash'] = ps(two_fifty_pm, seven_am, achmash=True, full=True)
    night['court'] = ps(eleven_pm, seven_am, full=True)
    night['shalom'] = ps(eleven_pm, seven_am, full=True)
    night['empire'] = ps(eleven_pm, seven_am, full=True)
    return night


def ctr_evening(size):
    evening = {}
    evening['achmash'] = ps(two_fifty_pm, eleven_pm, achmash=True, full=True)
    evening['shalom_1'] = ps(three_pm, eleven_pm, full=True)
    evening['shalom_2'] = ps(three_pm, eleven_pm, full=True)
    evening['shalom_3'] = ps(three_pm, eleven_pm, full=True)
    evening['shalom_4'] = ps(three_pm, eleven_pm, full=True)
    evening['shalom_5'] = ps(three_pm, five_pm, semi1=True)
    evening['shalom_6'] = ps(three_pm, seven_helf_pm, semi1=True)
    evening['chshin_1'] = ps(two_fifty_pm, seven_pm, controler=True, armed=True, semi1=True)
    evening['chshin_2'] = ps(three_pm, eleven_pm, controler=True, armed=True, full=True)
    evening['local'] = ps(two_fifty_pm, seven_pm, armed=True, controler=True, semi1=True)
    return evening


def ctr_morning(size):
    morning = {}
    morning['achmash'] = ps(sixfortyfive_am, three_pm, achmash=True, full=True)
    morning['achsan'] = ps(sixfortyfive_am, three_pm, achsan_shift=True, full=True)
    morning['zos'] = ps(six_fifty_five_am, three_pm, armed=True, full=True)
    morning['door'] = ps(six_fifty_am, three_pm, full=True)
    morning['library'] = ps(six_fifty_am, three_pm, full=True)
    morning['chshin6_1'] = ps(seven_twenty_am, three_pm, full=True)
    morning['chshin6_2'] = ps(seven_twenty_am, three_pm, full=True)
    morning['chshin6_3'] = ps(nine_am, three_pm, semi2=True)
    morning['chshin6_4'] = ps(eleven_am, three_pm, semi2=True)

    morning['chshin1_1'] = ps(sixfortyfive_am, three_pm, controler=True, full=True)
    morning['chshin1_2'] = ps(seven_twenty_am, three_pm, controler=True, full=True)
    morning['chshin1_3'] = ps(seven_twenty_am, three_pm, full=True)
    morning['chshin1_4'] = ps(seven_twenty_am, three_pm, full=True)
    morning['chshin1_5'] = ps(seven_twenty_am, three_pm, full=True)
    morning['chshin1_6'] = ps(seven_twenty_am, three_pm, full=True)

    morning['local_1'] = ps(sixfortyfive_am, three_pm, controler=True, full=True)
    morning['local_2'] = ps(seven_twenty_am, three_pm, controler=True, full=True)
    morning['local_3'] = ps(seven_twenty_am, three_pm, full=True)
    morning['local_4'] = ps(seven_twenty_am, three_pm, full=True)
    return morning
