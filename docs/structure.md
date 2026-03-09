# Project Structure Documentation

## Overview

The `state-security-analyzer` project is a comprehensive security simulation and analysis system designed to model tactical operations, optimize resource deployment, and evaluate risk scenarios in defined security spaces. The architecture follows a modular design separating the core simulation engine from the web interface, allowing for both command-line execution and web-based management.

The system implements behavior trees for agent decision-making, geometric analysis for spatial intelligence, and probabilistic calculations for incident prediction. It supports three operational cycles: Strategic (long-term planning), Operative (regional coordination), and Tactical (real-time execution).

## Directory Structure

### Root Level Files

- **`.gitignore`**: Standard Python and Django ignore patterns. Excludes virtual environments, cache files, logs, and sensitive data like database files and API keys.
- **`LICENSE`**: Project licensing information (existing file).
- **`README.md`**: Main project documentation with objective, features, behavior tree execution cycle, and operational cycles (existing file, to be updated with setup instructions).
- **`requirements.txt`**: Python dependencies pinned to specific versions for reproducibility:
  - Django: Web framework for the application layer
  - djangorestframework: API development
  - numpy: Numerical computations for simulations
  - shapely: Geometric operations for spatial analysis
  - networkx: Graph algorithms for behavior trees and route optimization
  - pandas: Data manipulation for analysis and reporting
  - matplotlib/plotly: Visualization of results and spatial data
- **`manage.py`**: Django's command-line utility for project management (migrations, running server, etc.).

### `core/` - Core Simulation Engine

This directory contains the framework-agnostic simulation logic, designed to be reusable as a standalone library or CLI tool. It implements the core algorithms described in the README's behavior tree execution cycle.

- **`__init__.py`**: Package initialization, potentially exposing main simulation classes.
- **`behavior_trees/`**: Implements decision-making logic for security agents.
  - **`__init__.py`**: Package init.
  - **`nodes.py`**: Defines action and condition nodes (patrol, respond, take_cover, engage, retreat, CASEVAC, communicate, resource_management).
  - **`tree.py`**: Tree execution logic, managing the flow through nodes based on agent state and environment.
  - **`evaluators.py`**: Decision evaluators that assess conditions and select appropriate actions.
- **`spatial/`**: Handles geometric and topographic analysis for spatial intelligence.
  - **`__init__.py`**: Package init.
  - **`geometry.py`**: Ballistic calculations, perimeter measurements, and geometric modeling of security spaces.
  - **`topography.py`**: Terrain analysis, elevation modeling, and heliport/route optimization algorithms.
  - **`routes.py`**: Pathfinding algorithms for evacuation, reinforcement, and patrol routes.
- **`simulation/`**: Core execution loop implementing the time-based simulation cycle.
  - **`__init__.py`**: Package init.
  - **`engine.py`**: Main simulation loop, managing timestep execution and state persistence.
  - **`agents.py`**: Agent models with state (position, fatigue, resources) and action capabilities.
  - **`teams.py`**: Team coordination logic, resolving conflicts and aggregating actions.
  - **`cycles.py`**: Implementation of strategic, operative, and tactical cycles with different synchronization intervals.
- **`logistics/`**: Resource management and tracking systems.
  - **`__init__.py`**: Package init.
  - **`inventory.py`**: Tracking of ammunition, magazines, and equipment availability.
  - **`reporting.py`**: Automated generation of usage reports and consumption statistics.
  - **`optimization.py`**: Supply chain algorithms for resource allocation and replenishment planning.
- **`analysis/`**: Risk assessment and probabilistic modeling.
  - **`__init__.py`**: Package init.
  - **`probabilities.py`**: Statistical models for calculating incident probabilities based on agent behaviors and environmental factors.
  - **`contingencies.py`**: Officer down protocols, including equipment reallocation and plan adjustments.
  - **`statistics.py`**: Analysis of behavior evolution and predictive modeling from historical data.
- **`utils/`**: Shared utilities and configuration.
  - **`__init__.py`**: Package init.
  - **`config.py`**: Simulation parameters (timestep duration, cycle intervals, agent capabilities).
  - **`logging.py`**: Custom logging system for simulation events, state changes, and incident tracking.

### `state_security_analyzer/` - Django Project Configuration

Standard Django project directory containing global settings and URL routing.

- **`__init__.py`**: Marks directory as Python package.
- **`settings.py`**: Project configuration including:
  - INSTALLED_APPS: Lists all Django apps (built-in + custom apps)
  - Database configuration (SQLite for development)
  - Security settings (SECRET_KEY, DEBUG, ALLOWED_HOSTS)
  - Static/media file handling
  - Internationalization and timezone settings
- **`urls.py`**: Root URL configuration, routing requests to app-specific URL patterns.
- **`wsgi.py`**: WSGI application entry point for production deployment.
- **`asgi.py`**: ASGI application for asynchronous operations (future-proofing for real-time simulations).

### `apps/` - Django Applications

Modular Django apps handling different aspects of the web interface.

- **`scenarios/`**: Scenario management and configuration.
  - **`__init__.py`**: App init.
  - **`models.py`**: Database models for scenarios, agents, teams, and configuration parameters.
  - **`views.py`**: Views for creating, editing, and running simulation scenarios.
  - **`forms.py`**: Django forms for user input validation and scenario setup.
  - **`templates/`**: HTML templates for scenario management interface.
  - **`static/`**: CSS/JS for interactive maps and parameter input widgets.
  - **`tests.py`**: Unit tests for scenario functionality.
- **`analysis/`**: Results visualization and reporting.
  - **`__init__.py`**: App init.
  - **`models.py`**: Models for storing simulation results, logs, and analysis data.
  - **`views.py`**: Views for displaying charts, reports, and spatial visualizations.
  - **`templates/`**: Templates for result dashboards and export options.
  - **`static/`**: Chart libraries (Chart.js, Plotly) and custom visualization scripts.
  - **`tests.py`**: Tests for analysis and reporting features.
- **`api/`**: REST API for external integrations.
  - **`__init__.py`**: App init.
  - **`serializers.py`**: DRF serializers for API data validation and formatting.
  - **`views.py`**: API viewsets and endpoints for scenario execution and result retrieval.
  - **`urls.py`**: API URL patterns and versioning.
  - **`tests.py`**: API endpoint tests and integration tests.
- **`dashboard/`**: Administrative monitoring interface.
  - **`__init__.py`**: App init.
  - **`views.py`**: Custom admin views for system monitoring and configuration.
  - **`templates/`**: Admin dashboard templates with real-time status displays.
  - **`tests.py`**: Dashboard functionality tests.

### `scripts/` - Utility Scripts

Command-line tools for development and deployment.

- **`run_simulation.py`**: CLI script to execute simulations independently of the web interface. Imports core engine and handles parameter parsing.
- **`import_data.py`**: Bulk data import utility for initializing scenarios or loading historical data.

### `tests/` - Global Test Suite

Project-wide testing infrastructure.

- **`__init__.py`**: Test package init.
- **`test_simulation.py`**: Integration tests for the core simulation engine, validating behavior trees and spatial calculations.
- **`test_api.py`**: End-to-end API tests ensuring proper data flow and error handling.

### `docs/` - Documentation

Comprehensive documentation for development and usage.

- **`index.md`**: Project overview and getting started guide.
- **`api.md`**: Detailed API documentation with examples.
- **`simulation_guide.md`**: User guide for configuring and running simulations.
- **`deployment.md`**: Instructions for production deployment and scaling.

### `docker/` - Containerization

Optional Docker setup for consistent deployment.

- **`Dockerfile`**: Container definition with Python environment and dependencies.
- **`docker-compose.yml`**: Multi-service orchestration (web app, database, potentially simulation workers).

## Integration and Data Flow

1. **Configuration**: Scenarios are defined via `apps/scenarios/` web interface or API, stored in Django models.
2. **Execution**: Simulations run through `core/simulation/engine.py`, utilizing behavior trees, spatial analysis, and logistics tracking.
3. **Analysis**: Results are processed by `core/analysis/` modules and stored for visualization in `apps/analysis/`.
4. **Reporting**: Web interface in `apps/analysis/` displays results using charts and maps.
5. **API Access**: External systems can interact via `apps/api/` endpoints.

## Development Workflow

- Core algorithms in `core/` can be developed and tested independently.
- Web features are built in respective `apps/` directories.
- Scripts in `scripts/` provide CLI access for debugging.
- Tests in `tests/` ensure integration across layers.

This structure ensures maintainability, testability, and scalability while supporting both research-oriented simulation development and production web deployment.
