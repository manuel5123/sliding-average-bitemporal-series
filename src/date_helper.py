"""
This file specifically contains date helper functions, replacing the datetime module.
"""


def date_in_n_days(date, n):
    for _ in range(n):
        date = date_next_day(date)
    return date




def date_next_day(datum1):
    """
    :param datum1: Input date, e.g. '2020-02-28'
    :return: Next day, e.g. '2020-02-29'
    """
    jahr = datum1[:4]
    monat = datum1[5:7]
    tag = datum1[-2:]
    if int(jahr)%4 == 0:
        schaltjahr = True
    else:
        schaltjahr = False
    jahr_out, monat_out, tag_out = return_date_next_day(jahr, monat, tag, schaltjahr)
    str1 = "{}-{}-{}".format(jahr_out,monat_out,tag_out)
    return str1


def return_date_next_day(jahr, monat, tag, schaltjahr):
    """
    Input: jahr, monat, tag, schaltjahr: '2020', '02', '28', True
    Output (tuple): ('2020', '02', '29')
    """
    def tag_zu_tag(str1):
        # str1 = '12' oder '02' oder '2'
        n = len(str1)
        if n == 1:
            return '0'+str1
        if n == 2:
            return str1
    if monat == '12':
        if tag == '31':
            jahr_out, monat_out, tag_out = str(int(jahr)+1), '01', '01'
        else:
            jahr_out, monat_out, tag_out = jahr, monat, tag_zu_tag(str(int(tag)+1))
    else:
        jahr_out = jahr
        if monat == '01':
            if tag == '31':
                monat_out, tag_out = '02','01'
            else:
                monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
        if monat == '02':
            if schaltjahr == True:
                if tag == '29':
                    monat_out, tag_out = '03','01'
                else:
                    monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
            else:
                if tag == '28':
                    monat_out, tag_out = '03','01'
                else:
                    monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
        if monat == '03':
            if tag == '31':
                monat_out, tag_out = '04','01'
            else:
                monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
        if monat == '04':
            if tag == '30':
                monat_out, tag_out = '05','01'
            else:
                monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
        if monat == '05':
            if tag == '31':
                monat_out, tag_out = '06','01'
            else:
                monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
        if monat == '06':
            if tag == '30':
                monat_out, tag_out = '07','01'
            else:
                monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
        if monat == '07':
            if tag == '31':
                monat_out, tag_out = '08','01'
            else:
                monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
        if monat == '08':
            if tag == '31':
                monat_out, tag_out = '09','01'
            else:
                monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
        if monat == '09':
            if tag == '30':
                monat_out, tag_out = '10','01'
            else:
                monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
        if monat == '10':
            if tag == '31':
                monat_out, tag_out = '11','01'
            else:
                monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
        if monat == '11':
            if tag == '30':
                monat_out, tag_out = '12','01'
            else:
                monat_out, tag_out = monat, tag_zu_tag(str(int(tag)+1))
    return jahr_out, monat_out, tag_out
