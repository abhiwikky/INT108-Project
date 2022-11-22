def add_data():
    # FUNCTION TO ADD DATA INTO A TUPLE AND APPEND IT INTO THE DATASET LIST

    global dataset
    print('\n**ADD ENTRIES**')

    while True:
        a = str(input('Enter Student Name      :>> '))
        temp = list(a)
        tmp = ''
        for i in temp:
            if i != ' ':
                tmp += i
        if tmp.isalpha():
            break
        else:
            print('\n!!!!ERROR!!!!\n**Invalid Name**\n')
            continue

    def ph():
        try:
            while True:
                b = int(input('\nEnter Student Ph. No. :>> +91 '))
                if len((str(b))) != 10:
                    print('\n!!!!ERROR!!!!\n**Invalid Phone number**')
                    continue
                else:
                    return b
        except ValueError:
            print('\n!!!!ERROR!!!!\n**Enter Correct Format Entries**')
            ph()

    b = ph()
    dataset.append((a, b))


def show_all():
    global dataset
    # FUNCTION TO SHOW ALL ELEMENTS IN A LIST
    print('*' * 50)
    print('\n**DISPLAYING ALL STUDENTS DETAILS**')
    for i in range(0, len(dataset)):
        print(i + 1, 'st entry :>>', dataset[i])
    print('*' * 50)
    print()


def show_data():
    global dataset
    print('###Instructions for single and multi search###')
    print('>>>Keep on Entering Full Name to be searched, one by one. Example: Abhinav S.')
    print('>>>For finishing name entry, simply press enter\n')

    while True:
        lis = []
        for i in dataset:
            lis.append(i[0])
        re = 0
        v = []
        while re == 0:
            k = input('>>>')
            if k == '':
                break
            else:
                v.append(k)
                continue
        if len(v) == 1:
            v = v[0]
        else:
            v = tuple(v)

        if type(v) == str:
            if v.isalpha():
                if v in lis:
                    t = lis.index(v)
                    print('-' * 50)
                    print('Requested Data Is :', dataset[t])
                    print('-' * 50)
                    print('\n')
                    break
                elif v not in lis:
                    print('!!!!ERROR!!!! >>> Name', i, 'Not Found In Database')
                    continue
            else:
                print('!!!!ERROR!!!!\n**Enter Correct Format Names As Given In The Examples**\n')
                continue
        elif type(v) == tuple:
            v = list(v)
            count1 = 0
            print('-' * 40)
            for i in v:
                count1 += 1
                print(count1, end='st ')
                if i in lis:
                    t = lis.index(i)
                    print('Requested Data Is :', dataset[t])
                elif i not in lis:
                    print('!!!!ERROR!!!! >>> Name "' + i + '" Not Found In Database')
                    continue
            print('-' * 40)
            break
        else:
            print('!!!!ERROR!!!!\n**Enter Correct Format Names As Given In The Examples**\n')
            continue


def select():
    # function for selection of appropriate option

    print('*' * 30)
    print("\nFor Adding Details, Enter         :>> A")
    print("For Displaying All Entries        :>> B")
    print("For Displaying Individual Entries :>> C")
    print("For Exiting The Program           :>> D")
    selection = input('\nA/B/C/D >>>')
    if selection not in ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']:
        print('!!!!ERROR!!!!\n**SELECT THE APPROPRIATE OPTION(A/B/C/D)**')
        select()
    else:
        return selection


print('*' * 30)
print("\nWELCOME TO STUDENT CONTACT DETAILS REPOSITORY \nENTER THE APPROPRIATE INPUT FROM THE BELOW OPTIONS")

dataset = []
while True:
    option = select()
    if option == 'a' or option == 'A':
        while True:
            add_data()
            z = input('Enter more ? (Y/N)')
            if z == 'Y' or z == 'y':
                continue
            else:
                print('\n**ALL ENTRIES SAVED**')
                break
    elif option == 'b' or option == 'B':
        show_all()
    elif option == 'c' or option == 'C':
        show_data()
    elif option == 'd' or option == 'D':
        print('\n!!!!EXITING  THE PROGRAM!!!!')
        print('Bye Bye!')
        break
