from name_function import get_formatted_name
def test_first_last_name():
    """Do names like 'Tokyo and London work?"""
    formatted_name = get_formatted_name('Tokyo', 'London')
    assert formatted_name == 'Tokyo and London'
    print(format)