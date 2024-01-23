import click
from load_data import config_data


# Stores the possible error messages
error_messages = {
    'MEASURE_CAT_ERROR': lambda measure_cat:
    f"Measurement category {click.style(measure_cat, fg='red')} is not valid; valid measurement categories are "
    f"{click.style(', '.join([str(s) for s in list(config_data['MeasurementCategory'].keys())]), fg='green')}",

    'NUM_ATTRIBUTES_ERROR': lambda num_attributes, expected:
    f"Number of descriptive attributes ({click.style(num_attributes, fg='red')}) does not match with expected "
    f"number of attributes ({click.style(expected, fg='green')}).",

    'ACQUISITION_ERROR': lambda acquisition_met:
    f"Acquisition method {click.style(acquisition_met, fg='red')} is not valid; valid acquisition methods are "
    f"{click.style(', '.join([str(s) for s in config_data['AcquisitionMethod']]), fg='green')}",

    'CORE_NAME_ERROR': lambda core_name, measure_cat:
    f"Core Name {click.style(core_name, fg='red')} is not valid for the measurement category "
    f"{click.style(measure_cat, fg='blue')}.",

    'SPECIFICITY_ERROR': lambda specificity, expected:
    f"Specificity attribute {click.style(specificity, fg='red')} does not match with the core name; "
    f"expected to see {click.style(expected, fg='green')}",

    'REPORTING_ERROR': lambda reporting, valid_list:
    f"Reporting attribute {click.style(reporting, fg='red')} is not valid; valid attributes are "
    f"{click.style(', '.join([str(s) for s in valid_list]), fg='green')}",

    'WL_ERROR': lambda wave_length, valid_list:
    f"WaveLength attribute {click.style(wave_length, fg='red')} is not valid; valid attributes are "
    f"{click.style(', '.join([str(s) for s in valid_list]), fg='green')}",

    'MEASUREMENT_RH_ERROR': lambda relative_humidity, valid_list:
    f"MeasurementRH attribute {click.style(relative_humidity, fg='red')} is not valid; valid attributes are "
    f"{click.style(', '.join([str(s) for s in valid_list]), fg='green')}",

    'SIZING_TECHNIQUE_ERROR': lambda sizing_technique, valid_list:
    f"SizingTechnique attribute {click.style(sizing_technique, fg='red')} is not valid; valid attributes are "
    f"{click.style(', '.join([str(s) for s in valid_list]), fg='green')}",

    'SIZE_RANGE_ERROR': lambda size_range, sizing_technique, valid_list:
    f"SizeRange attribute {click.style(size_range, fg='red')} is not valid; valid attributes are "
    f"{click.style(', '.join([str(s) for s in valid_list]), fg='green')}" if sizing_technique != 'None' else
    f"SizingRange attribute must be {click.style('Bulk', fg='green')} if SizingTechnique is "
    f"{click.style('None', fg='blue')}",

    'MEASURE_DIR_ERROR': lambda measurement_direction, valid_list:
    f"MeasurementDirection attribute {click.style(measurement_direction, fg='red')} is not valid; valid attributes "
    f"are {click.style(', '.join([str(s) for s in valid_list]), fg='green')}",

    'SPECTRAL_COV_ERROR': lambda spectral_coverage, valid_list:
    f"SpectralCoverage attribute {click.style(spectral_coverage, fg='red')} is not valid; valid attributes are "
    f"{click.style(', '.join([str(s) for s in valid_list]), fg='green')}",

    'PRODUCT_ERROR': lambda products, valid_list:
    f"{click.style(products, fg='red')} is not a known product; known products are "
    f"{click.style(', '.join([str(s) for s in valid_list]), fg='green')}" if valid_list else
    f"{click.style(products, fg='red')} is not valid; expected to see "
    f"{click.style('NoProductsSpecified', fg='green')}",

    'WL_MODE_ERROR': lambda wl_mode, valid_list:
    f"WLMode attribute ({click.style(wl_mode, fg='red')}) is not valid; valid attributes are "
    f"{click.style(', '.join([str(s) for s in valid_list]), fg='green')}",

    'ZERO_ATTRIBUTE_ERROR': lambda measure_cat:
    f"Descriptive attribute for {click.style(measure_cat, fg='blue')} must be {click.style('None', fg='green')}.",

    'INSITU_ERROR': lambda acquisition_met:
    f"Acquisition method ({click.style(acquisition_met, fg='red')}) is not valid; must be "
    f"{click.style('InSitu', fg='green')}",

    'NO_ERROR': click.style("Standard name is valid.", fg='green'),
}