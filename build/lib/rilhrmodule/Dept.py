class Dept:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member Dept
        self.members = ['Infra', 'Petcamp']
 
 
    def printMembers(self):
        print('Printing members of the Dept class')
        for member in self.members:
            print('\t%s ' % member)