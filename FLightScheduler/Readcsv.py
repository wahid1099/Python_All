import csv

with  open('./data/currencyrates.csv','r') as file:
    lines=csv.reader(file)
    header = next(lines)
    
    for line in lines:
       if 'Bangladeshi Taka' in line:
         usd=float(line[3])
         bd=float(usd*50)
        
         resultinbdt=round(bd,3)
         resultinusd=round(5000/usd,3)
         print("50$ in Taka is:",resultinbdt)
         print("5000TK in USD is:",resultinusd)
        
        #  print("50 usd in taka is",result)
   






# homework
# convert 50 USD to BDT
# convert 5000 BDT to USD