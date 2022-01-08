import get_color_pair_number_mapping
from get_color_pair_number_mapping import get_color_from_pair_number

def print_color_pair_number_mapping():
    print ('Pair number | Major color | Minor color \n')
    for number in range (len(MINOR_COLORS)*len(MAJOR_COLORS)):
        Major_color, Minor_color = get_color_from_pair_number(number+1)
        print (f'{number} | {Major_color} | {Minor_color}')
