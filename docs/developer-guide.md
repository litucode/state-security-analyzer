# Developer Guide

This guide is for developers contributing to the `state-security-analyzer` project.

## Development Environment

### Prerequisites

- Python 3.8+
- Git
- Virtual environment (venv/conda)
- Code editor (VS Code recommended)

### Setup

Follow the [Installation Guide](installation.md) for basic setup.

### Additional Development Tools

```bash
pip install -r requirements-dev.txt  # If available
```

Recommended tools:

- `black` for code formatting
- `flake8` or `ruff` for linting
- `pytest` for testing
- `pre-commit` for git hooks

## Project Structure

See [Project Structure](structure.md) for detailed architecture overview.

### Key Components

- **`core/`**: Framework-agnostic simulation engine
- **`apps/`**: Django applications for web interface
- **`state_security_analyzer/`**: Django project configuration

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed

### 3. Run Tests

```bash
python manage.py test
```

### 4. Commit Changes

```bash
git add .
git commit -m "Add feature: description"
```

### 5. Push and Create PR

```bash
git push origin feature/your-feature-name
```

## Coding Standards

### Python Style

- Follow PEP 8
- Use type hints where possible
- Maximum line length: 88 characters (Black default)
- Use descriptive variable names

### Django Best Practices

- Use class-based views
- Implement proper error handling
- Use Django ORM effectively
- Follow REST API conventions

### Documentation

- Add docstrings to all public functions/classes
- Update relevant documentation files
- Include inline comments for complex logic

## Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.scenarios

# Run with coverage
coverage run manage.py test
coverage report
```

### Writing Tests

- Use Django's TestCase for model/view tests
- Use pytest for utility function tests
- Aim for 80%+ code coverage
- Test edge cases and error conditions

## Database Migrations

When changing models:

```bash
# Create migration
python manage.py makemigrations

# Apply migration
python manage.py migrate

# Test migration
python manage.py test
```

## API Development

### Adding New Endpoints

1. Add serializer in `apps/api/serializers.py`
2. Add view in `apps/api/views.py`
3. Add URL pattern in `apps/api/urls.py`
4. Update API documentation

### Versioning

- Use URL versioning: `/api/v1/`
- Maintain backward compatibility
- Document breaking changes

## Simulation Engine

### Core Concepts

- **Behavior Trees**: Decision-making framework
- **Spatial Analysis**: Geometric calculations
- **Time-based Simulation**: Discrete event simulation

### Extending the Engine

- Add new node types in `core/behavior_trees/nodes.py`
- Implement spatial algorithms in `core/spatial/`
- Add analysis methods in `core/analysis/`

## Deployment

### Development Server

```bash
python manage.py runserver
```

### Production Deployment

- Use Gunicorn or uWSGI
- Configure static file serving
- Set up database backups
- Implement monitoring

## Contributing

### Issue Tracking

- Use GitHub Issues for bug reports and feature requests
- Follow issue templates
- Provide clear reproduction steps

### Pull Request Process

- Ensure CI passes
- Get code review from maintainers
- Squash commits before merge
- Update CHANGELOG.md

## Security Considerations

- Validate all user inputs
- Use Django's security features
- Implement proper authentication/authorization
- Regular dependency updates

## Performance Optimization

- Profile code with `cProfile`
- Optimize database queries
- Use caching where appropriate
- Monitor memory usage in simulations
