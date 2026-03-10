"""Domain classes for the various asset types described in the
`docs/classes` folder.

Each section of the documentation (fixed assets, structures, vehicles,
PPE, security force members, units) has a corresponding Python class or
set of classes below.  The goal of these classes is to provide a typed
representation of the concepts used throughout the simulator and the
Django apps.  They are intentionally lightweight and mostly act as
containers for data; further behavior can be added as the engine
evolves.

The attributes in the dataclasses mirror the categories and
specifications called out in the markdown files.  In many cases the
"specs" attribute is simply a catch-all dictionary since the examples
in the docs are varied and often non‑exhaustive.

Developers can import these classes from `core.assets` when building
scenario models, inventory systems or other parts of the simulation
that need to reason about physical assets, personnel, vehicles, etc.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Fixed assets
# ---------------------------------------------------------------------------

@dataclass
class FixedAsset:
    """Base class for any asset that is permanently (or semi-permanently)
    installed in the environment.

    ``asset_type`` should be one of the high level categories used in
    ``docs/classes/fixed-assets.md`` such as ``"Base Equipment"`` or
    ``"Communication Tower"``.  ``specs`` is an open dictionary that
    callers can populate with whatever parameters are relevant for the
    concrete subtype.
    """

    name: str
    asset_type: str = ""  # subclasses set a default in __post_init__
    description: Optional[str] = None
    specs: Dict[str, Any] = field(default_factory=dict)


@dataclass
class BaseEquipment(FixedAsset):
    """Represents infrastructure like generators, HVAC, water systems,
    etc.  The ``specs`` dictionary typically contains capacity, runtime
    and maintenance parameters.  """

    def __post_init__(self):
        self.asset_type = "Base Equipment"


@dataclass
class CommunicationTower(FixedAsset):
    """Tower used for encrypted radio transmissions as described in the
    docs.  Common fields include height, structure, footprint and
    frequency/coverage data.
    """

    height_m: Optional[float] = None
    structure: Optional[str] = None  # lattice, monopole, guyed, etc.
    footprint_m2: Optional[float] = None
    specs: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.asset_type = "Communication Tower"


@dataclass
class SurveillanceSystem(FixedAsset):
    """Encapsulates cameras and related monitoring equipment.  ``specs``
    might include resolution, range, optics type, and so on.
    """

    camera_type: Optional[str] = None  # PTZ, fixed dome, thermal, etc.
    specs: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.asset_type = "Surveillance System"


@dataclass
class Barrier(FixedAsset):
    """Fencing, barricades or other physical obstacles used for access
    control and perimeter security.
    """

    barrier_type: Optional[str] = None  # fence, bollard, concertina, etc.
    material: Optional[str] = None

    def __post_init__(self) -> None:
        self.asset_type = "Barrier"


# ---------------------------------------------------------------------------
# Structures (environmental assets)
# ---------------------------------------------------------------------------

@dataclass
class Space:
    """A discrete area within or adjacent to a structure.  See
    ``docs/classes/structures.md``.
    """

    name: str
    purpose: Optional[str] = None
    floor_area_m2: Optional[float] = None
    ceiling_height_m: Optional[float] = None
    access_control: Optional[str] = None
    lighting: Optional[str] = None
    security_features: List[str] = field(default_factory=list)
    fixed_assets: List[FixedAsset] = field(default_factory=list)


@dataclass
class Structure:
    """A building or facility that houses spaces and fixed assets.
    """

    name: str
    structure_type: Optional[str] = None  # e.g. TOC, armory, barracks
    construction_material: Optional[str] = None
    perimeter_security: Optional[str] = None
    spaces: List[Space] = field(default_factory=list)
    fixed_assets: List[FixedAsset] = field(default_factory=list)


@dataclass
class Infrastructure:
    """Large-scale systems such as roads, fences, utilities, etc.
    """

    name: str
    infrastructure_type: Optional[str] = None  # road, HLZ, fence, etc.
    specs: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Vehicles
# ---------------------------------------------------------------------------

@dataclass
class Vehicle:
    """Generic vehicle class; ``category`` is "Ground" or "Air".
    ``subtype`` corresponds to the detailed types described in
    ``docs/classes/vehicles.md``.
    """

    name: str
    category: str  # ground/air
    subtype: Optional[str] = None
    specs: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Personal Protective Equipment
# ---------------------------------------------------------------------------

@dataclass
class PPEItem:
    """Represents a piece of personal protective equipment (helmet,
    vest, gloves, etc.).
    """

    name: str
    category: Optional[str] = None  # helmet, body armor, boots, etc.
    features: List[str] = field(default_factory=list)
    specs: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Security force member definitions
# ---------------------------------------------------------------------------

@dataclass
class SecurityForceMember:
    """A generic security personnel profile; ``role`` is one of the
    types defined in ``docs/classes/security-force-member.md`` (transit,
    patrol, intervention, special intervention).
    """

    role: str
    personal_equipment: List[str] = field(default_factory=list)
    protective_equipment: List[PPEItem] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Units
# ---------------------------------------------------------------------------

@dataclass
class Unit:
    """Base class for any organized team of personnel.
    """

    name: str
    personnel_count: int
    roles: List[str] = field(default_factory=list)
    equipment: List[Any] = field(default_factory=list)  # could be PPEItem/Vehicle


@dataclass
class K9Unit(Unit):
    """Canine unit with handler and dog-specific attributes.
    """

    canine_breed: Optional[str] = None
    canine_certifications: List[str] = field(default_factory=list)
    handler_equipment: List[Any] = field(default_factory=list)


@dataclass
class SOFUnit(Unit):
    """Special Operations Forces team.
    """

    team_leader: Optional[str] = None
    deputy_leader: Optional[str] = None
    operator_roles: List[str] = field(default_factory=list)
    support_roles: List[str] = field(default_factory=list)


@dataclass
class Binome(Unit):
    """Two‑man patrol.
    """

    senior_officer: Optional[str] = None
    support_officer: Optional[str] = None


# End of file
