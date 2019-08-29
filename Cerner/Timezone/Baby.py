from datetime import datetime
import pytz


class Baby:
    def __init__(self, fname, lname, country, city, birth= None):
        self.first_name = fname
        self.last_name = lname
        self.country = country
        self.city = city
        if birth:
            self.birth = birth
        else:
            self.birth = datetime.now(pytz.utc)
    
    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

    def get_birth(self):
        return self.convert_to_timezone(self.country, self.city)
    
    def get_date_for_another_timezone(self, country, city):
        return self.convert_to_timezone(country, city)
    
    @classmethod
    def get_country_names(cls):
        country = {}
        for k, v in pytz.country_names.items():
            country[v] = [k]
        return country
    
    def convert_to_timezone(self, country, city):
        fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        countries = Baby.get_country_names()
        if country == 'United States':
            eastern = pytz.timezone('US/Eastern')
            #western = pytz.timezone('US/Pacific')
            #central = pytz.timezone('US/Central')
            #mid_west = pytz.timezone('US/Mountain')
            new_date = self.birth.astimezone(eastern)
            return new_date.strftime(fmt)
        elif country in countries:
            tz = pytz.timezone(pytz.country_timezones.get(countries[country]))
            new_date = self.birth.astimezone(tz)
            return new_date.strftime(fmt)
        else:
            return self.birth.strftime(fmt)
            


