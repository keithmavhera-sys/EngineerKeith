To_payA = (10 ** 6) - int((10/100) * (10 ** 6))
To_payB = (10 ** 6) - int((20/100) * (10 ** 6))

Credit_IsGood = True

if Credit_IsGood:
    print(f' 10% off Therefore: {To_payA}')

else:
    print(f' 20% off Therefore: {To_payB}')

    '''
        Price of a house is $1M.
If buyer has good credit,
they need to put down 10%
Otherwise

they need to put down 20%
Print the down payment//
    '''

