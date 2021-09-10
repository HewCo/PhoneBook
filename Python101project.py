pn = {
    'Amal': '1111111111',
    'Mohammed': '2222222222' ,
    'Khadijah': '3333333333',
    'Abdullah': '4444444444',
    'Rawan': '5555555555',
    'Faisal': '6666666666',
    'Layla': '7777777777'
}
options = input('Welcome! \ntype 1 to search by number \ntype 2 to search by name \ntype 3 to add a new number \n:')

if options == '2':
        name = input('Name:')

        pn.get(name)
        if pn.get(name) == None:
            print('Name Does NOT Exist! ')
            newName = input('Type 1 to add a new name:  ')
            if newName == '1':
                addNewname = input('Type the New Name Here: ')
                pn.get(addNewname)
                if pn.get(addNewname) == None:
                    newPn = input('Type the Phone Number Here: ')
                    if len(newPn) != 10:
                        print('The Number is Invalid')


                    else:
                        pn[addNewname] = newPn
                        print('the name', addNewname, 'with the number', newPn, 'was added!')
                        print('Thank you for using our program!')
                else:
                    print('Name Already Exists!')
                    print('Thank you for using our program!')
        else:
            print(name, 'Number is: ', pn[name])
            print('Thank you for using our program!')

elif options == '3':
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


elif options == '1':
        number = input('Number: ')
        if number in pn.values():
            for esm, r8m in pn.items():
                if number == r8m:
                    print(number,'is', esm,"'s number")
                    print('Thank you for using our program!')

        else:
            print('Number does NOT Exist! ')
            newNumber = input('Type 1 to add a new Number:  ')
            if newNumber == '1':
                addNewNumber = input('Type New Number Here: ')
                if addNewNumber in pn.values():
                    print('Number Already Exists!')
                elif len(addNewNumber) != 10:

                    print("Invalid Number")
                else:
                    newName = input('Type the name here: ')
                    pn[newName] = addNewNumber
                    print('the number', addNewNumber, 'for', newName, 'was added!')
                    print('Thank you for using our program!')
