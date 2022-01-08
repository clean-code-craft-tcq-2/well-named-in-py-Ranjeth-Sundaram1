import get_color_pair_number_mapping 
from get_color_pair_number_mapping import get_color_from_pair_number

def print_color_number_mapping():
    print ('Pair number | Major color | Minor color \n')
    for number in range (len(get_color_pair_number_mapping.MINOR_COLORS)*len(get_color_pair_number_mapping.MAJOR_COLORS)):
        Major_color, Minor_color = get_color_from_pair_number(number+1)
        print (f'{number+1} | {Major_color} | {Minor_color}')
