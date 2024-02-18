def GeneraPiramideuno (  ) :
  numcolumnas = 5
  for i in range (numcolumnas):
      for j in range (i,numcolumnas):
        print ( " * " ,end=" ")
      print('')
  
def Main():
  
  GeneraPiramideuno() 
 
Main()