
class Date(object):
    def get_date(self):
        return '2019-08-04'


class Time(Date):           # Herda método a partir da classe Date().
    def get_time(self):
        return '08:11:30'


date = Date()
print(date.get_date())

time = Time()
print(time.get_time())
print(time.get_date())

