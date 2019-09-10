
class Date(object):
    def get_date(self):
        return '2019-08-04'


class Time(Date):           # Herda método a partir da classe Date().
    def get_time(self):
        return '08:11:30'


data = Date()
print(data.get_date())

tempo = Time()
print(tempo.get_time())
print(tempo.get_date())

