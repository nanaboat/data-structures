import requests

class Emaildata:
    def __init__(self, user, data, page='first'):
        self.user = user
        self.body = data
        self.page = page
    
    def show(self):
        results = "user: {}  page_id: {}  email_content: {}".format(self.user, self.page, self.body)
        print(results)
            


class Processdata:
    def __init__(self, url):
        self.data = requests.get(url).json()
        
    def process_email_data(self):
        email_data = []
        for obj in self.data['emails']:
            email_data.append(obj['gibberish'])
        return email_data
    
    def get_next_page(self):
        return self.data.get('next_page', None)
    
    def get_emails(self, user, page, data):
        emails = []
        for info in data:
            emails.append(Emaildata(user, info, page))
        return emails
    
if __name__ == "__main__":
    url = "http://interview.armorblox.io/api/mails?user={}&next_page={}"
    users = ['prince', 'randy']
    email_list = []
    for user in users:
        page = ''
        end = False
        while not end:
            email_p = Processdata(url.format(user, page))
            email_data = email_p.process_email_data()
            page = email_p.get_next_page()
            if page == '':
                page = 'first'
            elif not page:
                page = 'last'
                end = True
            email_list += email_p.get_emails(user, page, email_data)
    
    for email in email_list:
        email.show()