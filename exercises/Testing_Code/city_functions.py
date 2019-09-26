def get_formatted_name(city, country, population=''):
    """Generate a neatly formatted sring of the form 'City, Country'."""
    if population:
        formatted_name = city.title() + ', ' + country.title() + ' - Population ' + str(population)
    else:
        formatted_name = city.title() + ', ' + country.title()
    return formatted_name

