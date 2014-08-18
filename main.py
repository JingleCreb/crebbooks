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
        self.shareholders = None
        self.directors = None
        self.secretaries = None
        self.directors_interests = None
        self.charges = None
        self.interests_in_shares = None

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
