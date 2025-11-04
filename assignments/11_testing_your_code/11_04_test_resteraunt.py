from name_function import get_formatted_name
def test_first_last_name():
    """Do names like 'Austin's an Coastal Grill' work?"""
    formatted_name = get_formatted_name('Austins', 'Coastal Grill')
    assert formatted_name == 'Austins and Coastal Grill'
    print(format)