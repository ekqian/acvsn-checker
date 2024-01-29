import unittest

from src.standard_name import StandardName


class TestChecker(unittest.TestCase):
    def test_checker(self):
        gas = StandardName('Gas_O3_InSitu_S_DMF')
        aermp = StandardName('AerMP_NumSizeDist_InSitu_RHd_Aerodynamic_Coarse_STP')
        aercomp = StandardName('AerComp_OrganicAerosol_InSitu_VacuumAerodynamic_Accu_MassSTP')
        aeropt = StandardName('AerOpt_Absorption_InSitu_Red_RHd_Bulk_AMB')
        cldcomp = StandardName('CldComp_Sodium_InSitu_None_Bulk_MassAMB')
        cldmicro = StandardName('CldMicro_NumSizeDist_InSitu_Optical_Drop_AMB')
        cldmacro = StandardName('CldMacro_CTH_InSitu_None')
        cldopt = StandardName('CldOpt_Extinction_InSitu_Blue')
        met = StandardName('Met_StaticAirTemperature_InSitu_None')
        gasjvalue = StandardName('GasJvalue_jHNO4_InSitu_Total_Partial_HO2-NO2')
        platform = StandardName('Platform_YawAngle_InSitu_None')
        rad = StandardName('Rad_IrradianceDownwellingDiffuse_InSitu_BB')

        self.assertTrue(gas.check_standard_name())
        self.assertTrue(aermp.check_standard_name())
        self.assertTrue(aercomp.check_standard_name())
        self.assertTrue(aeropt.check_standard_name())
        self.assertTrue(cldcomp.check_standard_name())
        self.assertTrue(cldmicro.check_standard_name())
        self.assertTrue(cldmacro.check_standard_name())
        self.assertTrue(cldopt.check_standard_name())
        self.assertTrue(met.check_standard_name())
        self.assertTrue(gasjvalue.check_standard_name())
        self.assertTrue(platform.check_standard_name())
        self.assertTrue(rad.check_standard_name())
