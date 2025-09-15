def concatenate_strings(input_tuple):
    # TODO
    result = ""
    for i in input_tuple:
        result += i + " "
    return result.strip()

input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string) 

def concatenate_strings2(input_tuple):
    return ' '.join(input_tuple)