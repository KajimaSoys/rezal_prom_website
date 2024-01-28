
#  README for RezAl Furniture Company Website Repository

## Introduction
Welcome to the repository for the RezAl Furniture Company website, hosted at https://mebel-rezal.com. This repository contains the code for a landing page designed to attract new clients. The website showcases the company's offerings with an appealing and user-friendly design.

## Technology Stack
- **Frontend**: Vue.js
- **Backend**: Django
- **Database**: PostgreSQL
- **Containerization**: Docker (Compose)
- **Web Servers**: Nginx
- **Programming Language**: Python, JavaScript

## Features
- **Landing Page**: Engaging and informative, designed to attract and retain visitor interest.
- **YouTube Player Integration**: For showcasing video content about the company.
- **Image Slider**: To visually highlight key products and offerings.

## Installation
To set up the project locally, follow these steps:
1. Clone the repository:
   ```shell
   git clone https://github.com/KajimaSoys/rezal_prom_website.git
   ```
2. Navigate to the project directory.
3. Configure `.env` files with the following variables:
   - **Backend `.env`**:
     - `DEBUG` - Set for development mode.
     - `SECRET_KEY` - A Django secret key.
     - `ALLOWED_HOSTS` - Default `127.0.0.1,localhost`.
     - `DB_NAME` - Database name.
     - `DB_USER` - Database user.
     - `DB_PASSWORD` - Database password.
     - `DB_HOST` - Default `db`.
     - `DB_PORT` - Default `5432`.
     - `CSRF_COOKIE_SECURE` - Set for HTTPS.
     - `SESSION_COOKIE_SECURE` - Set for HTTPS.
     - `EMAIL_HOST_USER` - (Optional) Email for sending inquiries.
     - `EMAIL_HOST_PASSWORD` - (Optional) Password for the email.
   - **Frontend `./client/.env`**:
     - `VITE_BACKEND_HOST` - Backend host, default `http://127.0.0.1:8000`.
     - `VITE_GOOGLE_API_KEY` - (Optional) Google API key.

4. Use Docker Compose to build and run the containers:
   ```shell
   docker compose build
   ```
   ```shell
   docker compose up -d
   ```
5. Access the application at `localhost` or the configured port.

## License
This project is licensed under the [MIT License](LICENSE).
