DIAGRAPH = ["gb"]

SINGLE_LETTER_CONSONANTS = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ṣ', 't', 'w', 'y']

YORUBA_CONSONANTS = DIAGRAPH + SINGLE_LETTER_CONSONANTS

NASAL_VOWELS = ["ẹ", "ọ"]

SYLLABIC_VOWELS = ["a", "e", "i", "o", "u"]

YORUBA_VOWELS = NASAL_VOWELS + SYLLABIC_VOWELS

YORUBA_ALPHABETS = YORUBA_CONSONANTS + YORUBA_VOWELS

alphabet_type_map = dict(diagraph=DIAGRAPH, consonants=SINGLE_LETTER_CONSONANTS + DIAGRAPH, vowels=NASAL_VOWELS + SYLLABIC_VOWELS)


def contains(text, value):
    return any(ext in text for ext in alphabet_type_map.get(value))
