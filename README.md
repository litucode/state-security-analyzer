# state-security-analyzer

## Software objective

Analyze the frequencies of variable changes over time to understand security phenomena in defined spaces, using behavior trees, geometry, and ballistic percentages to simulate impacts, evaluate officer down scenarios, and support strategic and operational evaluations.

## Description

This software provides spatial topography analysis and infrastructure displacement evaluation to optimize security deployments. It analyzes equipment and information with multiple variables to study unit compositions. The system organizes units into tactical teams by level and calculates incident probabilities to develop effective Officer Down (contingency) protocols. For example, if teams in the perimeter need to take cover but receive a casualty, the intervention may require specific equipment, which could be marked as unavailable and alter future plans.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment tool (venv, virtualenv, or conda)

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd state-security-analyzer
   ```

2. **Create and activate virtual environment:**

   ```bash
   # Using venv
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate

   # Or using conda
   conda create -n state-security-analyzer python=3.10
   conda activate state-security-analyzer
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`

For detailed installation instructions, see [docs/installation.md](docs/installation.md).

## Documentation

- **[Full Documentation](docs/)**: Complete project documentation
- **[User Guide](docs/user-guide.md)**: How to use the application
- **[API Reference](docs/api.md)**: REST API documentation
- **[Developer Guide](docs/developer-guide.md)**: Contributing and development
- **[Project Structure](docs/structure.md)**: Codebase architecture

## Key Features

- **Behavior Tree Simulation**: Models decision-making processes to assess intellectual and physical capacities of security agents through statistical analysis of mutable and immutable behaviors.
- **Infrastructure and Equipment Assessment**: Evaluates material assets, infrastructure, fixtures, fittings, plant, and equipment to optimize security deployments and resource allocation.
- **Spatial Intelligence**: Analyzes topography and perimeter measurements for efficient use of space in tactical operations.
- **Logistics Tracking**: Automates counting and reporting of ammunition, magazines, and other consumables to monitor resource usage.
- **Heliport and Route Optimization**: Identifies optimal extraction, reinforcement, and evacuation routes for rapid response in officer down scenarios.
- **Incident Probability Calculation**: Computes risks and develops contingency protocols based on unit compositions and environmental factors.

## What It Does

The software performs the following key functions to support security operations, evaluated by their role in enhancing security processes:

1. **Heliport Evaluation** (High Priority - Critical for rapid response): Assesses heliports to identify optimal routes for deploying reinforcement teams during officer down incidents, ensuring rapid response and evacuation. Evaluation: Essential for minimizing response times in high-risk scenarios.
2. **Spatial Analysis** (Medium Priority - Operational Efficiency): Evaluates measurements and topography to optimize space usage in tactical deployments, maximizing efficiency and coverage. Evaluation: Improves resource allocation and reduces operational blind spots.
3. **Ammunition Tracking** (High Priority - Resource Management): Monitors and reports ammunition and magazine usage, providing detailed counts for replenishment planning. Evaluation: Prevents shortages and supports accurate logistics forecasting.
4. **Behavior Tree Simulation** (Advanced - Capacity Assessment): Creates decision trees to model agent behaviors, analyzing intellectual and physical capacities through statistical evolution. Evaluation: Enables predictive modeling of human factors in security operations.
5. **Infrastructure Assessment** (Medium Priority - Asset Optimization): Analyzes material assets, fixtures, fittings, and equipment for suitability in security tasks. Evaluation: Identifies upgrades needed for better performance and safety.
6. **Contingency Planning** (High Priority - Risk Mitigation): Develops protocols for officer down scenarios, including equipment allocation and plan adjustments. Evaluation: Builds resilience against unforeseen events.
7. **Logistics Optimization** (Medium Priority - Supply Chain): Tracks consumables, personnel rotation, and supply chains for operational support. Evaluation: Ensures sustained operations at strategic and tactical levels.

## Behavior Tree Execution Cycle

The software operates on a time-based simulation loop where behavior trees drive agent decision-making and actions at regular intervals, creating a dynamic execution cycle that models security operations over time.

### Execution Timeline

1. **Timestep Definition**: System operates in discrete timesteps (configurable: 1 second, 5 seconds, 1 minute, etc.) or real-time continuous evaluation, allowing flexible simulation speeds for different operational scenarios.

2. **Per-Agent Cycle** (executes every timestep):
   - Read current state (environment conditions, inventory levels, threat detection, ally positions)
   - Evaluate behavior tree conditions and selectors
   - Select appropriate action node based on current context
   - Execute action and update agent state (position, resources, status)
   - Log action for analysis and incident probability calculation

3. **Per-Team Aggregation** (executes every N timesteps):
   - Aggregate individual agent actions into coordinated team behaviors
   - Resolve potential conflicts between agents (e.g., overlapping patrol routes)
   - Update team status, resource consumption, and equipment availability
   - Recalculate incident probability based on team dynamics

4. **Per-Operational Level Sync** (executes every M timesteps):
   - Tactical reports feed into operative level assessment
   - Operative adjustments trigger tactical redeployment
   - Strategic updates drive resource reallocations and policy changes

### Integration with Operational Cycles

- **Tactical Level**: Synchronized with rapid timesteps (real-time or near-real-time execution for immediate responses)
- **Operative Level**: Synchronized with medium intervals (every 5-10 minutes simulated for coordination)
- **Strategic Level**: Synchronized with long intervals (every hour/day simulated for planning)

### Agent Action Types Driven by Behavior Tree

- **Patrol**: Systematic movement through assigned sectors with threat scanning
- **Respond**: React to threat/incident detection with appropriate escalation
- **Take Cover**: Seek protective positions during active threats
- **Engage**: Initiate active response protocols (containment, neutralization)
- **Retreat**: Tactical withdrawal with minimal exposure
- **CASEVAC**: Coordinate casualty evacuation via optimal routes
- **Communicate**: Radio updates to command with status reports
- **Resource Management**: Monitor and report ammunition/fuel consumption

### State Persistence and Learning

- Each timestep updates agent state (fatigue levels, ammunition counts, position coordinates, health status)
- Historical action data informs future behavior tree decisions and probability calculations
- Incident probability dynamically recalculated based on action outcomes and environmental changes
- System learns from past incidents to optimize future behavior tree configurations

## Cycles (Operational Cycles)

This section outlines the operational cycles in execution order, explaining how the software processes data to provide insights for security operations. The cycles are structured hierarchically from strategic planning to tactical execution, ensuring comprehensive coverage of security needs.

### Strategic Level

Focuses on resource allocation and long-term risk assessment.

1. **Risk Assessment & Policy**: Defines critical threats and establishes general security objectives.
2. **Resource Management**: Handles budgetary distribution and long-term infrastructure acquisition.
3. **Intelligence Integration**: Analyzes historical data for macro-level preventive decision-making.

### Operative Level

Handles regional coordination and deployment logistics.

1. **Sectorization**: Divides terrain into zones of responsibility and assigns regional assets.
2. **Logistics Planning**: Coordinates supply chains (ammunition, fuel) and personnel rotation.
3. **Contingency Design**: Creates crisis response plans and evacuation/reinforcement routes.

### Tactical Level

Manages real-time field execution and unit maneuvering.

1. **Field Deployment**: Executes patrols, drone surveillance, and real-time SOF maneuvers.
2. **Live Engagement**: Manages active incidents, fire control, and ammunition consumption reports.
3. **Immediate Recovery**: Activates CASEVAC protocols for casualty evacuation and heliport extraction.

## Asset Classes

The software categorizes assets into the following classes and subclasses for comprehensive analysis:

- **Environment** – see [Structures](docs/classes/structures.md)
  - Space
  - Structures
  - Infrastructure

- **Vehicles** – see [Vehicles](docs/classes/vehicles.md)
  - **Ground**
    - Standard Patrol
    - Special Response Units (SRU)
  - **Air**
    - Rotary-wing (Helicopters)
    - UAVs (Drones)

- **Personal Equipment** – general items; refer to [security-force-member](docs/classes/security-force-member.md) for role‑based examples
  - Comms (Radio)
  - Bodycams
  - Weaponry
  - Uniforms
  - Tactical Footwear

- **Units** – see [Units](docs/classes/units.md)
  - K9
  - Special Operations Forces (SOF)
  - Two-man Patrols (Binomes)

- **Fixed Assets** – see [Fixed Assets](docs/classes/fixed-assets.md)
  - Base Equipment
  - Communication Towers
  - Surveillance Cameras and Systems
  - Barriers and Fencing
  - Storage Facilities

- **Personal Protective Equipment (PPE)** – see [PPE](docs/classes/ppe.md)
  - Helmets
  - Body Armor/Vests
  - Gloves
  - Boots
  - Eye Protection
  - Gas Masks

## Endpoints

The API provides RESTful endpoints for managing assets and generating reports. Each endpoint supports specific operations and query capabilities. Detailed documentation for data structures and query capabilities is provided below.

### Environment

- **GET** `/environment` - Retrieve a list of all environments or filter by parameters.
  - Query Parameters: `?type=structure`, `?location=zone_name`
  - Supported Queries: Filter by type, location, status
  - Not Supported: Complex nested filters, full-text search
  - Response Format: Array of environment objects with `id`, `type`, `location`, `status`, `capacity`

- **POST** `/environment` - Create a new environment entry.
  - Data Structure: `{ "type": "string", "location": "string", "status": "active|inactive", "capacity": "number" }`
  - Constraints: All fields required, location must be unique
  - File Structure: `/data/environment/`

- **PUT** `/environment/{id}` - Update an existing environment by ID.
  - Updateable Fields: `location`, `status`, `capacity`
  - Not Updateable: `type`, `id`, `created_date`

- **DELETE** `/environment/{id}` - Delete an environment by ID.
  - Constraints: Cannot delete if assigned to active units

### Vehicles

- **GET** `/vehicles` - Retrieve a list of all vehicles or filter by type (ground/air).
  - Query Parameters: `?type=ground|air`, `?status=operational|maintenance`
  - Supported Queries: Filter by type, status, unit assignment
  - Not Supported: Range queries on numeric fields
  - Response Format: Array of vehicle objects with `id`, `type`, `subtype`, `status`, `assignment`, `fuel_level`

- **POST** `/vehicles` - Create a new vehicle entry.
  - Data Structure: `{ "type": "ground|air", "subtype": "string", "status": "operational|maintenance", "assignment": "unit_id", "fuel_level": "number" }`
  - Constraints: Type and subtype required, fuel_level must be 0-100
  - File Structure: `/data/vehicles/`

- **PUT** `/vehicles/{id}` - Update an existing vehicle by ID.
  - Updateable Fields: `status`, `assignment`, `fuel_level`
  - Not Updateable: `type`, `subtype`, `id`

- **DELETE** `/vehicles/{id}` - Delete a vehicle by ID.
  - Constraints: Cannot delete if currently assigned to active unit

### Personal Equipment

- **GET** `/pe` - Retrieve a list of all personal equipment items.
  - Query Parameters: `?category=comms|weapons|uniform`, `?condition=new|serviceable|worn`
  - Supported Queries: Filter by category, condition, unit assignment, inventory count
  - Not Supported: Partial string matching, date range queries
  - Response Format: Array of equipment objects with `id`, `category`, `description`, `condition`, `count`, `assigned_to`

- **POST** `/pe` - Create a new personal equipment entry.
  - Data Structure: `{ "category": "string", "description": "string", "condition": "new|serviceable|worn", "count": "number", "assigned_to": "unit_id" }`
  - Constraints: Category and count required, count must be integer >= 0
  - File Structure: `/data/pe/`

- **PUT** `/pe/{id}` - Update an existing personal equipment item by ID.
  - Updateable Fields: `condition`, `count`, `assigned_to`
  - Not Updateable: `category`, `id`, `description`

- **DELETE** `/pe/{id}` - Delete a personal equipment item by ID.

### Fixed Assets

- **GET** `/fa` - Retrieve a list of all fixed assets.
  - Query Parameters: `?asset_type=base|tower|surveillance|barrier`, `?location=environment_id`
  - Supported Queries: Filter by asset type, location, operational status, maintenance schedule
  - Not Supported: Spatial queries, proximity searches
  - Response Format: Array of fixed asset objects with `id`, `asset_type`, `location`, `status`, `condition`, `last_maintenance`

- **POST** `/fa` - Create a new fixed asset entry.
  - Data Structure: `{ "asset_type": "string", "location": "environment_id", "status": "operational|maintenance", "condition": "excellent|good|fair|poor", "last_maintenance": "date" }`
  - Constraints: Asset_type and location required, location must exist
  - File Structure: `/data/fixed_assets/`

- **PUT** `/fa/{id}` - Update an existing fixed asset by ID.
  - Updateable Fields: `status`, `condition`, `last_maintenance`
  - Not Updateable: `asset_type`, `location`, `id`

- **DELETE** `/fa/{id}` - Delete a fixed asset by ID.
  - Constraints: Cannot delete if operational dependencies exist

### Units

- **GET** `/units` - Retrieve a list of all units or filter by type.
  - Query Parameters: `?type=k9|sof|binome`, `?status=active|standby|inactive`, `?location=environment_id`
  - Supported Queries: Filter by type, status, location, personnel count, equipment assignment
  - Not Supported: Hierarchical queries, multi-level filtering
  - Response Format: Array of unit objects with `id`, `type`, `size`, `status`, `location`, `equipment_assigned`

- **POST** `/units` - Create a new unit entry.
  - Data Structure: `{ "type": "k9|sof|binome", "size": "number", "status": "active|standby|inactive", "location": "environment_id", "equipment_assigned": ["pe_id", ...] }`
  - Constraints: Type and size required, size must be integer > 0
  - File Structure: `/data/units/`

- **PUT** `/units/{id}` - Update an existing unit by ID.
  - Updateable Fields: `status`, `location`, `equipment_assigned`, `size`
  - Not Updateable: `type`, `id`, `created_date`

- **DELETE** `/units/{id}` - Delete a unit by ID.
  - Constraints: Cannot delete if marked as active in incident logs

### Personal Protective Equipment (PPE)

- **GET** `/ppe` - Retrieve a list of all PPE items.
  - Query Parameters: `?type=helmet|armor|gloves|boots|eyewear|gas_mask`, `?stock_level=low|adequate|high`
  - Supported Queries: Filter by type, stock level, condition, unit assignment
  - Not Supported: Cost-based queries, supplier information
  - Response Format: Array of PPE objects with `id`, `type`, `stock_count`, `condition`, `assigned_units`, `expiration_date`

- **POST** `/ppe` - Create a new PPE entry.
  - Data Structure: `{ "type": "string", "stock_count": "number", "condition": "new|serviceable|worn", "assigned_units": ["unit_id", ...], "expiration_date": "date" }`
  - Constraints: Type and stock_count required, expiration_date must be future date
  - File Structure: `/data/ppe/`

- **PUT** `/ppe/{id}` - Update an existing PPE item by ID.
  - Updateable Fields: `stock_count`, `condition`, `assigned_units`, `expiration_date`
  - Not Updateable: `type`, `id`

- **DELETE** `/ppe/{id}` - Delete a PPE item by ID.

### Report

- **POST** `/report` - Create a new report based on asset data and analysis.
  - Data Structure: `{ "report_type": "incident|resource|logistics|capability", "filters": { "date_range": ["start_date", "end_date"], "location": "environment_id", "units": ["unit_id", ...] }, "include_analysis": "boolean" }`
  - Supported Report Types: Incident analysis, resource availability, logistics consumption, capability assessment
  - File Structure: `/data/reports/`
  - Response: Report object with `id`, `created_date`, `report_type`, `data`, `analysis`

- **GET** `/report` - Retrieve a list of reports or a specific report by ID (read-only after creation).
  - Query Parameters: `?report_id=id`, `?report_type=type`, `?date_from=date`, `?date_to=date`
  - Supported Queries: Filter by report type, date range, creator, status
  - Not Supported: Full-text search in report content, cross-report comparisons
  - Response Format: Array of report objects or single report object

- **Note**: Reports are not updatable or deletable once created to maintain data integrity and audit trail compliance.

### Data Structure File Organization

``` plain
/data/
├── environment/
│   └── environment_*.json
├── vehicles/
│   └── vehicles_*.json
├── pe/
│   └── equipment_*.json
├── fixed_assets/
│   └── fixed_assets_*.json
├── units/
│   └── units_*.json
├── ppe/
│   └── ppe_*.json
└── reports/
    └── report_*.json
```
