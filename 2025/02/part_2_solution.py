testing = False
if not testing:
    with open(r"2025/02/input.txt", "r") as file:
        input = file.read()
else:
    input = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''

product_id_list = input.split(',')

bad_products_list = []

def is_invalid_id(id_num):
    """
    Check if an ID is invalid (made of some sequence repeated at least twice)
    """
    id_str = str(id_num)
    length = len(id_str)
    
    # Try all possible pattern lengths from 1 to half the string length
    for pattern_length in range(1, length // 2 + 1):
        # Check if the string can be divided evenly by this pattern length
        if length % pattern_length == 0:
            # Get the pattern (first part)
            pattern = id_str[:pattern_length]
            # Calculate how many times this pattern should repeat
            num_repeats = length // pattern_length
            # If it repeats at least twice, it's invalid
            if num_repeats >= 2:
                # Check if the entire string is made up of this pattern repeated
                if pattern * num_repeats == id_str:
                    return True
    
    return False


for product_id in product_id_list:
    # print(product_id)
    first_id,second_id = product_id.split('-')
    print(first_id, 'to', second_id)
    for product in range(int(first_id), int(second_id)+1):
        # print(product)
        if is_invalid_id(product):
            print(f'{product} invalid')
            bad_products_list.append(product)
        else:
            pass
            # print(f'product {product} looks valid')
    print(bad_products_list)

total_sum = 0

for bad_id in bad_products_list:
    total_sum += int(bad_id)

print(total_sum)

