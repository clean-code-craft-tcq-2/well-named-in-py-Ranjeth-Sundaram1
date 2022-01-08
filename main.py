from test_color_number_maping import test_number_to_pair
from test_color_number_mapping import test_pair_to_number
from get_color_number_mapping import print_color_number_mapping

if __name__ == '__main__':
    
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print_color_number_combo()
    print('Done :)')
