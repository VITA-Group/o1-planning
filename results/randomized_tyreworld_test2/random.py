import os

def replace_terms(input_file, output_file, hash_dict1, hash_dict2):
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
            
        for key, value in hash_dict1.items():
            content = case_insensitive_replace(content, key, value)

        # Perform case-insensitive replacement
        for key, value in hash_dict2.items():
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
# hash_dict = {
#     "replace": "a1b2",
#     "have": "e5f6",
#     "hold": "g7h8",
#     "perform": "i9j0",
#     "undo": "k1l2",
#     "fasten": "m3n4",
#     "remove": "o5p6",
#     "put": "q7r8",
#     "inflate": "s9t0",
#     "open": "u1v2",
#     "close": "w3x4",
#     "fetch": "y5z6",
#     "put-away": "a7b8",
#     "loosen": "c9d0",
#     "loose": "c9d0",
#     "tighten": "e1f2",
#     "tight": "e1f2",
#     "jack-up": "g3h4",
#     "jack-down": "i5j6",
#     "do-up": "k7l8",
#     "remove-wheel": "m9n0",
#     "put-on-wheel": "o1p2",
#     "goal": "q3r4",
#     "flat": "s5t6",
#     "tyres": "u7v8",
#     "tyre": "u7v8",
#     "hubs": "w9x0",
#     "hub": "w9x0",
#     "nuts": "y1z2",
#     "nut": "y1z2",
#     "wrench": "a2b3",
#     "jack": "c4d5",
#     "pump": "e6f7",
#     "boot": "g8h9",
#     "container": "k2l3",
#     "object": "m4n5",
#     "agent": "o6p7",
#     "ground": "q8r9",
#     "wheel": "s0t1",
#     "unlocked" : "930d",
#     'intact': 'sdofi',
# }
# two hash_dict to prevent overlap
hash_dict1 ={
    "loosen": "c9d0",
    "tighten": "f8k1",
    "unfastened": "not m3n4",
    "jack-up": "g3h4",
    "jack-down": "i5j6",
    " This action fasten a nut on a hub" : "",
    " This action undo the fastening of a nut on a hub": ""
    
}
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
}



for i in range(1, 11):
    # Format the current number with leading zero if less than 10
    number_str = f'{i:02}'  # Ensures two digits with leading zeros
    input_path = f'./../tyreworld/p{number_str}.pddl.prompt'
    output_path = f'./p{number_str}.pddl.prompt'
    # Assuming the input file is 'input.txt' and the output file is 'output.txt'
    replace_terms(input_path,output_path, hash_dict1, hash_dict)
