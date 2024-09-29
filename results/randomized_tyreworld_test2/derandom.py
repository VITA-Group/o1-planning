import os

def replace_terms(input_file, output_file, hash_dict):
    """
    Read a text file and replace occurrences of dictionary keys with their hashed values, case-insensitively.

    Parameters:
    - input_file (str): The path to the input text file.
    - output_file (str): The path to the output text file where modified content will be saved.
    - hash_dict (dict): A dictionary where keys are terms to replace and values are their hashes.

    Returns:
    None
    """
    try:
        # Read the content of the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Perform case-insensitive replacement
        for key, value in hash_dict.items():
            content = case_insensitive_replace(content, key, value)

        # Write the modified content to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"File processed successfully. Output saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def case_insensitive_replace(content, old, new):
    """
    Replace all occurrences of 'old' with 'new' in 'content' in a case-insensitive manner.

    Parameters:
    - content (str): The original string.
    - old (str): The substring to replace.
    - new (str): The replacement substring.

    Returns:
    str: The modified string with all occurrences of 'old' replaced by 'new'.
    """
    import re
    # Use regular expression to replace all case-insensitive occurrences of 'old'
    pattern = re.compile(re.escape(old), re.IGNORECASE)
    return pattern.sub(new, content)

# Example usage
hash_dict = {
    # "replace": "switch",
    # "with": "to",
    "have": "e5f6",
    "hold": "g7h8",
    "perform": "i9j0",
    "undo": "k1l2",
    "remove": "o5p6",
    "put": "q7r8",
    "inflate": "s9t0",
    "fastened": "m3n4",
    "open": "u1v2",
    "close": "w3x4",
    "fetch": "y5z6",
    "put-away": "a7b8",
    "loose": "f03k",
    "tight": "e1f2",
    "do-up": "k7l8",
    "remove-wheel": "m9n0",
    "put-on-wheel": "o1p2",
    "flat": "s5t6",
    "tyres": "u7v8",
    "tyre": "u7v8",
    "hubs": "w9x0",
    "hub": "w9x0",
    "nuts": "y1z2",
    "nut": "y1z2",
    "wrench": "a2b3",
    "jack": "c4d5",
    "pump": "e6f7",
    "boot": "g8h9",
    "container": "k2l3",
    "object": "m4n5",
    "agent": "o6p7",
    "ground": "q8r9",
    "wheel": "s0t1",
    "unlocked" : "930d",
    'intact': 's4f5',
    "loosen": "c9d0",
    "tighten": "f8k1",
    "unfastened": "not m3n4",
    "jack-up": "g3h4",
    "jack-down": "i5j6",
}

reversed_hash_dict = {value: key for key, value in hash_dict.items()}



# input_path = './../randomized_tyreworld/p02.pddl.o1-preview'
# output_path = './reverse_p02.pddl.o1-preview'
for i in range(1, 11):
    # Format the current number with leading zero if less than 10
    number_str = f'{i:02}'  # Ensures two digits with leading zeros
    # Construct the output path by inserting the current number
    input_path = f'./../randomized_tyreworld_test2/p{number_str}.pddl.o1-preview'
    output_path = f'./reverse_p{number_str}.pddl.o1-preview'
    replace_terms(input_path,output_path, reversed_hash_dict)
# input_path = './../tyreworld/p02.pddl.o1-preview'
# output_path = './reverse_p02.pddl.o1-preview'
# Assuming the input file is 'input.txt' and the output file is 'output.txt'

