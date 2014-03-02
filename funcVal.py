#functions for validating user input

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month (month):
	if month:
		short_month = month[:3].lower()
		return month_abbvs.get(short_month)

# print valid_month('jan')
# print valid_month('asdfsdf1')


def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if 1 <= day <= 31:
			return day


# print valid_day('15')
# print valid_day('sd')
# print valid_day('31')
# print valid_day('1512')

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year > 1900 and year < 2020:
			return year

# print valid_year('1900')
# print valid_year('1912')
# print valid_year('2021')