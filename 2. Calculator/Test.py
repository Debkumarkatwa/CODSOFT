while True:
    try:
        Expression = input('Enter the Problem Equation(0 for Exit): ')
        if Expression.lower() == '0':
            print('Good Bye!')
            break
        result = eval(Expression)
        print(f'{Expression} = {result}')

    except:
        print('Sorry! An Error Occcured.......')