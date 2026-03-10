from django.contrib import admin
from .models import (
    SecurityForceMember,
    EquipmentCategory,
    Equipment,
    RoleEquipmentAssignment,
    MemberEquipmentAssignment,
    Unit,
    K9Unit,
    SOFUnit,
    Vehicle,
    ArmoredVehicle,
    Helicopter,
    UAV,
    Space,
    Structure,
    Infrastructure,
    FixedAsset,
    Generator,
    CommunicationTower,
    SurveillanceCamera,
)


# Security Force Members
@admin.register(SecurityForceMember)
class SecurityForceMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'badge_number', 'role', 'rank', 'is_armed', 'is_active')
    list_filter = ('role', 'is_armed', 'is_active')
    search_fields = ('name', 'badge_number', 'rank')
    ordering = ('name',)


# Equipment Management
@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    list_filter = ('parent_category',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'equipment_type', 'category', 'protection_level', 'is_restricted')
    list_filter = ('equipment_type', 'protection_level', 'is_restricted', 'category')
    search_fields = ('name', 'description')


@admin.register(RoleEquipmentAssignment)
class RoleEquipmentAssignmentAdmin(admin.ModelAdmin):
    list_display = ('role', 'equipment', 'requirement_level')
    list_filter = ('role', 'requirement_level')
    search_fields = ('equipment__name',)


@admin.register(MemberEquipmentAssignment)
class MemberEquipmentAssignmentAdmin(admin.ModelAdmin):
    list_display = ('member', 'equipment', 'quantity', 'condition', 'is_active')
    list_filter = ('condition', 'is_active', 'assignment_date')
    search_fields = ('member__name', 'equipment__name')


# Units
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_type', 'team_leader', 'is_active')
    list_filter = ('unit_type', 'is_active')
    search_fields = ('name', 'team_leader__name')


@admin.register(K9Unit)
class K9UnitAdmin(admin.ModelAdmin):
    list_display = ('canine_name', 'canine_breed', 'handler', 'is_active')
    list_filter = ('canine_breed', 'is_active')
    search_fields = ('canine_name', 'handler__name')


@admin.register(SOFUnit)
class SOFUnitAdmin(admin.ModelAdmin):
    list_display = ('unit', 'team_size', 'training_level', 'is_active')
    list_filter = ('training_level', 'is_active')
    search_fields = ('unit__name',)


# Vehicles
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration', 'vehicle_type', 'condition', 'is_operational')
    list_filter = ('vehicle_type', 'condition', 'is_operational')
    search_fields = ('name', 'registration', 'model')


@admin.register(ArmoredVehicle)
class ArmoredVehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'armor_rating', 'has_thermal_imaging', 'has_nbc_filtration')
    list_filter = ('armor_rating', 'has_thermal_imaging', 'has_nbc_filtration')


@admin.register(Helicopter)
class HelicopterAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'has_hoist_system', 'has_thermal_imaging', 'endurance_hours')
    list_filter = ('has_hoist_system', 'has_thermal_imaging')


@admin.register(UAV)
class UAVAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'has_optical_camera', 'has_thermal_camera', 'endurance_minutes')
    list_filter = ('has_optical_camera', 'has_thermal_camera')


# Structures & Infrastructure
@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'floor_area_m2', 'capacity')
    list_filter = ('category', 'has_backup_power', 'has_surveillance')
    search_fields = ('name', 'description')


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'structure_type', 'location', 'capacity')
    list_filter = ('structure_type', 'has_backup_power', 'has_surveillance_system')
    search_fields = ('name', 'location')


@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'infrastructure_type', 'location', 'condition')
    list_filter = ('infrastructure_type', 'condition')
    search_fields = ('name', 'location')


# Fixed Assets
@admin.register(FixedAsset)
class FixedAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'asset_type', 'location', 'condition', 'is_operational')
    list_filter = ('asset_type', 'condition', 'is_operational')
    search_fields = ('name', 'location__name')


@admin.register(Generator)
class GeneratorAdmin(admin.ModelAdmin):
    list_display = ('fixed_asset', 'fuel_type', 'capacity_kw', 'fuel_capacity_liters')
    list_filter = ('fuel_type',)
    search_fields = ('fixed_asset__name',)


@admin.register(CommunicationTower)
class CommunicationTowerAdmin(admin.ModelAdmin):
    list_display = ('fixed_asset', 'tower_type', 'height_meters', 'antenna_count', 'coverage_range_km')
    list_filter = ('tower_type', 'has_encryption')
    search_fields = ('fixed_asset__name',)


@admin.register(SurveillanceCamera)
class SurveillanceCameraAdmin(admin.ModelAdmin):
    list_display = ('fixed_asset', 'camera_type', 'resolution', 'viewing_angle_degrees')
    list_filter = ('camera_type', 'resolution', 'has_recording')
    search_fields = ('fixed_asset__name',)
