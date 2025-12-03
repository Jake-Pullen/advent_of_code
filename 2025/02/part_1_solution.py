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
    Check if an ID is invalid (made of some sequence repeated twice)
    """
    id_str = str(id_num)
    length = len(id_str)
    
    # If length is odd, can't be made of two equal parts
    if length % 2 != 0:
        return False
    
    # Split into two halves and check if they're identical
    half_length = length // 2
    first_half = id_str[:half_length]
    second_half = id_str[half_length:]
    
    return first_half == second_half


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