# Library Management System with MongoDB

This project is a Library Management System built with Python and MongoDB using the MongoEngine ODM (Object-Document Mapper). It demonstrates how to create, read, update, and delete records for books, authors, users, and loans. The project also implements a Singleton pattern for managing the database connection efficiently.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Singleton Pattern for Database Connection](#singleton-pattern-for-database-connection)
- [Using MongoEngine as an ORM](#using-mongoengine-as-an-orm)
- [CRUD Operations](#crud-operations)
- [Usage](#usage)
- [License](#license)

## Overview

The Library Management System allows you to manage:

- **Books**: Store information about books, including title, author, genre, and availability.
- **Authors**: Store details about authors, including their name, date of birth, and works written.
- **Users**: Maintain information about library users, including name, email address, and borrowed books.
- **Loans**: Keep track of book loans, including the user, borrowed book, and loan date.

## Features

- Singleton pattern for efficient database connection.
- Use of MongoEngine as an ORM to interact with MongoDB in an object-oriented manner.
- CRUD operations for books, authors, users, and loans.
- Proper handling of relationships between collections using MongoEngine's `ReferenceField`.

## Technologies Used

- **Python**: Main programming language.
- **MongoDB**: NoSQL database for storing the library data.
- **MongoEngine**: Object-Document Mapper (ODM) for MongoDB.
- **dotenv**: For managing environment variables securely.

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```

2. **Set up a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Environment Variables**:
    - Create a `.env` file in the root directory and add your MongoDB URI:
    ```
    MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority
    ```

5. **Run the Application**:
    ```bash
    python main.py
    ```

## Singleton Pattern for Database Connection

To manage the database connection efficiently, we implemented a Singleton pattern in the `Database` class. The Singleton pattern ensures that only one instance of the database connection is created throughout the application's lifecycle. This helps in reducing the overhead of creating multiple connections and ensures efficient resource utilization.

### Implementation

```python
# db.py

import os
import mongoengine as me
from dotenv import load_dotenv

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            load_dotenv()
            uri = os.getenv('MONGODB_URI')
            if not uri:
                raise ValueError("The MONGODB_URI environment variable is not set")
            me.connect(host=uri)
        return cls._instance
```

- **Lazy Initialization**: The connection is established only when needed, and it is reused for subsequent database operations.
- **Secure**: The MongoDB URI is stored as an environment variable, preventing exposure of sensitive data.

## Using MongoEngine as an ORM

MongoEngine is used as an Object-Document Mapper (ODM) to interact with MongoDB in an object-oriented way. It simplifies data manipulation and helps maintain relationships between different collections using `ReferenceField`.

### Models

- **Author**: Represents an author with fields for name, date of birth, and works.
- **Book**: Represents a book with fields for title, genre, availability, and a reference to an author.
- **User**: Represents a user with fields for name, email, and a list of borrowed books.
- **Loan**: Represents a loan with references to a user and a book, along with the loan date.

### Example Model

```python
# models.py

class Book(me.Document):
    title = me.StringField(required=True, max_length=200)
    author = me.ReferenceField(Author, required=True)
    genre = me.StringField(max_length=100)
    availability = me.BooleanField(default=True)
```

## CRUD Operations

CRUD (Create, Read, Update, Delete) operations are implemented for all entities. Here's an overview of what each operation does:

- **Create**: Inserts new records into the database. For example, `insert_books` inserts books into the `Book` collection and references authors by their IDs.
- **Read**: Retrieves records from the database. For instance, `read_books` fetches all books along with their authors.
- **Update**: Modifies existing records. For example, `update_availability` changes the availability status of a book.
- **Delete**: Removes records from the database. For example, `delete_book` deletes a book record.

### Example Create Operation

```python
# crud/create.py

def insert_books(books_data, authors_objs):
    books_objs = []
    for book in books_data:
        author_name = book.pop('author')
        author_obj = next((author for author in authors_objs if author.name == author_name), None)
        if author_obj:
            book['author'] = author_obj
            books_objs.append(Book(**book).save())
    return books_objs
```

- The `insert_books` method creates new book records and references the author using `ReferenceField`.

## Usage

1. **Insert Data**: Use the provided methods in `create.py` to insert authors, books, users, and loans.
2. **Retrieve Data**: Use methods in `read.py` to fetch and display records.
3. **Update Data**: Use methods in `update.py` to modify existing records.
4. **Delete Data**: Use methods in `delete.py` to remove records from the database.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

By Camilo Rivera Q
