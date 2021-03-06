import code

from assembler.registers import REGISTERS
from assembler.error import SyntaxError

"""
This function checks that the passed in instruction matches the form of the
tuple. The tuple represents the order, type and number of the parameters that
be passed into the function. There are three types of parameters (`register`,
`label`, and `number`). In the above example, `check_params()` is used to check
to make sure there are two parameters that are both registers.
"""
def check_params(instruction, param_type_tuple):
    params = instruction['params']
    labels = instruction['labels']

    # Check to make sure the number of parameters are the same.
    if not len(params) == len(param_type_tuple):
        raise SyntaxError("Expected " + str(len(param_type_tuple)) + " params. Found " + str(len(params)))

    for index, param_type in enumerate(param_type_tuple):
        if param_type == "label":
            # Check if the label exists in the label object.
            if not params[index] in labels:
                raise SyntaxError("Label '" + params[index] + "' not found.")
        elif param_type == "register":
            # Check if the register exists in REGISTER.
            if not params[index] in REGISTERS:
                raise SyntaxError("Register '" + params[index] + "' not found.")
        elif param_type == "number":
            # Checks if the number can be typcasted into an int.
            number = 0
            try:
                number = int(params[index])
            except ValueError:
                raise SyntaxError("Can't convert '" + params[index] + "' to number.")
        else:
            # Just in case one of the instructions doesn't have any of the valid options.
            raise ElectronGoblins("Valid options for params are 'label', 'register', and 'number'.")


def to_bin_string(number, bin_digits, signed=False):

    if not signed:
        num_str = format(number, "0" + str(bin_digits) + "b")
        if len(num_str) <= bin_digits:
            return num_str
        else:
            raise SyntaxError("The number '%s' cannot be converted to %s bits." % (number, bin_digits))
    else:
        # Check that the number can be represented in two's comp. Specifically,
        # check to make sure there are enough bits.
        minmax = 2 ** (bin_digits - 1)
        if minmax > number >= 0:
            return format(number, "0" + str(bin_digits) + "b")
        elif 0 > number >= -minmax:
            num_str = bin(number % (1<<bin_digits))
            return num_str[2:]
        raise SyntaxError("The number '%s' cannot be represented in 2's complement with %s digits." % (number, bin_digits))
