import json

def guestbook():

    guestbooklist = []

    choice = 0
    while choice !="Quit":
        print("*** Guestbook Manager ***")
        print("new")
        print("list")
        print("edit 3")
        print("delete 1")
        print("export")
        print("Quit")
        choice = str(input())

        if choice == "new":
            print("Add a new note...")
            nNote = input("This is my note ")
            guestbooklist.append([nNote])

        elif choice == "list":
            print("Printing all entries in the guestbook...")
            for i in range(len(guestbooklist)):
                print(guestbooklist[i]) 


        elif choice == "edit 3":
            print("Change the note 3rd newest note...")
            cNote = input("Change the note >>> ")
            guestbooklist[2] = cNote

        elif choice == "delete 1":
            guestbooklist.pop(-1)
            print("Deleted the most recent note.")

        elif choice == "export":
            guestbook_dict = {i+1: guestbooklist[i] for i in range(len(guestbooklist))}
            guestbook_json = json.dumps(guestbook_dict, indent=4)
            print(guestbook_json)

if __name__ == "__main__":
    guestbook()