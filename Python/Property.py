class TestProperty(object):
    def __init__(self,name):
        self.name=name
    def _set_name(self,name):
        print("Setting name")
        self.name = name
    def _get_name(self,name):
        print("Getting Name ")
        return self.name
    name = property(_get_name,_set_name)
    
                    
    
    
    
    
                
