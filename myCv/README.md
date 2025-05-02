# Django Resume Builder

This is a Django-based web application that allows users to create, manage, and download resume profiles.

## Features

- Submit profile data including name, email, phone, address, summary, degree, university, experience, and skills via a web form.
- Store profiles in a database using Django's ORM.
- View a list of all submitted profiles.
- Download resumes as PDF files generated dynamically using `pdfkit` and `wkhtmltopdf`.
- View resumes as HTML pages.
- Delete profiles from the list.
- Responsive UI styled with Bootstrap and FontAwesome icons.

## Technologies Used

- Django (Python web framework)
- pdfkit and wkhtmltopdf for PDF generation
- Bootstrap 4 for UI styling
- FontAwesome for icons

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd myCv
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install `wkhtmltopdf`:

   Download and install from [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html).

   Make sure the path to `wkhtmltopdf.exe` is correctly set in `pdf/views.py` (line with `Configuration`).

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/` to access the app.

## Usage

- Fill out the resume form on the home page to create a new profile.
- View the list of profiles by clicking the "Open Resume List" button.
- Download or view resumes from the list.
- Delete profiles as needed.

## Project Structure

- `pdf/` - Main Django app containing models, views, templates, and URL routing.
- `myCv/` - Django project configuration files.
- `templates/pdf/` - HTML templates for the app.
- `pdf/views.py` - Contains views for handling profile submission, listing, resume generation, and deletion.
- `pdf/models.py` - Defines the `Profile` model.
- `pdf/templates/pdf/accept.html` - Form for submitting profile data.
- `pdf/templates/pdf/list.html` - Displays list of profiles.
- `pdf/templates/pdf/resume.html` - Resume layout used for HTML and PDF rendering.

## License

This project is licensed under the MIT License.
