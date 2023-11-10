# CRUD
# MY Project
clients = ['Luis', 'Samuel']
list(enumerate(clients))

def create_client(client_name):
    if client_name not in clients: 
        clients.append(client_name) 
        print(clients)
    else:
         print("Client already exists: {}".format(client_name))

def update_client(client_name, client_name_update):
    if client_name in clients:
        index = clients.index(client_name) #arrojan la posicion del cliente
        clients[index] = client_name_update #remplazo por posicion 
        print(clients)
    else:
        print("The name its no found:{}".format(client_name))

    
def delete_client():
    global clients,client_delete
    client_delete = input("Type the name to delete:")
    if client_delete in clients:
        clients.remove(client_delete)
        print(f"Client Deleted:{client_delete}")
    else:
        print("Client not found")


def _print_welcome():
    print("WELCOME TO UNIVERSIDAD DEL VALLE - TULUA")
    print('*' * 100)
    print("What would you like to do today:")
    print("[C]reate client or user")
    print("[R]ead client or user")
    print("[U]pdate client or user")
    print("[D]elete client or user")
    print("[E]xit")


def _get_client_name(): 
    return input("Type your name client:")


def _get_list_client_names():
    global clients
    print(clients)


if __name__ == '__main__':
    while True:
        _print_welcome()
        option = input("Type otpion desired: ").upper()

        if option == "E":
             break
        
        elif option == "C":
            client_name = _get_client_name()
            create_client(client_name)
            _get_list_client_names

        elif option == 'R':
            print("Here are the clients:")
            for i in range(len(clients)):
                print(i+1,"-",clients[i])
        
        elif option == 'U':
            client_name = _get_client_name()
            client_name_update = input("What is the name to update:")
            update_client(client_name,client_name_update)

        elif option == 'D':
            delete_client()                
        else:
            print("Invalid command")