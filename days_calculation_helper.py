def day_calculation(year_1, month_1, day_1, year_2, month_2, day_2):
    leap_year = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    common_year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 'unfit'

    if month_1 > 12 or month_2 > 12 or month_1 <= 0 or month_2 <= 0 or year_1 <= 0 or day_1 <= 0 or year_2 <= 0 or day_2 <= 0:
        result = 'unfit'

    elif year_1 % 4 == 0 and day_1 > leap_year[month_1] or year_2 % 4 == 0 and day_2 > leap_year[
        month_2] or year_1 % 4 != 0 and day_1 > common_year[month_1] or year_2 % 4 != 0 and day_2 > common_year[
        month_2]:
        result = 'unfit'

    elif year_1 % 4 == 0 and year_2 % 4 == 0:
        sum_1 = (year_1 - 1) * 365 + (year_1 - 1) // 4 + sum(leap_year[0:month_1]) + day_1
        sum_2 = (year_2 - 1) * 365 + (year_2 - 1) // 4 + sum(leap_year[0:month_2]) + day_2
        difference = abs(sum_1 - sum_2)
        result = difference

    elif year_1 % 4 == 0 and year_2 % 4 != 0:
        sum_1 = (year_1 - 1) * 365 + (year_1 - 1) // 4 + sum(leap_year[0:month_1]) + day_1
        sum_2 = (year_2 - 1) * 365 + (year_2 - 1) // 4 + sum(common_year[0:month_2]) + day_2
        difference = abs(sum_1 - sum_2)
        result = difference

    elif year_1 % 4 != 0 and year_2 % 4 == 0:
        sum_1 = (year_1 - 1) * 365 + (year_1 - 1) // 4 + sum(common_year[0:month_1]) + day_1
        sum_2 = (year_2 - 1) * 365 + (year_2 - 1) // 4 + sum(leap_year[0:month_2]) + day_2
        difference = abs(sum_1 - sum_2)
        result = difference

    elif year_1 % 4 != 0 and year_2 % 4 != 0:
        sum_1 = (year_1 - 1) * 365 + (year_1 - 1) // 4 + sum(common_year[0:month_1]) + day_1
        sum_2 = (year_2 - 1) * 365 + (year_2 - 1) // 4 + sum(common_year[0:month_2]) + day_2
        difference = abs(sum_1 - sum_2)
        result = difference

    return result
