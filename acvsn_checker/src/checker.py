import click
from error_codes import error_messages
from standard_name import StandardName


# Command line interface that prints whether standard name is valid; if not, prints list of errors
@click.group()
def main():
    """Checks if a STANDARD NAME is valid. For documentation on ACVSNC, visit
    https://www.earthdata.nasa.gov/esdis/esco/standards-and-practices/acvsnc"""
    pass


@click.command()
@click.argument('name')
def check_name(name):
    standard_name = StandardName(name)
    is_valid = standard_name.check_standard_name()
    errors = standard_name.error_codes

    click.echo(f"Checking {click.style(standard_name.standard_name, fg='yellow')} ... \n")

    if is_valid:
        click.echo(f"{error_messages['NO_ERROR']}")
    elif len(errors) == 1:
        click.echo(f"{errors[0]}")
    else:
        for index, error in enumerate(errors):
            click.echo(f"{index + 1}. {error}")


@click.command()
@click.argument('filename')
def check_file(filename):
    click.echo("Checking file ... \n")

    try:
        with open(filename, 'r') as file_input:
            file_header = file_input.readlines()
    except IOError:
        click.secho("File was not found.", fg='red')
        exit()

    num_variables = int(file_header[9])
    valid_header = True

    for line_index in range(12, 12 + num_variables):
        line = file_header[line_index]
        if not ('TIME' in line.upper()):

            standard_name = StandardName(line.split(',')[2].strip())
            is_valid = standard_name.check_standard_name()
            errors = standard_name.error_codes

            if not is_valid and standard_name.standard_name != 'None':
                click.echo(f"Error found on line {click.style(line_index, fg='yellow')} with standard name "
                           f"{click.style(standard_name.standard_name, fg='red')}")
                valid_header = False
                if len(errors) == 1:
                    click.echo(f"{errors[0]}")
                else:
                    for index, error in enumerate(errors):
                        click.echo(f"{index + 1}. {error}")
                click.echo("-------------------------------------------------------------------------------")

    if valid_header:
        click.echo("All standard names in file header are valid.")


main.add_command(check_name)
main.add_command(check_file)

if __name__ == '__main__':
    main()
