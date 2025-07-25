# Django Project

A basic Django app using:

- Django
- Pollow for images
- Requests (for external HTTP requests)

## 🚀 Setup

1. Clone the repository
   ```bash
   git clone git@github.com:yvartpro/joliephoto.git
   cd joliephoto
   ```
   
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .env
   source .env/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## 📝 Notes

- Media files and database are not included.
- You may need to create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
   
- Remember to deactivate environment when closing project
   ```bash
   deactivate
   ```

