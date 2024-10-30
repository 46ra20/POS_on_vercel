# POS System

This POS (Point of Sale) System is designed to streamline operations for shops and marketplaces. It includes features for managing sales, purchases, inventory, expenses, payments, and promotions, all integrated into an easy-to-use system. The system is secure, and user accounts are provided by the administrator.



## Getting Started

### Login System

  - Users need to log in with their **Username** and **Password** provided by the system administrator.
  - Once logged in, the user can access all features based on their role.

### Dashboard

  - The dashboard provides a summary of the business's financial performance, including **daily**, **monthly**, **yearly**, and **total income** statistics.



## Key Features

### 1. Sales & Purchases

- **Sales**:
  - Record and track sales transactions.
  - View the full history of sales.
  
- **Returns**:
  - Process product returns.
  - Track and view all return transactions.

- **Purchases**:
  - Log and track new product purchases.
  - Access a complete purchase history.

- **Stock**:
  - Manage and view inventory levels for all products.

- **Damages**:
  - Record damaged items in stock.
  - View the history of all damaged items.



### 2. Product Information Management

- **Units**:
  - Manage product measurement units (e.g., kg, pcs).

- **Products**:
  - Add new products to the inventory.
  - View and manage the list of all available products.

- **Categories**:
  - Create, update, and delete product categories.

- **Brands**:
  - Add, update, or remove product brands.

---

### 3. Expenses & Payments

- **Expenses**:
  - Log and track all business expenses.
  - View a history of all recorded expenses.

- **Payments**:
  - Record payments for services or product orders.
  - View and manage payment history.


### 4. Promotions

- **Promotional SMS**:
  - Send promotional SMS messages to customers to increase engagement and sales.



## Technologies Used

- **Backend**:
  - Python
  - Django
  - Django REST Framework
  - PostgreSQL
  - Supabase for real-time database functions
  - Vercel for deployment

- **Frontend**:
  - JavaScript
  - HTML5
  - CSS3
  - Bootstrap



## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pos-system.git
cd pos-system
```

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

### 6. Access the Application

Open your browser and navigate to `http://127.0.0.1:8000/`.



## API Endpoints

### 1. Authentication

- **POST** - User login:  
  `POST account/login/`
- **GET** - User logout:  
  `GET account/logout/`

### 2. Sales & Purchases

- **POST** - Create new sale:  
  `POST product_sales/sales_save/`

- **POST** - Record a return:  
  `POST product_sales/return/`

- **POST** - Add new purchase:  
  `POST product/purchase/`

- **GET** - List all stock items:  
  `GET product/view_stock/`

- **POST** - Record damaged items:  
  `POST product_sales/damage_add/`

### 3. Product Management

- **POST** - Add new product:  
  `POST product/add_product/<userId>/`

- **GET** - List all products:  
  `GET /product/`

### 4. Expenses & Payments

- **POST** - Record an expense:  
  `POST expanses_and_payments/ payment/<key>/`

- **POST** - Record a payment:  
  `POST expanses_and_payments/ expanse_add/`
### 5. Promotions

- **POST** - Send promotional SMS:  
  `POST /promotional/`



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


## Contact

For any inquiries or access requests, feel free to contact:

- **Md Rakib Bhuiyan**
- Email: [rakib2046.md@.com]
- GitHub: [https://github.com/46ra20](https://github.com/46ra20)
