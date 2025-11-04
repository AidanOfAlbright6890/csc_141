from name_function import get_formatted_name
def test_first_last_name():
    """Do names like 'Ash Ketchum' work?"""
    formatted_name = get_formatted_name('Ash', 'Ketchum')
    assert formatted_name == 'Ash Ketchum'
    print(format)