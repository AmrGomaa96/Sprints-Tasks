import insert
import delete
import update
def menu():
    print("\n \n Please choose option")
    print("1- Insert Record")
    print("2- Delete Record")
    print("3- Update Record")
while (True):
    menu()
    choice = input("Your Choice :")
    match choice:
        case '1':
            insert.insert()
        case '2':
            delete.delete()
        case '3':
            update.update()
        case 'q':
            exit()
        case _:
            print('Please Enter A valid input\n')
