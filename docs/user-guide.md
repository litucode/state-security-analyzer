# User Guide

This guide explains how to use the `state-security-analyzer` application for security analysis and simulation.

## Overview

The application provides tools for:

- Creating and managing security scenarios
- Running simulations with behavior trees
- Analyzing spatial intelligence and logistics
- Generating reports and visualizations

## Getting Started

### Accessing the Web Interface

After installation, start the server:

```bash
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` in your browser.

### Dashboard

The main dashboard provides:

- Overview of active scenarios
- Quick access to recent analyses
- System status and alerts

## Scenario Management

### Creating a Scenario

1. Navigate to the Scenarios section
2. Click "Create New Scenario"
3. Configure:
   - Scenario name and description
   - Geographic boundaries
   - Agent teams and capabilities
   - Equipment inventory
   - Environmental factors

### Scenario Parameters

- **Agents**: Define security personnel with roles, skills, and equipment
- **Teams**: Group agents into tactical units
- **Environment**: Set topography, weather, and threat levels
- **Objectives**: Define mission goals and success criteria

## Running Simulations

### Simulation Types

1. **Tactical Simulation**: Real-time execution with behavior trees
2. **Strategic Analysis**: Long-term planning and resource optimization
3. **Contingency Planning**: Officer down scenarios and response protocols

### Execution Process

1. Select a configured scenario
2. Set simulation parameters (duration, timestep)
3. Start the simulation
4. Monitor progress in real-time
5. Review results and generate reports

## Analysis and Reporting

### Visualization Tools

- **Spatial Maps**: Geographic analysis of deployments
- **Behavior Charts**: Agent decision patterns over time
- **Resource Tracking**: Equipment usage and logistics
- **Risk Assessment**: Probability calculations for incidents

### Export Options

- PDF reports
- CSV data exports
- Interactive charts (Plotly)
- API access for custom integrations

## Command Line Usage

For advanced users, the core simulation engine can be run directly:

```bash
python scripts/run_simulation.py --scenario <scenario_id> --duration 3600
```

## Best Practices

### Scenario Design

- Start with simple scenarios and gradually add complexity
- Validate agent capabilities against real-world data
- Test contingency protocols regularly

### Performance Optimization

- Use appropriate timestep intervals for your analysis needs
- Monitor resource usage during long simulations
- Archive completed scenarios to maintain performance

## Troubleshooting

### Common Issues

- **Simulation hangs**: Check agent configurations for infinite loops
- **Memory errors**: Reduce scenario complexity or increase system resources
- **Visualization fails**: Ensure matplotlib and plotly are properly installed

### Support

For technical issues, check the logs in the Django admin or contact the development team.
