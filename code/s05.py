# product cost $100 how much tax do we pay 

product = 100 
tax_rate= 0.0625
paid= product*tax_rate 
#print (f'you pay ${paid} in tax')

#more usable, make it into a function with parameters 
def tax_calcualtor(prod_price, tax, state_fee ): 
    """calculate prouct tax based on input price and tax rate. 
    if there is an additional state fee bool (true/false), an extra 10% is added to tax rate"""
    if (state_fee == True):
            tax+=0.10
    paid= prod_price*tax  
    #print (f'you pay ${paid} in tax')
    return paid # will return none as not explictly defined what to return.  

#store the value retrieved from the calculator 
stored = tax_calcualtor(97375, 0.3, True)
print (stored)


"""here i'm experimenting with a more streamlined approach to products and prices """
Products = ['Computer', 'phone', 'headphones']
Prices = [700.20, 200, 80.99]
state_tax = 0.08
fee = False

"""i learned about range for loop syntax in pyton from lse, 
len() retrieves the number of places in an array. 
i is the index or placement of each product and their appropirate prices """
for i in range(len(Products)):
    tax = tax_calcualtor(Prices[i], state_tax, fee)
    print(f'you bought {Products[i]} for ${Prices[i]} and paid ${tax} in tax')
