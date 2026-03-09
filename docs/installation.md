# Installation Guide

This guide will help you set up the `state-security-analyzer` project for development.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool (venv, virtualenv, or conda)

## Installation Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd state-security-analyzer
```

### 2. Create a Virtual Environment

Using venv:

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

Using conda (recommended for scientific computing):

```bash
conda create -n state-security-analyzer python=3.10
conda activate state-security-analyzer
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:

- **Django**: Web framework
- **Django REST Framework**: API development
- **NumPy**: Numerical computations
- **Shapely**: Geometric operations
- **NetworkX**: Graph algorithms
- **Pandas**: Data manipulation
- **Matplotlib**: Plotting
- **Plotly**: Interactive visualizations

### 4. Database Setup

The project uses SQLite for development by default.

Run Django migrations:

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

For accessing the Django admin interface:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Verification

After setup, you should be able to:

1. Access the web interface at the local URL
2. Run simulations via the command line using the core engine
3. Access the Django admin at `/admin/` (if superuser created)

## Troubleshooting

### Common Issues

- **Import errors**: Ensure all dependencies are installed and virtual environment is activated
- **Database errors**: Run `python manage.py migrate` to set up the database
- **Port conflicts**: Use `python manage.py runserver <port>` to specify a different port

### Development Tools

For enhanced development experience:

- Install Django Debug Toolbar: `pip install django-debug-toolbar`
- Configure your IDE for Django development
- Set up pre-commit hooks for code quality
