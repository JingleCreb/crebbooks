# Classes

class Company(object):
    '''A UK company, incorporated under the Companies Acts.'''
    
    def __init__(self):
        self.name = None
        self.number = None
        self.registered_office = None
        self.company_type = None
        self.registers = None

class RegistersCollection(object):
    '''A set of statutory books.'''
    
    def __init__(self):
        self.members = None
        self.directors = None
        self.secretaries = None
        self.directors_interests = None
        self.charges = None
        self.interests_in_shares = None

class Shareholder(object):
    '''A company shareholder.'''
    
    def __init__(self):
        self.person = None
        self.shareholdings = None

class Shareholding(object):
    '''A collection of shares of a particular class in a particular company.'''
    
    def __init__(self):
        self.company = None
        self.share_class = None
        self.number = None
        self.number_range = None
        self.nominal_value = None
        self.amount_paid_up = None
        self.date_acquired = None
        self.date_disposed = None

class Individual(object):
    '''A human.'''
    
    def __init__(self):
        self.title = None
        self.forenames = None
        self.surname = None
        self.dob = None

class Corporation(object):
    '''A body corporate.'''
    
    def __init__(self):
        self.name = None
        self.address = None

def create_company():
    '''Set up a new company'''
    
    pass
