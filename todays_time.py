import datetime, arrow

T = datetime.datetime.today().strftime('%Y-%m-%d')
print(T)


D = arrow.now().format('YYYY-MM-DD')
print(D)


#add change here