import unittest

from core import assets


class AssetClassesTest(unittest.TestCase):
    def test_fixed_asset_subclasses(self):
        base = assets.BaseEquipment(name="Generator", description="Backup power")
        self.assertEqual(base.asset_type, "Base Equipment")
        tower = assets.CommunicationTower(name="Tower 1", height_m=45)
        self.assertEqual(tower.asset_type, "Communication Tower")
        cam = assets.SurveillanceSystem(name="PTZ Cam", camera_type="PTZ")
        self.assertEqual(cam.asset_type, "Surveillance System")
        barrier = assets.Barrier(name="Chain Link Fence", barrier_type="Fence")
        self.assertEqual(barrier.asset_type, "Barrier")

    def test_structure_space_infrastructure(self):
        space = assets.Space(name="Command Center", purpose="Operations")
        self.assertIn("Operations", space.purpose)
        structure = assets.Structure(name="Main Base", structure_type="TOC")
        structure.spaces.append(space)
        self.assertEqual(structure.spaces[0].name, "Command Center")
        infra = assets.Infrastructure(name="Main Road", infrastructure_type="Road")
        self.assertEqual(infra.infrastructure_type, "Road")

    def test_vehicle_and_ppe(self):
        vehicle = assets.Vehicle(name="Patrol SUV", category="Ground", subtype="Standard Patrol")
        self.assertEqual(vehicle.category, "Ground")
        ppe = assets.PPEItem(name="Kevlar Helmet", category="Helmet")
        self.assertEqual(ppe.category, "Helmet")

    def test_security_force_member(self):
        member = assets.SecurityForceMember(role="Patrol")
        self.assertEqual(member.role, "Patrol")

    def test_units(self):
        k9 = assets.K9Unit(name="K9 Alpha", personnel_count=2, canine_breed="Belgian Malinois")
        self.assertEqual(k9.canine_breed, "Belgian Malinois")
        sof = assets.SOFUnit(name="SOF Team", personnel_count=8, team_leader="Leader A")
        self.assertEqual(sof.team_leader, "Leader A")
        binome = assets.Binome(name="Binome 1", personnel_count=2, senior_officer="Officer 1")
        self.assertEqual(binome.senior_officer, "Officer 1")


if __name__ == '__main__':
    unittest.main()
