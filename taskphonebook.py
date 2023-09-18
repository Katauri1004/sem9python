def write_name():
    name = input('Enter the name: ')
    return name

def write_surname():
    surname = input('Enter the surname: ')
    return surname

def write_phone():
    phone = input('Enter the phone: ')
    return phone

def write_adress():
    adress = input('Enter the adress: ')
    return adress

def input_data(a=None):
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open('phonebook.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'{name} {surname} -  {phone}, {adress}\n\n')

def print_data():
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        data_first = data.readlines()
        print(data_first)
        for line in data_first:
            print(line, end='')

def search_line():
    searching = input('Input the data for search: ')
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        temp = data.readlines()
        data_first = ''.join(temp).split('\n\n')
        for line in data_first:
            if searching in line:
                print(line)
        return line        

def rewrite():
    search_line()
    rewrite_data = input('Please, enter the data, that you want to overwrite: ')
    new_data = input('Please, enter the new data: ')
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        old = data.read()
        new = old.replace(rewrite_data, new_data)
    with open('phonebook.txt', 'w', encoding = 'utf-8') as data:
        data.write(new)


# def delete():
#     search_line()
#     want_to_del_data = input('Please, enter the data, that you want to delete: ')
#     with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
#         list_of_el = data.readlines()
#         for el in range(len(list_of_el)):
#             if want_to_del_data in list_of_el[el]:
#                 list_of_el[el] = ''
#     new_data = str(list_of_el)            
                
#     with open('phonebook.txt', 'w', encoding = 'utf-8') as data:
#         data.write(new_data)

def delete():
    search_line()
    rewrite_data = input('Please, enter the data, that you want to delete: ')
    new_data = ''
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        old = data.read()
        new = old.replace(rewrite_data, new_data)
    with open('phonebook.txt', 'w', encoding = 'utf-8') as data:
        data.write(new)







# rewrite()
# delete()
# input_data()
# print_data()







                    
                 



       




# input_data()   
# print_data() 
   


