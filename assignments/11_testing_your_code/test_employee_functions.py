from name_function import get_formatted_name
def test_first_last_name():
    """Do names like 'Daniel Flood $83,720.00' work?"""
    formatted_name = get_formatted_name('Daniel', 'Flood', '$83,730.00')
    assert formatted_name == 'Daniel Flood $83,730.00'
    print(format)