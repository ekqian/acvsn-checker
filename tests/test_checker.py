import unittest

from src.main import StandardName


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
        gasjvalue = StandardName('GasJvalue_jNO2_InSitu_Total_Full_NO2-O3P')
        aqujvalue = StandardName('GasJvalue_jNO2_InSitu_Total_Full_NO2-O3P')
        platform = StandardName('Platform_YawAngle_InSitu_None')
        rad = StandardName('Rad_IrradianceDownwellingDiffuse_InSitu_BB')

        self.assertEquals(gas.check_standard_name(), True)
        self.assertEquals(aermp.check_standard_name(), True)
        self.assertEquals(aercomp.check_standard_name(), True)
        self.assertEquals(aeropt.check_standard_name(), True)
        self.assertEquals(cldcomp.check_standard_name(), True)
        self.assertEquals(cldmicro.check_standard_name(), True)
        self.assertEquals(cldmacro.check_standard_name(), True)
        self.assertEquals(cldopt.check_standard_name(), True)
        self.assertEquals(met.check_standard_name(), True)
        self.assertEquals(gasjvalue.check_standard_name(), True)
        self.assertEquals(aqujvalue.check_standard_name(), True)
        self.assertEquals(platform.check_standard_name(), True)
        self.assertEquals(rad.check_standard_name(), True)

