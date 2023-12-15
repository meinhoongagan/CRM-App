# Django CRM App 📊🔒

Welcome to the Django CRM App, a customer relationship management system built using Django! This app allows managing client leads, converting them to clients, and includes authorization features. Please note that certain sections are under development.

## Features 🚀

- **Client Leads Management:** Store and manage leads' information.
- **Lead Conversion:** Convert leads to clients seamlessly.
- **Authorization:** Secure access with user authentication and authorization.
- **Admin Panel:** Utilize Django's admin panel for efficient data management.
- **Database Structure:** Well-designed SQLite database tables for CRM functionalities.
- **Team Collaboration:** Manage teams using a many-to-many field for improved collaboration and organization.
- **Dashboard:** Introducing a dashboard template for enhanced data visualization and insights.
- **My Account:** Users can view and modify their account details.
- **Teams Form:** Modify team names for improved team management.

## Incomplete Work 🚧
- **Non-dynamic Homepage:** Currently, the homepage lacks dynamic content.

## Installation & Usage 🛠️🔍

1. **Clone the repository:**
   ```bash
   git clone https://github.com/meinhoongagan/Django-CRM-App.git
2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
3. **Run migrations:**

    ```bash
    python manage.py migrate
4. **Create a superuser (Admin):**

    ```bash
    python manage.py createsuperuser
5. **Start the development server:**

    ```bash
    python manage.py runserver
6. **Access the Admin Panel:**
    Visit http://localhost:8000/admin and log in with your superuser credentials to manage CRM data.

# Database Schema 🗄️
Below is an overview of the main tables in the SQLite database:

Clients: Information about converted leads turned into clients.
Leads: Details of potential leads.
Users: Django's default User table for authentication.
# Contribution Guidelines 🤝
Contributions are welcome! Fork the repository, make improvements, and submit a pull request following our guidelines in CONTRIBUTING.md.

# Future Improvements 🌟
Completion of Dashboard: Finishing the dashboard template for better data visualization.
Enhanced Homepage: Implement dynamic content on the homepage for better user engagement.
# Contact 📧
For any queries or suggestions, contact us at gagansharma3002@gmail.com or create an issue on our GitHub repository.
