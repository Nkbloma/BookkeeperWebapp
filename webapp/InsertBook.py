class InsertBook:
    """
        Book Title:
            Enter Book title
        
        Book Author: 
            See if Author's name is in the thing. If it is enter id of author
            If not add new author. I don't like the idea that people can just add
            new authors willy nilly, I think it would be best if it worked like genre
            where they're already put in there. This is okay though.

        Book Publisher:
            Same with publisher, I don't like the idea that they can just add publishers
            but I'll deal with it.
        
        Publish Date: Add date if None put None
        Start Date: Add date if None put None
        Finish Date: Add date if None put None
        Number of Pages: add number
        Current Page: Add number
        IsFinished: If false 0 if true 1
        Book Description Add description
        Interest Level: Get number and add it.

        Genre: I'm assuming I just have to get the name, get the ids of the name
        Then add a combination of the new book id and the genre ids into the
        genrejunction table.
    """