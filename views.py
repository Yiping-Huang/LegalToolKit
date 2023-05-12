from django.shortcuts import render

# Create your views here.
from legal_toolkit.days_calculation_helper import day_calculation


def days_calculator(request):
    """ Calculate the days between two dates. """
    a_check = 0
    b_check = 0
    c_check = 0
    d_check = 0
    e_check = 0
    a_result = 0
    b_result = 0
    c_result = 0
    d_result = 0
    e_result = 0
    result = "You have not submitted data yet."

    if request.POST.get('Ayear_1') and request.POST.get('Amonth_1') and request.POST.get('Aday_1') and request.POST.get(
            'Ayear_2') and request.POST.get('Amonth_2') and request.POST.get('Aday_2'):
        Ayear_1 = int(request.POST.get('Ayear_1'))
        Amonth_1 = int(request.POST.get('Amonth_1'))
        Aday_1 = int(request.POST.get('Aday_1'))
        Ayear_2 = int(request.POST.get('Ayear_2'))
        Amonth_2 = int(request.POST.get('Amonth_2'))
        Aday_2 = int(request.POST.get('Aday_2'))
        a_check = 1
        a_result = day_calculation(Ayear_1, Amonth_1, Aday_1, Ayear_2, Amonth_2, Aday_2)

    if request.POST.get('Byear_1') and request.POST.get('Bmonth_1') and request.POST.get('Bday_1') and request.POST.get(
            'Byear_2') and request.POST.get('Bmonth_2') and request.POST.get('Bday_2'):
        Byear_1 = int(request.POST.get('Byear_1'))
        Bmonth_1 = int(request.POST.get('Bmonth_1'))
        Bday_1 = int(request.POST.get('Bday_1'))
        Byear_2 = int(request.POST.get('Byear_2'))
        Bmonth_2 = int(request.POST.get('Bmonth_2'))
        Bday_2 = int(request.POST.get('Bday_2'))
        b_check = 1
        b_result = day_calculation(Byear_1, Bmonth_1, Bday_1, Byear_2, Bmonth_2, Bday_2)

    if request.POST.get('Cyear_1') and request.POST.get('Cmonth_1') and request.POST.get('Cday_1') and request.POST.get(
            'Cyear_2') and request.POST.get('Cmonth_2') and request.POST.get('Cday_2'):
        Cyear_1 = int(request.POST.get('Cyear_1'))
        Cmonth_1 = int(request.POST.get('Cmonth_1'))
        Cday_1 = int(request.POST.get('Cday_1'))
        Cyear_2 = int(request.POST.get('Cyear_2'))
        Cmonth_2 = int(request.POST.get('Cmonth_2'))
        Cday_2 = int(request.POST.get('Cday_2'))
        c_check = 1
        c_result = day_calculation(Cyear_1, Cmonth_1, Cday_1, Cyear_2, Cmonth_2, Cday_2)

    if request.POST.get('Dyear_1') and request.POST.get('Dmonth_1') and request.POST.get('Dday_1') and request.POST.get(
            'Dyear_2') and request.POST.get('Dmonth_2') and request.POST.get('Dday_2'):
        Dyear_1 = int(request.POST.get('Dyear_1'))
        Dmonth_1 = int(request.POST.get('Dmonth_1'))
        Dday_1 = int(request.POST.get('Dday_1'))
        Dyear_2 = int(request.POST.get('Dyear_2'))
        Dmonth_2 = int(request.POST.get('Dmonth_2'))
        Dday_2 = int(request.POST.get('Dday_2'))
        d_check = 1
        d_result = day_calculation(Dyear_1, Dmonth_1, Dday_1, Dyear_2, Dmonth_2, Dday_2)

    if request.POST.get('Eyear_1') and request.POST.get('Emonth_1') and request.POST.get('Eday_1') and request.POST.get(
            'Eyear_2') and request.POST.get('Emonth_2') and request.POST.get('Eday_2'):
        Eyear_1 = int(request.POST.get('Eyear_1'))
        Emonth_1 = int(request.POST.get('Emonth_1'))
        Eday_1 = int(request.POST.get('Eday_1'))
        Eyear_2 = int(request.POST.get('Eyear_2'))
        Emonth_2 = int(request.POST.get('Emonth_2'))
        Eday_2 = int(request.POST.get('Eday_2'))
        e_check = 1
        e_result = day_calculation(Eyear_1, Emonth_1, Eday_1, Eyear_2, Emonth_2, Eday_2)

    if a_check + b_check + c_check + d_check + e_check == 0:
        result = "You have not submitted any data yet."

    if a_check + b_check + c_check + d_check + e_check >= 1:
        if a_result == 'unfit' or b_result == 'unfit' or c_result == 'unfit' or d_result == 'unfit' or e_result == 'unfit':
            result = "You have some required fields left unfilled"
        else:
            result = "There are " + str(a_result + b_result + c_result + d_result + e_result) + " days in total."

    context = {'result': result}
    return render(request, 'legal_toolkit/days_calculator.html', context)


def date_calculator(request):
    """ Infer the date after or between certain days. """
    check_1 = 0
    check_2 = 0
    leap_year = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    common_year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result_1 = ""
    result_2 = ""

    if request.POST.get('year_1') and request.POST.get('month_1') and request.POST.get('day_1') and request.POST.get(
            'interval_1'):
        check_1 = 1
        year_1 = int(request.POST.get('year_1'))
        month_1 = int(request.POST.get('month_1'))
        day_1 = int(request.POST.get('day_1'))
        interval_1 = int(request.POST.get('interval_1'))
        ini_interval_1 = interval_1
        ini_result_1 = str(year_1) + "/" + str(month_1) + "/" + str(day_1)
        year_3 = year_1
        month_3 = month_1
        day_3 = day_1 + interval_1

        if month_1 > 12 or month_1 <= 0 or year_1 <= 0 or day_1 <= 0:
            result_1 = "You have submitted improper data!"

        elif year_1 % 4 == 0 and day_1 > leap_year[month_1] or year_1 % 4 != 0 and day_1 > common_year[month_1]:
            result_1 = "You have submitted improper data!"

        else:
            while interval_1 > 0:
                if month_3 < 12 and year_3 % 4 != 0 and day_3 > common_year[month_3]:
                    day_3 = day_3 - common_year[month_3]
                    month_3 = month_3 + 1
                    interval_1 = day_3
                    continue

                if month_3 < 12 and year_3 % 4 == 0 and day_3 > leap_year[month_3]:
                    day_3 = day_3 - leap_year[month_3]
                    month_3 = month_3 + 1
                    interval_1 = day_3
                    continue

                if month_3 == 12 and year_3 % 4 != 0 and day_3 > common_year[month_3]:
                    day_3 = day_3 - common_year[month_3]
                    month_3 = 1
                    year_3 = year_3 + 1
                    interval_1 = day_3
                    continue

                if month_3 == 12 and year_3 % 4 == 0 and day_3 > leap_year[month_3]:
                    day_3 = day_3 - leap_year[month_3]
                    month_3 = 1
                    year_3 = year_3 + 1
                    interval_1 = day_3
                    continue

                else:
                    interval_1 = 0
                    break

            result_1 = str(ini_interval_1) + " days after " + ini_result_1 + " is " + str(
                year_3) + "/" + str(month_3) + "/" + str(day_3) + "."

    if request.POST.get('year_2') and request.POST.get('month_2') and request.POST.get('day_2') and request.POST.get(
            'interval_2'):
        check_2 = 1
        year_2 = int(request.POST.get('year_2'))
        month_2 = int(request.POST.get('month_2'))
        day_2 = int(request.POST.get('day_2'))
        interval_2 = int(request.POST.get('interval_2'))
        ini_interval_2 = interval_2
        ini_result_2 = str(year_2) + "/" + str(month_2) + "/" + str(day_2)
        year_4 = year_2
        month_4 = month_2
        day_4 = day_2 - interval_2

        if month_2 > 12 or month_2 <= 0 or year_2 <= 0 or day_2 <= 0:
            result_2 = "You have submitted improper data!"

        elif year_2 % 4 == 0 and day_2 > leap_year[month_2] or year_2 % 4 != 0 and day_2 > common_year[month_2]:
            result_2 = "You have submitted improper data!"

        else:
            while interval_2 > 0:
                if month_4 > 1 and year_4 % 4 != 0 and day_4 < 0:
                    month_4 = month_4 - 1
                    day_4 = day_4 + common_year[month_4]
                    interval_2 = abs(day_4)
                    continue

                if month_4 > 1 and year_4 % 4 == 0 and day_4 < 0:
                    month_4 = month_4 - 1
                    day_4 = day_4 + leap_year[month_4]
                    interval_2 = abs(day_4)
                    continue

                if month_4 == 1 and year_4 % 4 != 0 and day_4 < 0:
                    month_4 = 12
                    day_4 = day_4 + common_year[month_4]
                    year_4 = year_4 - 1
                    interval_2 = abs(day_4)
                    continue

                if month_4 == 1 and year_4 % 4 == 0 and day_4 < 0:
                    month_4 = 12
                    day_4 = day_4 + leap_year[month_4]
                    year_4 = year_4 - 1
                    interval_2 = abs(day_4)
                    continue

                else:
                    interval_2 = 0
                    break

            result_2 = str(ini_interval_2) + " days before " + ini_result_2 + " is " + str(
                year_4) + "/" + str(month_4) + "/" + str(day_4) + "."

    if check_1 + check_2 == 0:
        result_1 = "You have not submitted complete data yet."
        result_2 = ""

    if check_1 == 1 and check_2 == 0:
        result_2 = ""

    if check_1 == 0 and check_2 == 1:
        result_1 = ""

    context = {'result_1': result_1, 'result_2': result_2}
    return render(request, 'legal_toolkit/date_calculator.html', context)


def sls_calculator(request):
    """ count the salary for sick leave"""
    result = "您尚未输入完整数据！You have not submitted complete data yet!"

    if request.POST.get('method_1') and request.POST.get('method_2') and request.POST.get(
            'salary') and request.POST.get('day'):
        result = "您不可同时选择两种计算方法！You cannot choose two methods at the same time!"

    if request.POST.get('method_1') and request.POST.get('salary') and request.POST.get('day'):
        salary = int(request.POST.get('salary'))
        day = int(request.POST.get('day'))
        if salary == 0 or day == 0:
            result = "您输入了不合适的数据！You have submitted improper data!"
        else:
            sickleavesalary = day * salary / 21.75
            ini_result = round(sickleavesalary, 2)
            result = "该员工当月病假工资应为 " + str(ini_result) + \
                     " 元。 The sick leave salary of this worker is " + str(ini_result) + "CNY."

    if request.POST.get('method_2') and request.POST.get('salary') and request.POST.get('day'):
        salary = int(request.POST.get('salary'))
        day = int(request.POST.get('day'))
        if salary == 0 or day == 0:
            result = "您输入了不合适的数据！You have submitted improper data!"
        else:
            sickleavesalary = salary - day * salary / 21.75
            ini_result = round(sickleavesalary, 2)
            result = "该员工当月病假工资应为 " + str(ini_result) + \
                     " 元。 The sick leave salary of this worker is " + str(ini_result) + " CNY."

    if request.POST.get('method_1') and request.POST.get('method_2') and request.POST.get(
            'salary') and request.POST.get('day'):
        result = "您不可同时选择两种计算方法！You cannot choose two methods at the same time!"

    context = {'result': result}
    return render(request, 'legal_toolkit/sls_calculator.html', context)


def ect_calculator(request):
    """Show the result of the calculation."""
    ecocom = ""
    avginc = ""
    process = ""
    result = ""
    show = False

    if request.POST.get('ectext') and request.POST.get('aitext'):
        ecocom = request.POST.get('ectext')
        avginc = request.POST.get('aitext')
        gap = int(ecocom) - int(avginc) * 3
        show = True
        if gap <= 0:
            process = "该劳动者的经济补偿金免征个人所得税 Exemption from individual income tax on the economic compensation of this " \
                      "worker "
            result = "0"
        elif 0 < gap <= 36000:
            pro_result = gap * 0.03
            process = "( " + str(ecocom.ectext) + " - " + str(avginc.aitext) + "*3 ) * 3% = " + str(pro_result) + " 元"
            result = str(pro_result)
        elif 36000 < gap <= 144000:
            pro_result = gap * 0.1 - 2520
            process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 10% - 2520 = " + str(pro_result) + " 元"
            result = str(pro_result)
        elif 144000 < gap <= 300000:
            pro_result = gap * 0.2 - 16920
            process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 20% -16920 = " + str(pro_result) + " 元"
            result = str(pro_result)
        elif 300000 < gap <= 420000:
            pro_result = gap * 0.25 - 31920
            process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 25% -31920 = " + str(pro_result) + " 元"
            result = str(pro_result)
        elif 420000 < gap <= 660000:
            pro_result = gap * 0.3 - 52920
            process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 30% -52920 = " + str(pro_result) + " 元"
            result = str(pro_result)
        elif 660000 < gap <= 960000:
            pro_result = gap * 0.35 - 85920
            process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 35% -85920 = " + str(pro_result) + " 元"
            result = str(pro_result)
        elif gap > 960000:
            pro_result = gap * 0.40 - 181920
            process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 40% -181920 = " + str(pro_result) + " 元"
            result = str(pro_result)

    context = {'ecocom': ecocom, 'avginc': avginc, 'process': process,
               'result': result, 'show': show}
    return render(request, 'legal_toolkit/ect_calculator.html', context)
