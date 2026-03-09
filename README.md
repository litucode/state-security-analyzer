# state-security-analyzer

## Software objective

Analyze the frequencies of variable changes over time to understand security phenomena in defined spaces, using behavior trees, geometry, and ballistic percentages to simulate impacts, evaluate officer down scenarios, and support strategic and operational evaluations.

## Description

This software provides spatial topography analysis and infrastructure displacement evaluation to optimize security deployments. It analyzes equipment and information with multiple variables to study unit compositions. The system organizes units into tactical teams by level and calculates incident probabilities to develop effective Officer Down (contingency) protocols. For example, if teams in the perimeter need to take cover but receive a casualty, the intervention may require specific equipment, which could be marked as unavailable and alter future plans.

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

- **Environment**
  - Space
  - Structures
  - Infrastructure

- **Vehicles**
  - **Ground**
    - Standard Patrol
    - Special Response Units (SRU)
  - **Air**
    - Rotary-wing (Helicopters)
    - UAVs (Drones)

- **Personal Equipment**
  - Comms (Radio)
  - Bodycams
  - Weaponry
  - Uniforms
  - Tactical Footwear

- **Units**
  - K9
  - Special Operations Forces (SOF)
  - Two-man Patrols (Binomes)

- **Fixed Assets**
  - Base Equipment
  - Communication Towers
  - Surveillance Cameras and Systems
  - Barriers and Fencing
  - Storage Facilities

- **Personal Protective Equipment (PPE)**
  - Helmets
  - Body Armor/Vests
  - Gloves
  - Boots
  - Eye Protection
  - Gas Masks

## Getting Started

Install dependencies

    pip install -r requirements.txt

Run

    python main.py

## Endpoints

The API provides RESTful endpoints for managing assets and generating reports. All endpoints support standard HTTP methods where applicable.

### Environment

- **GET** `/environment` - Retrieve a list of all environments or filter by parameters.
- **POST** `/environment` - Create a new environment entry.
- **PUT** `/environment/{id}` - Update an existing environment by ID.
- **DELETE** `/environment/{id}` - Delete an environment by ID.

### Vehicles

- **GET** `/vehicles` - Retrieve a list of all vehicles or filter by type (ground/air).
- **POST** `/vehicles` - Create a new vehicle entry.
- **PUT** `/vehicles/{id}` - Update an existing vehicle by ID.
- **DELETE** `/vehicles/{id}` - Delete a vehicle by ID.

### Personal Equipment

- **GET** `/pe` - Retrieve a list of all personal equipment items.
- **POST** `/pe` - Create a new personal equipment entry.
- **PUT** `/pe/{id}` - Update an existing personal equipment item by ID.
- **DELETE** `/pe/{id}` - Delete a personal equipment item by ID.

### Fixed Assets

- **GET** `/fa` - Retrieve a list of all fixed assets.
- **POST** `/fa` - Create a new fixed asset entry.
- **PUT** `/fa/{id}` - Update an existing fixed asset by ID.
- **DELETE** `/fa/{id}` - Delete a fixed asset by ID.

### Units

- **GET** `/units` - Retrieve a list of all units or filter by type.
- **POST** `/units` - Create a new unit entry.
- **PUT** `/units/{id}` - Update an existing unit by ID.
- **DELETE** `/units/{id}` - Delete a unit by ID.

### Personal Protective Equipment (PPE)

- **GET** `/ppe` - Retrieve a list of all PPE items.
- **POST** `/ppe` - Create a new PPE entry.
- **PUT** `/ppe/{id}` - Update an existing PPE item by ID.
- **DELETE** `/ppe/{id}` - Delete a PPE item by ID.

### Report

- **POST** `/report` - Create a new report based on asset data and analysis.
- **GET** `/report` - Retrieve a list of reports or a specific report by ID (read-only after creation).
- **Note**: Reports are not updatable or deletable once created to maintain data integrity.
