Product Management System
This Django project provides a robust platform for managing products and categories. It includes features such as user authentication, product listing, adding, updating, and deleting products, category-based filtering, and a search function.

Features
User Authentication: Allows users to register, login, and logout securely.
Product Management: Users can add new products, update existing ones, and delete products as needed.
Category Filtering: Products can be filtered based on categories, providing easier navigation.
Search Functionality: Users can search for products using keywords, enhancing the user experience.
PDF Reporting: Generates PDF reports of product information for easy sharing and reference.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/PrashanthBomma5/ProductManagement.git
Navigate to the project directory:
bash
Copy code
cd ProductManagement
Install the required dependencies:
Copy code
pip install -r requirements.txt
Configure the database settings in settings.py.
Apply migrations:
Copy code
python manage.py migrate
Run the development server:
Copy code
python manage.py runserver
Usage
Register an account or login if you already have one.
Navigate through the product management interface.
Add, update, or delete products as necessary.
Utilize category filtering and search functionality for better product discovery.
Generate PDF reports for product information using the provided functionality.
Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests for any improvements or feature additions.
