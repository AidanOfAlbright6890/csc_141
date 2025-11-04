from name_function import get_formatted_name
def test_first_last_name():
    """Do names like 'Denver 729.02k Colorado' work?"""
    formatted_name = get_formatted_name('Denver', '729.02k', 'Colorado')
    assert formatted_name == 'Denver 729.02k Colorado'
    print(format)