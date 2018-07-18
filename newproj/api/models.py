class User:
   
    def __init__(self, user_id, name, username, email, password, confirmation):
        self.user_id = 0
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.confirmation = confirmation

users =[]

class Request:
       
    def __init__(self, request_id, clientname, clientcontact, clientemail, locationaddress, department, dateneeded,workassignedto, workbilledto,detailsofrequest):
        self.request_id = request_id
        self.clientname = clientname
        self.clientcontact = clientcontact
        self.clientemail= clientemail
        self.locationaddress = locationaddress
        self.department = department
        self.dateneeded = dateneeded
        self.workassignedto = workassignedto
        self.workbilledto = workbilledto
        self.detailsofrequest = detailsofrequest
       
    
    def __repr__(self):
        return repr(self.__dict__) 
        
requests = []
