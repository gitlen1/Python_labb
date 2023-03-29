Create a Guestbook command line application using python
Requirements:

Write a python CLI application implementing a guestbook. It should allow the user to insert a new note in the guestbook, to see all the notes in the guestbook and to edit and delete entries in the guestbook.

Your guestbook application should save the state of the guestbook (all the entries in order of insertion) in a file.

You should name your main python file guestbook.py.

Here are the commands you need to implement:

- guestbook.py new "This is my note"
This command adds a new note with the content "This is my note"

- guestbook.py list
This command prints all the entries in the guestbook

- guestbook.py edit 3 "Change the note"
This command changes the 3rd newest note's content to "Change the note"

- guestbook.py delete 1
This command deletes the most recent note

- implement the command guestbook.py export that prints the contents of the guestbook in json format
