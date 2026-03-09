# API Reference

The `state-security-analyzer` provides a REST API for programmatic access to simulation capabilities.

## Base URL

```
http://localhost:8000/api/
```

## Authentication

Currently, the API does not require authentication for development. In production, implement appropriate authentication mechanisms.

## Endpoints

### Scenarios

#### GET /api/scenarios/

List all scenarios.

**Response:**

```json
[
  {
    "id": 1,
    "name": "Perimeter Defense",
    "description": "Standard perimeter security scenario",
    "created_at": "2024-01-01T00:00:00Z",
    "status": "active"
  }
]
```

#### POST /api/scenarios/

Create a new scenario.

**Request Body:**

```json
{
  "name": "New Scenario",
  "description": "Description of the scenario",
  "parameters": {
    "agents": 10,
    "area": "500x500m"
  }
}
```

#### GET /api/scenarios/{id}/

Get scenario details.

#### PUT /api/scenarios/{id}/

Update scenario.

#### DELETE /api/scenarios/{id}/

Delete scenario.

### Simulations

#### POST /api/simulations/

Start a new simulation.

**Request Body:**

```json
{
  "scenario_id": 1,
  "duration": 3600,
  "timestep": 1.0
}
```

**Response:**

```json
{
  "id": 1,
  "status": "running",
  "start_time": "2024-01-01T00:00:00Z",
  "progress": 0.0
}
```

#### GET /api/simulations/{id}/

Get simulation status and results.

#### GET /api/simulations/{id}/results/

Get detailed simulation results.

### Analysis

#### GET /api/analysis/risk/

Get risk assessment data.

#### GET /api/analysis/spatial/

Get spatial analysis data.

#### GET /api/analysis/logistics/

Get logistics and resource data.

## Data Formats

### Scenario Object

```json
{
  "id": "integer",
  "name": "string",
  "description": "string",
  "parameters": "object",
  "created_at": "datetime",
  "updated_at": "datetime",
  "status": "string"
}
```

### Simulation Object

```json
{
  "id": "integer",
  "scenario_id": "integer",
  "status": "string",
  "start_time": "datetime",
  "end_time": "datetime",
  "duration": "integer",
  "timestep": "float",
  "results": "object"
}
```

## Error Handling

The API returns standard HTTP status codes:

- `200`: Success
- `201`: Created
- `400`: Bad Request
- `404`: Not Found
- `500`: Internal Server Error

Error responses include a JSON object with error details:

```json
{
  "error": "Description of the error",
  "code": "ERROR_CODE"
}
```

## Rate Limiting

Currently no rate limiting is implemented. Consider implementing appropriate limits for production use.

## Versioning

The API is versioned. Current version is v1. Include version in URL path:

```
/api/v1/scenarios/
```

## SDKs and Libraries

No official SDKs are available yet. Use standard HTTP clients or REST libraries in your preferred language.
