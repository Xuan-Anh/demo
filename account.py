
import hashlib
def add(username, password, name, age):
    users[username] = {'username': username, 'password': password, 'name': name, 'age': age, 'password':password}

def search(username):
    return users.get(username)

def read_file():
    f = open(file_name, 'r', encoding='utf-8')
    for line in f:
        username, password, name, age = line.split(',')
        age = int(age)
        add(username, password, name, age)
    f.close()

def write_file():
    f = open(file_name, 'w', encoding='utf-8')
    for k, v in users.items():
        user = v
        f.write('%s,%s,%s,%d\n' % (user['username'], user['password'], user['name'], user['age']))
    f.close()

users = dict() #{'abc': {'username': 'abc', 'password': 123456, 'name': vcs, 'age': 22}}
file_name = 'users_database.txt'
read_file()
# print(users)
while True:
    print('__________MENU________')
    print('1. Search by username')
    print('2. Add new')
    print('3. Exit')
    print('__________________')
    choice = int(input('Your choice:'))
    if choice == 3:
        break
    if choice == 1:
        #search
        username = input('Search username: ')
        result = search(username)
        if result:
            print('Ket qua: ', result)
        else:
            print('Not found')
    elif choice == 2:
        #add new
        while True:
            username = input('Username: ')
            if search(username) == None: #available
                break
            else:
                print("Input again: ")
        password = input('Password: ')
        name = input('Name: ')
        age = int(input('Age: '))
        password = input('Password:	')
   		password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        add(username, password, name, age, password)
write_file()