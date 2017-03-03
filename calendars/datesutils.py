import datetime
from datetime import timedelta, date
import calendar

def add_month(sourcedate,months):
	month = sourcedate.month - 1 + months
	year = int(sourcedate.year + month / 12 )
	month = month % 12 + 1
	day = min(sourcedate.day,calendar.monthrange(year,month)[1])
	return datetime.date(year,month,day)
	
def add_months(start_date, end_date, number_of_months):
	dates = []
	cur_date= start_date
	dates.append(cur_date)
	while cur_date< end_date:
		cur_date = add_month(cur_date, 1)
		print(cur_date)
		dates.append(cur_date)
	return dates
	
def add_days(start_date, end_date, interval):
	dates = []
	cur_date= start_date
	dates.append(cur_date)
	while cur_date< end_date:
		cur_date += datetime.timedelta(days=interval)
		dates.append(cur_date)
	return dates

def daterange(start_date, end_date, interval_type, interval):
	cur_date = start_date
	dates=[]
	dates.append(start_date)
	print (interval_type)
	if (interval_type == 'week'):
		interval = interval *7
		dates = add_days(start_date, end_date, interval)
	elif (interval_type == 'day'):
		dates = add_days(start_date, end_date, interval)
	elif interval_type == 'month':
		dates = add_months(start_date, end_date, interval)
	
	return dates
start_date = date(2013, 1, 1)
end_date = date(2015, 6, 2)
print (daterange(start_date, end_date, 'month', 1))