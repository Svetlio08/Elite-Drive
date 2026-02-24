# EliteDrive 🚗

EliteDrive is a luxury car catalog web application built with Django and PostgreSQL.

The application allows managing premium cars, brands, features, and curated collections.  
It demonstrates full CRUD functionality, model relationships, filtering, custom validations, and custom template filters.

---

## 🛠 Tech Stack

- Python
- Django
- PostgreSQL
- Bootstrap 5
- HTML & CSS

---

## 📦 Features

- Full CRUD for:
  - Cars
  - Brands
  - Features
  - Collections
- Many-to-One relationship (Car → Brand)
- Many-to-Many relationships:
  - Car ↔ Feature
  - Collection ↔ Car
- Filtering & Sorting for Cars
- Pagination
- Custom form validations
- Disabled (read-only) field in forms
- Custom template filter (`format_price`)
- Custom 404 page
- Responsive Bootstrap UI

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally after download.

---

### 1️⃣ Create Virtual Environment

```bash
python -m venv .venv
```
Activate it:

### Windows
```bash
.venv\Scripts\activate
```
### Mac/Linux

```bash
source .venv/bin/activate
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Create PostgreSQL Database

Make sure PostgreSQL is running.

Create a database named:
```bash
elitedrive
```
Example using psql:
```bash
createdb elitedrive
```

### 4️⃣ Create Environment Variables

Create a file named .env in the project root (next to manage.py) with the following content:
```bash
SECRET_KEY=change-this-secret-key
DEBUG=True

DB_NAME=elitedrive
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=5432
```
Replace:  
- your_password with your PostgreSQL password.

5️⃣ Apply Migrations
``` bash
python manage.py makemigrations
python manage.py migrate
```
6️⃣ Run the Development Server
``` bash
python manage.py runserver
```
Open in your browser:
``` bash
http://127.0.0.1:8000/
```

---

## 📂 Main Page

| Page        | URL             |
| ----------- | --------------- |
| Home        | `/`             |
| Cars        | `/cars/`        |
| Brands      | `/brands/`      |
| Features    | `/features/`    |
| Collections | `/collections/` |

---

## 🔍 Filtering & Sorting

- The Cars page supports:
- Search by model or brand
- Filter by brand
- Filter by fuel type
- Filter by transmission
- Filter by feature
- Filter by price range
- Sorting by:
  - Newest
  - Price (ascending / descending)
  - Year
  - Horsepower

---

## 🧩 Custom Functionality Custom Template Filter

format_price

Formats numeric values:

250000 → 250,000.00

---

## Custom 404 Page

A custom styled 404 page is implemented and configured in the project URLs.

---

## 🗄 Database Structure
Models
- Brand
- Feature
- Car
- Collection   

Relationships
- Car → Brand (ForeignKey)
- Car ↔ Feature (ManyToMany)
- Collection ↔ Car (ManyToMany)

---

## Author

Svetlomir
EliteDrive – Luxury Car Catalog