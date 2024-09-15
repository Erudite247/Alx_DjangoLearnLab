# Advanced API Project

## API Endpoints

- **List Books**
  - `GET /books/`
  - Retrieves a list of all books.

- **Retrieve Book**
  - `GET /books/<id>/`
  - Retrieves a single book by its ID.

- **Create Book**
  - `POST /books/create/`
  - Creates a new book (authentication required).

- **Update Book**
  - `PUT /books/<id>/update/`
  - Updates an existing book (authentication required).

- **Delete Book**
  - `DELETE /books/<id>/delete/`
  - Deletes a book (authentication required).

## Permissions

- **ListView** and **DetailView**: Accessible to all users.
- **CreateView**, **UpdateView**, and **DeleteView**: Restricted to authenticated users.
