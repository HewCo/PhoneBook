pn = {
    'Amal': '1111111111',
    'Mohammed': '2222222222' ,
    'Khadijah': '3333333333',
    'Abdullah': '4444444444',
    'Rawan': '5555555555',
    'Faisal': '6666666666',
    'Layla': '7777777777'
}
nameOrnumber = input('Do you want to search by name or number? ')
if nameOrnumber == 'name' or nameOrnumber == 'Name':
    name = input('Name:')

    pn.get(name)
    if pn.get(name) == None:
        print('Name Does NOT Exist! ')

    else:
        print(name, 'Number is: ', pn[name])
        print('Thank you for using our program!')

    if pn.get(name) == None:
        newName = input('Do You Want to Add a New Name? ')
        if (newName == 'yes') or  (newName == 'Yes'):
            addNewname = input('Type the New Name Here: ')
            pn.get(addNewname)
            if pn.get(addNewname) == None:
                newPn = input('Type the Phone Number Here: ')
                if len(newPn) != 10:
                    print('The Number is Invalid')
                    print('Thank you for using our program!')
                else:
                    pn[addNewname] = newPn
                    print('the name', addNewname, 'with the number', newPn, 'was added!')
                    print('Thank you for using our program!')
            else:
                print('Name Already Exists!')
                print('Thank you for using our program!')

        else:
            print('Thank you for using our program!')
elif nameOrnumber == 'number' or nameOrnumber == 'Number':
    number = input('Number: ')
    if number in pn.values():
        for esm, r8m in pn.items():
            if number == r8m:
                print(number, 'is', esm, 'number')
                print('Thank you for using our program!')

    else:
        print('Number does NOT Exist! ')
        newNumber = input('Do you want to add a new number? ')
        if newNumber == 'yes' or newNumber == 'Yes':
            addNewNumber = input('Type New Number Here: ')
            if addNewNumber in pn.values():
                print('Number Already Exists!')

            else:
                newName = input('Type the name here: ')
                pn[newName] = addNewNumber
                print('the number', addNewNumber, 'for', newName, 'was added!')
                print('Thank you for using our program!')

