def to_rna(text):
    dna_to_rna = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U'
     }

    result = []
    for d in text:
        if d in dna_to_rna :
            result.append(dna_to_rna[d])
        else:
            return ''
    return ''.join(result)
