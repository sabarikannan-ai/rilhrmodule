import logging 

class Employee:
    def __init__(self):
        #logging.basicConfig(filename="newfile.log", 
                    #format='%(asctime)s %(message)s', 
                    #filemode='w') 
  
        #logger=logging.getLogger() 
        ''' Constructor for this class. '''
        # Create some member employee
        self.members = ['Sab', 'Kannan']
 
 
    def printMembers(self):
        #self.members = ['Sab', 'Kannan']
        #logger=logging.getLogger() 
        #logger.info("Just an information") 
        print('Printing members of the employee class')
        for member in self.members:
            print('\t%s ' % member)