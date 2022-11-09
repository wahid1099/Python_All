

def centerlines():
  with open('center.txt','r+') as file:
            lines=file.readlines()
            for line in lines:

                # file.write( "{0:^100}".format(line))
                #  print( "{0:^80}".format(line))
                print(line.center(100))



centerlines()
            
            