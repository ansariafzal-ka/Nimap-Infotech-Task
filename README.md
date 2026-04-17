# FastAPI Machine Test - Nimap Infotech

This project implements Category and Product APIs using FastAPI with CRUD operations, pagination, and one-to-many relationship.

## Description

This project implements Category and Product APIs using FastAPI with CRUD operations, pagination, and one-to-many relationship.

## Project Structure

```
src/
  config/
  models/
  routes/
  controllers/
main.py
```

## Setup Instructions

```
# clone the repository
git clone https://github.com/ansariafzal-ka/Nimap-Infotech-Task.git
cd  Nimap-Infotech-Task

# create a virtual environment
python -m venv venv

# activate the virtual environment
./venv/scripts/activate

# install the libraries
pip install -r requirements.txt
```

Before running the project, create a .env file first with the url of your mysql database

```
DATABASE_URL=your_db_url
```

Then run the server using

```
uvicorn main:app --reload
```

## Database Design Details

- **Category Table**
  - id (primary key)
  - name (unique, not null)
  - created_at
  - updated_at
- **Product Table**
  - id (primary key)
  - name (not null)
  - description (optional)
  - category_id (foreign key → category.id, not null)
  - created_at
  - updated_at

The db is setup in such a way that one category can have multiple products.
