# CarDeals - Django Car Dealership Project

A web application built with Django that allows users to manage and showcase cars for sale. This project demonstrates basic CRUD operations, image handling, and responsive design using Bootstrap.

## Features

- List available cars with details and images
- Add new cars with specifications
- Delete existing car listings
- Responsive design for mobile and desktop
- Image upload functionality
- Clean and modern UI using Bootstrap 5

## Technologies Used

- Python 3.12
- Django 5.1.7
- Bootstrap 5.1.3
- SQLite3
- Pillow (Python Imaging Library)

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/Django_cars.git
cd Django_cars
```

2. Create a virtual environment
```bash
python -m venv env
```

3. Activate the virtual environment
```bash
# On Windows
env\Scripts\activate
```

4. Install required packages
```bash
pip install -r requirements.txt
```

5. Apply migrations
```bash
cd src
python manage.py migrate
```

6. Create superuser (admin)
```bash
python manage.py createsuperuser
```

7. Run the development server
```bash
python manage.py runserver
```

8. Visit http://127.0.0.1:8000 in your browser

## Project Structure

```
Django_cars/
├── src/
│   ├── car/                    # Main app directory
│   │   ├── migrations/         # Database migrations
│   │   ├── templates/car/      # App templates
│   │   ├── admin.py           # Admin configuration
│   │   ├── models.py          # Database models
│   │   ├── urls.py            # URL configurations
│   │   └── views.py           # View functions
│   ├── media/                 # Uploaded images
│   ├── project/               # Project settings
│   ├── templates/             # Base templates
│   ├── manage.py             
│   └── requirements.txt       # Project dependencies
└── README.md
```

## Usage

1. Navigate to the home page to see an overview
2. Click "Cars" to view all listed vehicles
3. Use "Add Car" to create a new listing
4. Each car listing shows:
   - Make and model
   - Year
   - Color
   - Price
   - Description
   - Image (if uploaded)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Learning Outcomes

Through this project, you'll learn:
- Django MVT (Model-View-Template) architecture
- CRUD operations in Django
- File handling in Django
- Bootstrap integration
- Form processing
- Database migrations
- Template inheritance
- URL routing
- Static and media files management

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- Python Documentation
