def insert_value_front(input_tuple, value_to_insert):
    # TODO
    return tuple([value_to_insert] + list(input_tuple))

input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)

def insert_value_at_beginning2(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple