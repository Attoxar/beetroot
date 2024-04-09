# primitives
integer = 4 # int(4.9) -> 4, int(True) -> 1 int(False) -> 0, int(...

float = 4. #float() same as above

string = '"any word like hello, world"'
things_to_escape = ('tap: \t, backward slash, \\, what if ' 
                    'i want to write down a very long string')
exemple = (
    "string one" 
    "the second half of the string"
)
 boolean = True # bool
 Nothing = None # None is a placeholder
# collections
tuple_with_a_single_element = (3,) # is not mutable

my_list = [3, 4] #list is mutable
my_set = {3, 3}
my_dictionary = {3,}
print(id(my_list)) # build in namesspace

# build-ins vs reserverd words
def = # reserverd word
# print = # build in function
def function_to_demonstrate_parameters(
        first_positional_parameter,
        second_positional_parameter,
         and_here_goes_a_keyword_paragram="default"
):
    print(f"first positional: {first_positional_parameter}")
    print(f"second postiotinal: {second_positional_parameter}")
    print(f"keyword_argument: {and_here_goes_a_keyword_paragram}")
print("outside of the function")
function_to_demonstrate_parameters("first string","second string")