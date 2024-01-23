from error_codes import error_messages
from load_data import config_data, load_config, gas_vocab_file, aerosol_vocab_file, cloud_vocab_file, \
      meteorology_vocab_file, photolysis_rate_vocab_file, platform_vocab_file, radiation_vocab_file


# Constructs StandardName object, then parses name with underscore delimiter
class StandardName:
    def __init__(self, standard_name):
        self.standard_name = standard_name
        self.parsed_name = []
        self.num_of_attributes = 0
        self.measurement_cat = ""
        self.error_codes = []

    def parse_name(self):
        self.parsed_name = self.standard_name.split('_')
        self.num_of_attributes = max(0, len(self.parsed_name) - 3)
        self.measurement_cat = self.parsed_name[0]

    # Functions for checking the measurement category and acquisition method
    def check_measure_cat(self) -> bool:
        valid_measure_cat = self.measurement_cat in config_data["MeasurementCategory"].keys()
        if not valid_measure_cat:
            self.error_codes.append(error_messages['MEASURE_CAT_ERROR'](self.measurement_cat))
        return valid_measure_cat

    def check_acquisition_met(self) -> bool:
        acquisition_met = self.parsed_name[2]
        valid_acquisition_met = self.parsed_name[2] in config_data["AcquisitionMethod"]
        if not valid_acquisition_met:
            self.error_codes.append(error_messages["ACQUISITION_ERROR"](acquisition_met))
        return valid_acquisition_met

    # Checks if the number of descriptive attributes matches with measurement category
    def check_num_attributes(self) -> bool:
        expected_attributes = config_data["MeasurementCategory"].get(self.measurement_cat)
        valid_num_attributes = (expected_attributes == self.num_of_attributes) if expected_attributes != 0 \
            else (self.num_of_attributes == 1)
        if not valid_num_attributes:
            self.error_codes.append(error_messages["NUM_ATTRIBUTES_ERROR"](self.num_of_attributes, expected_attributes))
        return valid_num_attributes

    # Helper functions to check if the descriptive attributes are valid for the corresponding measurement category
    def check_gas(self) -> bool:
        gas_vocab = load_config(gas_vocab_file)

        core_name = self.parsed_name[1]
        specificity = self.parsed_name[3]
        reporting = self.parsed_name[4]

        expected_specificity = gas_vocab["Gas CoreName:MeasurementSpecificity"].get(core_name)

        valid_core_name = core_name in gas_vocab["Gas CoreName:MeasurementSpecificity"].keys()
        valid_specificity = (specificity == expected_specificity)
        valid_reporting = reporting in gas_vocab["Reporting"]

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_specificity and valid_core_name:
            self.error_codes.append(error_messages["SPECIFICITY_ERROR"](specificity, expected_specificity))
        if not valid_reporting:
            self.error_codes.append(error_messages["REPORTING_ERROR"](reporting, gas_vocab["Reporting"]))

        return valid_core_name and valid_reporting and valid_specificity

    def check_aermp(self) -> bool:
        aerosol_vocab = load_config(aerosol_vocab_file)

        core_name = self.parsed_name[1]
        relative_humidity = self.parsed_name[3]
        sizing_technique = self.parsed_name[4]
        size_range = self.parsed_name[5]
        reporting = self.parsed_name[6]

        valid_core_name = core_name in aerosol_vocab["AerMP CoreName"]
        valid_rh = relative_humidity in aerosol_vocab["MeasurementRH"]
        valid_size_technique = sizing_technique in aerosol_vocab["SizingTechnique"]
        valid_size_range = (size_range == "Bulk") if sizing_technique == "None" else \
            size_range in aerosol_vocab["SizeRange"]
        valid_reporting = reporting in aerosol_vocab["AerMP/AerOpt Reporting"]

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_rh:
            self.error_codes.append(error_messages["MEASUREMENT_RH_ERROR"](relative_humidity,
                                                                           aerosol_vocab["MeasurementRH"]))
        if not valid_size_technique:
            self.error_codes.append(error_messages["SIZING_TECHNIQUE_ERROR"](sizing_technique,
                                                                             aerosol_vocab["SizingTechnique"]))
        if not valid_size_range:
            self.error_codes.append(error_messages["SIZE_RANGE_ERROR"](size_range, sizing_technique,
                                                                       aerosol_vocab["SizeRange"]))
        if not valid_reporting:
            self.error_codes.append(error_messages["REPORTING_ERROR"](reporting,
                                                                      aerosol_vocab["AerMP/AerOpt Reporting"]))

        return valid_core_name and valid_rh and valid_size_technique and valid_size_range and valid_reporting

    def check_aercomp(self) -> bool:
        aerosol_vocab = load_config(aerosol_vocab_file)

        core_name = self.parsed_name[1]
        sizing_technique = self.parsed_name[3]
        size_range = self.parsed_name[4]
        reporting = self.parsed_name[5]

        valid_core_name = core_name in aerosol_vocab["AerComp CoreName"]
        valid_size_technique = sizing_technique in aerosol_vocab["SizingTechnique"]
        valid_size_range = (size_range == "Bulk") if sizing_technique == "None" else \
            size_range in aerosol_vocab["SizeRange"]
        valid_reporting = reporting in aerosol_vocab["AerComp Reporting"]

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_size_technique:
            self.error_codes.append(error_messages["SIZING_TECHNIQUE_ERROR"](sizing_technique,
                                                                             aerosol_vocab["SizingTechnique"]))
        if not valid_size_range:
            self.error_codes.append(error_messages["SIZE_RANGE_ERROR"](size_range, sizing_technique,
                                                                       aerosol_vocab["SizeRange"]))
        if not valid_reporting:
            self.error_codes.append(error_messages["REPORTING_ERROR"](reporting, aerosol_vocab["AerComp Reporting"]))

        return valid_core_name and valid_size_technique and valid_size_range and valid_reporting

    def check_aeropt(self) -> bool:
        aerosol_vocab = load_config(aerosol_vocab_file)

        core_name = self.parsed_name[1]
        wave_length = self.parsed_name[3]
        relative_humidity = self.parsed_name[4]
        size_range = self.parsed_name[5]
        reporting = self.parsed_name[6]

        valid_core_name = core_name in aerosol_vocab["AerOpt CoreName"]
        valid_wl = wave_length in aerosol_vocab["WL"]
        valid_rh = relative_humidity in aerosol_vocab["MeasurementRH"]
        valid_size_range = size_range in aerosol_vocab["SizeRange"]
        valid_reporting = reporting in aerosol_vocab["AerMP/AerOpt Reporting"]

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_wl:
            self.error_codes.append(error_messages["WL_ERROR"](wave_length, aerosol_vocab["WL"]))
        if not valid_rh:
            self.error_codes.append(error_messages["MEASUREMENT_RH_ERROR"](relative_humidity,
                                                                           aerosol_vocab["MeasurementRH"]))
        if not valid_size_range:
            self.error_codes.append(error_messages["SIZE_RANGE_ERROR"](size_range, "Default",
                                                                       aerosol_vocab["SizeRange"]))
        if not valid_reporting:
            self.error_codes.append(error_messages["REPORTING_ERROR"](reporting,
                                                                      aerosol_vocab["AerMP/AerOpt Reporting"]))

        return valid_core_name and valid_wl and valid_rh and valid_size_range and valid_reporting

    def check_cldcomp(self) -> bool:
        cloud_vocab = load_config(cloud_vocab_file)

        core_name = self.parsed_name[1]
        sizing_technique = self.parsed_name[3]
        size_range = self.parsed_name[4]
        reporting = self.parsed_name[5]

        valid_core_name = core_name in cloud_vocab["CldComp CoreName"]
        valid_size_technique = sizing_technique in cloud_vocab["SizingTechnique"]
        valid_size_range = (size_range == "Bulk") if sizing_technique == "None" else \
            size_range in cloud_vocab["SizeRange"]
        valid_reporting = reporting in cloud_vocab["CldComp Reporting"]

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_size_technique:
            self.error_codes.append(error_messages["SIZING_TECHNIQUE_ERROR"](sizing_technique,
                                                                             cloud_vocab["SizingTechnique"]))
        if not valid_size_range:
            self.error_codes.append(error_messages["SIZE_RANGE_ERROR"](size_range, sizing_technique,
                                                                       cloud_vocab["SizeRange"]))
        if not valid_reporting:
            self.error_codes.append(error_messages["REPORTING_ERROR"](reporting, cloud_vocab["CldComp Reporting"]))

        return valid_core_name and valid_size_technique and valid_size_range and valid_reporting

    def check_cldmicro(self) -> bool:
        cloud_vocab = load_config(cloud_vocab_file)

        core_name = self.parsed_name[1]
        sizing_technique = self.parsed_name[3]
        size_range = self.parsed_name[4]
        reporting = self.parsed_name[5]

        valid_core_name = core_name in cloud_vocab["CldMicro CoreName"]
        valid_size_technique = sizing_technique in cloud_vocab["SizingTechnique"]
        valid_size_range = (size_range == "Bulk") if sizing_technique == "None" else \
            size_range in cloud_vocab["SizeRange"]
        valid_reporting = reporting in cloud_vocab["CldMicro Reporting"]

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_size_technique:
            self.error_codes.append(error_messages["SIZING_TECHNIQUE_ERROR"](sizing_technique,
                                                                             cloud_vocab["SizingTechnique"]))
        if not valid_size_range:
            self.error_codes.append(error_messages["SIZE_RANGE_ERROR"](size_range, sizing_technique,
                                                                       cloud_vocab["SizeRange"]))
        if not valid_reporting:
            self.error_codes.append(error_messages["REPORTING_ERROR"](valid_reporting,
                                                                      cloud_vocab["CldMicro Reporting"]))

        return valid_core_name and valid_size_technique and valid_size_range and valid_reporting

    def check_cldmacro(self) -> bool:
        cloud_vocab = load_config(cloud_vocab_file)

        core_name = self.parsed_name[1]
        attributes = self.parsed_name[3]

        valid_core_name = core_name in cloud_vocab["CldMacro CoreName"]
        valid_zero_attribute = (attributes == "None")

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_zero_attribute:
            self.error_codes.append(error_messages["ZERO_ATTRIBUTE_ERROR"](self.measurement_cat))

        return valid_core_name and valid_zero_attribute

    def check_cldopt(self) -> bool:
        cloud_vocab = load_config(cloud_vocab_file)

        core_name = self.parsed_name[1]
        wave_length = self.parsed_name[3]

        valid_core_name = core_name in cloud_vocab["CldOpt CoreName"]
        valid_wl = wave_length in cloud_vocab["WL"]

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_wl:
            self.error_codes.append(error_messages["WL_ERROR"](wave_length, cloud_vocab["WL"]))

        return valid_core_name and valid_wl

    def check_met(self) -> bool:
        meteorology_vocab = load_config(meteorology_vocab_file)

        core_name = self.parsed_name[1]
        attributes = self.parsed_name[3]

        valid_core_name = core_name in meteorology_vocab["Met CoreName"]
        valid_zero_attribute = (attributes == "None")

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_zero_attribute:
            self.error_codes.append(error_messages["ZERO_ATTRIBUTE_ERROR"](self.measurement_cat))

        return valid_core_name and valid_zero_attribute

    def check_gasjvalue(self) -> bool:
        photolysis_rate_vocab = load_config(photolysis_rate_vocab_file)

        core_name = self.parsed_name[1]
        acquisition_met = self.parsed_name[2]
        measurement_direction = self.parsed_name[3]
        spectral_coverage = self.parsed_name[4]
        products = self.parsed_name[5]

        expected_products = photolysis_rate_vocab["GasJvalue CoreName:Products"].get(core_name)

        valid_core_name = core_name in photolysis_rate_vocab["GasJvalue CoreName:Products"].keys()
        valid_measure_dir = measurement_direction in photolysis_rate_vocab["MeasurementDirection"]
        valid_spectral_cov = spectral_coverage in photolysis_rate_vocab["SpectralCoverage"]
        valid_products = (products in expected_products) if expected_products else (products == "NoProductsSpecified")
        valid_acquisition = (acquisition_met == "InSitu")

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_measure_dir:
            self.error_codes.append(error_messages["MEASURE_DIR_ERROR"](measurement_direction,
                                                                        photolysis_rate_vocab['MeasurementDirection']))
        if not valid_spectral_cov:
            self.error_codes.append(error_messages["SPECTRAL_COV_ERROR"](spectral_coverage,
                                                                         photolysis_rate_vocab['SpectralCoverage']))
        if not valid_products and valid_core_name:
            self.error_codes.append(error_messages["PRODUCT_ERROR"](products, expected_products))
        if not valid_acquisition:
            self.error_codes.append(error_messages["INSITU_ERROR"](acquisition_met))

        return valid_core_name and valid_measure_dir and valid_spectral_cov and valid_products and valid_acquisition

    def check_aqujvalue(self) -> bool:
        photolysis_rate_vocab = load_config(photolysis_rate_vocab_file)

        core_name = self.parsed_name[1]
        acquisition_met = self.parsed_name[2]
        measurement_direction = self.parsed_name[3]
        spectral_coverage = self.parsed_name[4]
        products = self.parsed_name[5]

        expected_products = photolysis_rate_vocab["AquJvalue CoreName:Products"].get(core_name)

        valid_core_name = core_name in photolysis_rate_vocab["AquJvalue CoreName:Products"].keys()
        valid_measure_dir = measurement_direction in photolysis_rate_vocab["MeasurementDirection"]
        valid_spectral_cov = spectral_coverage in photolysis_rate_vocab["SpectralCoverage"]
        valid_products = (products in expected_products) if expected_products else (products == "NoProductsSpecified")
        valid_acquisition = (acquisition_met == "InSitu")

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_measure_dir:
            self.error_codes.append(error_messages["MEASURE_DIR_ERROR"](measurement_direction,
                                                                        photolysis_rate_vocab['MeasurementDirection']))
        if not valid_spectral_cov:
            self.error_codes.append(error_messages["SPECTRAL_COV_ERROR"](spectral_coverage,
                                                                         photolysis_rate_vocab['SpectralCoverage']))
        if not valid_products and valid_core_name:
            self.error_codes.append(error_messages["PRODUCT_ERROR"](products, expected_products))
        if not valid_acquisition:
            self.error_codes.append(error_messages["INSITU_ERROR"](acquisition_met))

        return valid_core_name and valid_measure_dir and valid_spectral_cov and valid_products and valid_acquisition

    def check_platform(self) -> bool:
        platform_vocab = load_config(platform_vocab_file)

        core_name = self.parsed_name[1]
        acquisition_met = self.parsed_name[2]
        attributes = self.parsed_name[3]

        valid_core_name = core_name in platform_vocab["Platform CoreName"]
        valid_acquisition = (acquisition_met == "InSitu")
        valid_zero_attribute = (attributes == "None")

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_acquisition:
            self.error_codes.append(error_messages["INSITU_ERROR"](acquisition_met))
        if not valid_zero_attribute:
            self.error_codes.append(error_messages["ZERO_ATTRIBUTE_ERROR"](self.measurement_cat))

        return valid_core_name and valid_acquisition and valid_zero_attribute

    def check_rad(self) -> bool:
        radiation_vocab = load_config(radiation_vocab_file)

        core_name = self.parsed_name[1]
        acquisition_met = self.parsed_name[2]
        wl_mode = self.parsed_name[3]

        valid_core_name = core_name in radiation_vocab["Rad CoreName"]
        valid_wl_mode = wl_mode in radiation_vocab["WLMode"]
        valid_acquisition = (acquisition_met == "InSitu")

        if not valid_core_name:
            self.error_codes.append(error_messages["CORE_NAME_ERROR"](core_name, self.measurement_cat))
        if not valid_wl_mode:
            self.error_codes.append(error_messages["WL_MODE_ERROR"](wl_mode, radiation_vocab["WLMode"]))
        if not valid_acquisition:
            self.error_codes.append(error_messages["INSITU_ERROR"](acquisition_met))

        return valid_core_name and valid_wl_mode and valid_acquisition

    # Main function that checks all the attributes of standard name
    def check_standard_name(self) -> bool:
        self.parse_name()

        valid_measure_cat = self.check_measure_cat()
        valid_num_att = False
        valid_acquisition = False
        valid_attributes = False

        check_descriptive_att = {
            "Gas": self.check_gas,
            "AerMP": self.check_aermp,
            "AerComp": self.check_aercomp,
            "AerOpt": self.check_aeropt,
            "CldComp": self.check_cldcomp,
            "CldMicro": self.check_cldmicro,
            "CldMacro": self.check_cldmacro,
            "CldOpt": self.check_cldopt,
            "Met": self.check_met,
            "GasJvalue": self.check_gasjvalue,
            "AquJvalue": self.check_aqujvalue,
            "Platform": self.check_platform,
            "Rad": self.check_rad
        }

        if valid_measure_cat:
            valid_num_att = self.check_num_attributes()
        if valid_num_att:
            valid_acquisition = self.check_acquisition_met()
        if valid_acquisition:
            valid_attributes = check_descriptive_att[self.measurement_cat]()

        return valid_measure_cat and valid_num_att and valid_acquisition and valid_attributes
