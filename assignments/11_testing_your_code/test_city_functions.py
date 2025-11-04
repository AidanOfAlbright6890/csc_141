from name_function import get_formatted_name
def test_first_last_name():
    """Do names like 'Denver Colorado' work?"""
    formatted_name = get_formatted_name('Denver', 'Colorado')
    assert formatted_name == 'Denver Colorado'
    print(format)