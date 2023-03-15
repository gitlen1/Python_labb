import argparse
import json

def new(guestbooklist):
    print("Add a new note...")
    nNote = input("This is my note ")
    guestbooklist.append(nNote)

def list_notes(guestbooklist):
    print("Printing all entries in the guestbook...")
    for i in range(len(guestbooklist)):
        print(guestbooklist[i])

def edit(guestbooklist, edit_number):
    print("Change the note...")
    cNote = input("Enter the new note >>> ")
    guestbooklist[-edit_number] = cNote

def delete(guestbooklist):
    guestbooklist.pop() 
    print("Deleted the latest note.")

def export(guestbooklist):
    guestbook_dict = {i+1: guestbooklist[i] for i in range(len(guestbooklist))}
    guestbook_json = json.dumps(guestbook_dict, indent=4)
    print(guestbook_json)

def guestbook():
    parser = argparse.ArgumentParser(description='Guestbook Manager CLI')
    subparsers = parser.add_subparsers(dest='command')

    new_parser = subparsers.add_parser('new', help='Add a new note')

    list_parser = subparsers.add_parser('list', help='Print all entries in the guestbook')

    edit_parser = subparsers.add_parser('edit', help='Change the third newest note')
    edit_parser.add_argument('edit_number', type=int, help='Specify the index of the note to edit')

    delete_parser = subparsers.add_parser('delete', help='Delete the latest note')

    export_parser = subparsers.add_parser('export', help='Export the guestbook as a JSON file')

    quit_parser = subparsers.add_parser('quit', help='Exit the program')

    guestbooklist = []

    while True:
        args = parser.parse_args(input().split())
        if args.command == 'new':
            new(guestbooklist)
        elif args.command == 'list':
            list_notes(guestbooklist)
        elif args.command == 'edit':
            edit(guestbooklist, args.edit_number)
        elif args.command == 'delete':
            delete(guestbooklist)
        elif args.command == 'export':
            export(guestbooklist)
        elif args.command == 'quit':
            break
        else:
            print('Invalid command')

if __name__ == "__main__":
    guestbook()
