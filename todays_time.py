import datetime, arrow

T = datetime.datetime.today().strftime('%Y-%m-%d')
print(T)


D = arrow.now().format('YYYY-MM-DD')
print(D)


#add change here
x = 1
y = 2
z = (3x+1)-y
print(z)