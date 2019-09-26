def get_formatted_name(city, country):
    """Generate a neatly formatted sring of the form 'City, Country'."""
    formatted_name = city.title() + ', ' + country.title()
    return formatted_name

