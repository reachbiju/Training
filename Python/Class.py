class A(object):
    
    #print ("Now its %s" %str(datetime.now() )) 
    
    def __init__(self,name):
        
        self.name=name
        
        #str(datetime.now() ) ) 
        
    def show(self): #Self refrence the current object
        from datetime import datetime
        print('The object  {0} was created  on at {1}   '.format( self.name, str(datetime.now() ) ) )
        

a = A("Biju Oommen")
a.show()



    