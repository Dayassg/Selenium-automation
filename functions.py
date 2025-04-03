def program(x):
    print(x)

program("First Demo")
program(2)

def program_return(x):
    return x

returned_value = program_return(5)
print(returned_value)

def program_return_optional(x, optional_params = 2):
    return x + optional_params

returned_value_optional = program_return_optional(5)
print(returned_value_optional)

def xargs(*any_name):
    k = 1
    for i in any_name:
        k = k*i
    return k

xargs_values = xargs(2,3)
print(xargs_values)

def xxargs(**dict_name):
    return(dict_name.values())

xxargs_values = xxargs(id = 1, name = "Daya", Occupation = "Software Engineer")
print(xxargs_values)