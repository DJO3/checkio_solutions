"""
Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.

Input: Year as an integer.

Output: Number of Black Fridays in the a year as an integer.

Example:

checkio(2015) == 3
checkio(1986) == 1
1
2
Precondition: 1000 < |year| < 3000
"""

def checkio(year):
    import calendar

    # If the month starts on a Sunday, there will be a Friday the 13th
    first_sundays = 0
    for month in range(1, 13):
        calendar.setfirstweekday(calendar.SUNDAY)
        c = calendar.monthcalendar(year, month)
        first_day = c[0][0]
        first_sundays += first_day
    return first_sundays
