from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# ==================== SECURITY FORCE MEMBER ====================

class SecurityForceMember(models.Model):
    """Represents a security force member with role-specific attributes."""
    
    ROLE_CHOICES = [
        ('transit', 'Transit Agent'),
        ('patrol', 'Patrol Officer'),
        ('intervention', 'Intervention Team Member'),
        ('special_intervention', 'Special Intervention Operator'),
    ]
    
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    rank = models.CharField(max_length=100, blank=True)
    badge_number = models.CharField(max_length=50, unique=True)
    is_armed = models.BooleanField(default=True)
    years_of_service = models.PositiveIntegerField(default=0)
    certifications = models.TextField(blank=True, help_text="Comma-separated list of certifications")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return f"{self.get_role_display()} - {self.name} ({self.badge_number})"


# ==================== EQUIPMENT ====================

class EquipmentCategory(models.Model):
    """Categorizes equipment for organization and filtering."""
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategories'
    )
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Equipment Categories"
        
    def __str__(self):
        return self.name


class Equipment(models.Model):
    """Represents individual equipment items that can be assigned to security force members."""
    
    EQUIPMENT_TYPE_CHOICES = [
        ('personal', 'Personal Equipment'),
        ('protective', 'Protective Equipment'),
    ]
    
    PROTECTION_LEVEL_CHOICES = [
        ('none', 'None'),
        ('basic', 'Basic'),
        ('level_ii', 'Level II'),
        ('level_iiia', 'Level IIIA'),
        ('level_iii', 'Level III'),
        ('level_iv', 'Level IV'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.ForeignKey(EquipmentCategory, on_delete=models.SET_NULL, null=True)
    equipment_type = models.CharField(max_length=20, choices=EQUIPMENT_TYPE_CHOICES)
    description = models.TextField(blank=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cost_range = models.CharField(
        max_length=20,
        choices=[('budget', 'Budget'), ('mid', 'Mid-Range'), ('premium', 'Premium')],
        blank=True
    )
    protection_level = models.CharField(
        max_length=20,
        choices=PROTECTION_LEVEL_CHOICES,
        default='none',
        blank=True
    )
    maintenance_schedule = models.CharField(max_length=100, blank=True, help_text="e.g., 'Every 6 months'")
    expected_lifespan_years = models.PositiveIntegerField(null=True, blank=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags (lethal, non-lethal, ballistic, etc.)")
    is_restricted = models.BooleanField(default=False, help_text="Requires special authorization")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class RoleEquipmentAssignment(models.Model):
    """Specifies which equipment is required, optional, or prohibited for each role."""
    
    REQUIREMENT_LEVEL_CHOICES = [
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('prohibited', 'Prohibited'),
    ]
    
    role = models.CharField(
        max_length=20,
        choices=SecurityForceMember.ROLE_CHOICES
    )
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    requirement_level = models.CharField(max_length=20, choices=REQUIREMENT_LEVEL_CHOICES)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('role', 'equipment')
        ordering = ['role', 'requirement_level']
        
    def __str__(self):
        return f"{self.get_role_display()} - {self.equipment.name}: {self.get_requirement_level_display()}"


class MemberEquipmentAssignment(models.Model):
    """Tracks equipment assigned to individual security force members."""
    
    member = models.ForeignKey(SecurityForceMember, on_delete=models.CASCADE, related_name='equipment_assignments')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    assignment_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    condition = models.CharField(
        max_length=20,
        choices=[('excellent', 'Excellent'), ('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')],
        default='excellent'
    )
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('member', 'equipment', 'is_active')
        ordering = ['-assignment_date']
        
    def __str__(self):
        return f"{self.member.name} - {self.equipment.name} (x{self.quantity})"


# ==================== UNITS ====================

class Unit(models.Model):
    """Represents organized tactical formations of security personnel."""
    
    UNIT_TYPE_CHOICES = [
        ('k9', 'K9 Unit'),
        ('sof', 'Special Operations Forces (SOF)'),
        ('binome', 'Two-man Patrol (Binome)'),
    ]
    
    name = models.CharField(max_length=200)
    unit_type = models.CharField(max_length=20, choices=UNIT_TYPE_CHOICES)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    team_leader = models.ForeignKey(
        SecurityForceMember,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='led_units'
    )
    members = models.ManyToManyField(SecurityForceMember, related_name='units', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name} ({self.get_unit_type_display()})"


class K9Unit(models.Model):
    """Specialization for K9 units."""
    
    CANINE_BREED_CHOICES = [
        ('german_shepherd', 'German Shepherd'),
        ('belgian_malinois', 'Belgian Malinois'),
        ('labrador', 'Labrador Retriever'),
        ('other', 'Other'),
    ]
    
    SPECIALIZATION_CHOICES = [
        ('narcotics', 'Narcotics Detection'),
        ('explosives', 'Explosives Detection'),
        ('tracking', 'Tracking'),
        ('apprehension', 'Apprehension'),
        ('area_denial', 'Area Denial'),
    ]
    
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='k9_unit')
    handler = models.ForeignKey(SecurityForceMember, on_delete=models.SET_NULL, null=True, related_name='k9_handler')
    canine_name = models.CharField(max_length=100)
    canine_breed = models.CharField(max_length=20, choices=CANINE_BREED_CHOICES)
    canine_age_years = models.DecimalField(max_digits=3, decimal_places=1)
    specializations = models.CharField(max_length=200, help_text="Comma-separated specializations")
    certification_date = models.DateField(null=True, blank=True)
    work_hours_per_shift = models.PositiveIntegerField(default=4, validators=[MinValueValidator(1), MaxValueValidator(12)])
    rest_hours_required = models.PositiveIntegerField(default=8, validators=[MinValueValidator(4), MaxValueValidator(24)])
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"K9 {self.canine_name} ({self.unit.name})"


class SOFUnit(models.Model):
    """Specialization for Special Operations Forces units."""
    
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='sof_unit')
    team_size = models.PositiveIntegerField(validators=[MinValueValidator(6), MaxValueValidator(12)])
    team_leader = models.ForeignKey(
        SecurityForceMember,
        on_delete=models.SET_NULL,
        null=True,
        related_name='sof_leadership'
    )
    specializations = models.CharField(
        max_length=500,
        blank=True,
        help_text="e.g., CQB, hostage rescue, counter-terrorism, dynamic entry"
    )
    training_level = models.CharField(
        max_length=20,
        choices=[('basic', 'Basic'), ('advanced', 'Advanced'), ('elite', 'Elite')],
        default='advanced'
    )
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"SOF {self.unit.name} (Size: {self.team_size})"


# ==================== VEHICLES ====================

class Vehicle(models.Model):
    """Represents motorized and aerial assets."""
    
    VEHICLE_TYPE_CHOICES = [
        ('patrol_ground', 'Ground - Standard Patrol'),
        ('sru_ground', 'Ground - Special Response Unit (SRU)'),
        ('helicopter', 'Air - Rotary-wing (Helicopter)'),
        ('uav', 'Air - UAV (Drone)'),
    ]
    
    CONDITION_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('maintenance', 'In Maintenance'),
    ]
    
    name = models.CharField(max_length=200)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    registration = models.CharField(max_length=50, unique=True)
    model = models.CharField(max_length=100, blank=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    
    # Capacity
    seating_capacity = models.PositiveIntegerField(default=2)
    payload_capacity_kg = models.PositiveIntegerField(null=True, blank=True)
    
    # Performance
    max_speed_kmh = models.PositiveIntegerField(null=True, blank=True)
    range_km = models.PositiveIntegerField(null=True, blank=True)
    
    # Status
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='good')
    is_operational = models.BooleanField(default=True)
    assigned_unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, related_name='vehicles')
    
    # Maintenance
    last_maintenance_date = models.DateField(null=True, blank=True)
    next_maintenance_date = models.DateField(null=True, blank=True)
    odometer_km = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name} ({self.registration})"


class ArmoredVehicle(models.Model):
    """Specialization for armored SRU vehicles."""
    
    ARMOR_RATING_CHOICES = [
        ('b6', 'Level B6'),
        ('b7', 'Level B7'),
    ]
    
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name='armored_specs')
    armor_rating = models.CharField(max_length=10, choices=ARMOR_RATING_CHOICES)
    has_thermal_imaging = models.BooleanField(default=False)
    has_nbc_filtration = models.BooleanField(default=False)
    has_weapon_mounting = models.BooleanField(default=False)
    fuel_capacity_liters = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Armored {self.vehicle.name} ({self.armor_rating})"


class Helicopter(models.Model):
    """Specialization for helicopter assets."""
    
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name='helicopter_specs')
    has_hoist_system = models.BooleanField(default=True)
    has_thermal_imaging = models.BooleanField(default=True)
    has_door_guns = models.BooleanField(default=False)
    has_rappel_system = models.BooleanField(default=True)
    endurance_hours = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    operational_ceiling_meters = models.PositiveIntegerField(null=True, blank=True)
    fuel_capacity_liters = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Helicopters"
        
    def __str__(self):
        return f"Helicopter {self.vehicle.name}"


class UAV(models.Model):
    """Specialization for UAV (drone) assets."""
    
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name='uav_specs')
    has_optical_camera = models.BooleanField(default=True)
    has_thermal_camera = models.BooleanField(default=True)
    has_obstacle_avoidance = models.BooleanField(default=True)
    endurance_minutes = models.PositiveIntegerField(null=True, blank=True)
    operational_altitude_meters = models.PositiveIntegerField(null=True, blank=True)
    max_range_km = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "UAVs"
        
    def __str__(self):
        return f"UAV {self.vehicle.name}"


# ==================== STRUCTURES & INFRASTRUCTURE ====================

class Space(models.Model):
    """Represents defined areas within or adjacent to structures."""
    
    SPACE_CATEGORY_CHOICES = [
        ('operational', 'Operational'),
        ('logistical', 'Logistical'),
        ('personnel', 'Personnel'),
        ('support', 'Support'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=SPACE_CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    floor_area_m2 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    ceiling_height_m = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True, help_text="Maximum number of personnel")
    has_backup_power = models.BooleanField(default=False)
    has_environmental_control = models.BooleanField(default=False)
    has_surveillance = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Structure(models.Model):
    """Represents permanent or semi-permanent physical buildings."""
    
    STRUCTURE_TYPE_CHOICES = [
        ('toc', 'Tactical Operations Center'),
        ('station', 'Police/Security Station'),
        ('headquarters', 'Regional Headquarters'),
        ('barracks', 'Barracks/Base Housing'),
        ('armory', 'Armory/Weapons Facility'),
        ('training', 'Training Facility'),
        ('hangar', 'Hangar/Vehicle Maintenance'),
        ('detention', 'Detention Facility'),
        ('checkpoint', 'Checkpoint/Guard Post'),
        ('bunker', 'Fortified Bunker/Observation Post'),
        ('fob', 'Forward Operating Base'),
        ('medical', 'Medical Clinic/Hospital'),
        ('warehouse', 'Supply Warehouse'),
        ('maintenance', 'Maintenance & Repair Shop'),
        ('it_center', 'IT/Communications Center'),
    ]
    
    name = models.CharField(max_length=200)
    structure_type = models.CharField(max_length=20, choices=STRUCTURE_TYPE_CHOICES)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    
    # Physical specs
    construction_material = models.CharField(max_length=100, blank=True)
    Floor_count = models.PositiveIntegerField(default=1)
    capacity = models.PositiveIntegerField(null=True, blank=True, help_text="Maximum number of personnel")
    
    # Features
    has_perimeter_fencing = models.BooleanField(default=True)
    has_access_control = models.BooleanField(default=True)
    has_backup_power = models.BooleanField(default=True)
    has_communication_tower = models.BooleanField(default=False)
    has_surveillance_system = models.BooleanField(default=True)
    
    spaces = models.ManyToManyField(Space, blank=True, related_name='structures')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name} ({self.get_structure_type_display()})"


class Infrastructure(models.Model):
    """Represents large-scale systems and installations connecting structures."""
    
    INFRASTRUCTURE_TYPE_CHOICES = [
        ('primary_road', 'Primary Roads/Access Routes'),
        ('secondary_road', 'Secondary Roads/Patrol Routes'),
        ('hlz', 'Heliport/HLZ'),
        ('rally_point', 'Rally Points'),
        ('perimeter_fence', 'Perimeter Fencing'),
        ('barriers', 'Vehicle Barriers/Obstacles'),
        ('checkpoint', 'Checkpoints/Guard Stations'),
    ]
    
    name = models.CharField(max_length=200)
    infrastructure_type = models.CharField(max_length=20, choices=INFRASTRUCTURE_TYPE_CHOICES)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    
    # Infrastructure specs
    length_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    condition = models.CharField(
        max_length=20,
        choices=[('excellent', 'Excellent'), ('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')],
        default='good'
    )
    
    connected_structures = models.ManyToManyField(Structure, blank=True, related_name='connected_by_infrastructure')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Infrastructure"
        
    def __str__(self):
        return f"{self.name} ({self.get_infrastructure_type_display()})"


# ==================== FIXED ASSETS ====================

class FixedAsset(models.Model):
    """Represents fixed installations enhancing security operations."""
    
    ASSET_TYPE_CHOICES = [
        ('base_equipment', 'Base Equipment'),
        ('generator', 'Generator'),
        ('hvac', 'HVAC System'),
        ('water_system', 'Water System'),
        ('comm_equipment', 'Communications Equipment'),
        ('comms_tower', 'Communication Tower'),
        ('camera', 'Surveillance Camera'),
        ('barrier', 'Barrier/Fencing'),
    ]
    
    name = models.CharField(max_length=200)
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPE_CHOICES)
    description = models.TextField(blank=True)
    location = models.ForeignKey(Structure, on_delete=models.SET_NULL, null=True, blank=True, related_name='fixed_assets')
    
    # Asset tracking
    acquisition_date = models.DateField(null=True, blank=True)
    expected_lifespan_years = models.PositiveIntegerField(null=True, blank=True)
    last_maintenance_date = models.DateField(null=True, blank=True)
    next_maintenance_date = models.DateField(null=True, blank=True)
    
    condition = models.CharField(
        max_length=20,
        choices=[('excellent', 'Excellent'), ('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor'), ('non-operational', 'Non-operational')],
        default='good'
    )
    is_operational = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name} ({self.get_asset_type_display()})"


class Generator(models.Model):
    """Specialization for generator assets."""
    
    FUEL_TYPE_CHOICES = [
        ('diesel', 'Diesel'),
        ('gasoline', 'Gasoline'),
        ('hybrid', 'Hybrid'),
    ]
    
    fixed_asset = models.OneToOneField(FixedAsset, on_delete=models.CASCADE, related_name='generator_specs')
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    capacity_kw = models.PositiveIntegerField()
    fuel_capacity_liters = models.PositiveIntegerField()
    fuel_consumption_liters_per_hour = models.DecimalField(max_digits=5, decimal_places=1)
    has_automatic_transfer_switch = models.BooleanField(default=True)
    noise_level_db = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Generator {self.capacity_kw}kW - {self.fixed_asset.name}"


class CommunicationTower(models.Model):
    """Specialization for communication tower assets."""
    
    TOWER_TYPE_CHOICES = [
        ('lattice', 'Lattice Tower'),
        ('monopole', 'Monopole Tower'),
        ('guyed', 'Guyed Tower'),
    ]
    
    fixed_asset = models.OneToOneField(FixedAsset, on_delete=models.CASCADE, related_name='tower_specs')
    tower_type = models.CharField(max_length=20, choices=TOWER_TYPE_CHOICES)
    height_meters = models.DecimalField(max_digits=6, decimal_places=1)
    antenna_count = models.PositiveIntegerField(default=2)
    transmission_power_watts = models.PositiveIntegerField(default=100)
    coverage_range_km = models.DecimalField(max_digits=6, decimal_places=1)
    has_encryption = models.BooleanField(default=True)
    backup_power_hours = models.DecimalField(max_digits=5, decimal_places=1)
    
    class Meta:
        verbose_name_plural = "Communication Towers"
        
    def __str__(self):
        return f"{self.tower_type} - {self.fixed_asset.name}"


class SurveillanceCamera(models.Model):
    """Specialization for surveillance camera assets."""
    
    CAMERA_TYPE_CHOICES = [
        ('ptz', 'Pan/Tilt/Zoom (PTZ)'),
        ('fixed_dome', 'Fixed Dome'),
        ('thermal', 'Thermal/FLIR'),
        ('hybrid', 'Hybrid Optical/Thermal'),
    ]
    
    fixed_asset = models.OneToOneField(FixedAsset, on_delete=models.CASCADE, related_name='camera_specs')
    camera_type = models.CharField(max_length=20, choices=CAMERA_TYPE_CHOICES)
    resolution = models.CharField(max_length=50, choices=[('1080p', '1080p Full HD'), ('2k', '2K'), ('4k', '4K UHD')])
    viewing_angle_degrees = models.PositiveIntegerField()
    night_vision_range_m = models.PositiveIntegerField(null=True, blank=True)
    has_recording = models.BooleanField(default=True)
    recording_storage_gb = models.PositiveIntegerField(null=True, blank=True)
    frame_rate_fps = models.PositiveIntegerField(default=30)
    
    def __str__(self):
        return f"{self.camera_type} - {self.fixed_asset.name}"
