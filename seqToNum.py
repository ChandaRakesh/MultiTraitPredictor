import numpy as np
geno_map = {'AA':1, 'AT':2, 'AG':3, 'AC':4, 'TT':5, 'TG':6, 'TC':7, 'GG':8, 'CG':9, 'CC':10}
def map_sequence_to_numbers(sequence):
    
    # Check if the sequence length is even
    if len(sequence)!=48:
        raise ValueError("The sequence length must be even.")

    # Split the sequence into chunks of two characters
    chunks = [sequence[i:i+2] for i in range(0, len(sequence), 2)]

    # Map each chunk to its corresponding number using the geno_map
    mapped_numbers = [geno_map[chunk] for chunk in chunks if chunk in geno_map]

    return mapped_numbers

def convert_to_npArray(sequence):
    if len(sequence)!=48:
        raise ValueError("The sequence length must be even.")
    genotype_list = [sequence[i:i+2] for i in range(0, len(sequence), 2)]
    number_list = [geno_map.get(genotype, 0) for genotype in genotype_list]
    return np.array(number_list).reshape(1, -1)