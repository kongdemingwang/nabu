'''@file aurora4.py
contains the global phoneset target normalizer'''

import unicodedata
import normalizer

class Gp(normalizer.Normalizer):
    '''normalize for the Global Phoneset database'''

    def __call__(self, transcription):
        '''normalize a transcription

        Args:
            transcription: the transcription to be normalized as a string

        Returns:
            the normalized transcription as a string space seperated per
            character'''

        #remove accents
        normalized = unicodedata.normalize(
            'NFKD', transcription.decode('utf-8')).encode('ASCII', 'ignore')

        #replace the spaces with <space>
        normalized = [character if character is not ' ' else '<space>'
                      for character in normalized]

        #replace unknown characters with <unk>
        normalized = [character if character in self.alphabet else '<unk>'
                      for character in normalized]

        return ' '.join(normalized)

    def _create_alphabet(self):
        '''create the alphabet that is used in the normalizer

        Returns:
            the alphabet as a list of strings'''

        alphabet = []

        #space
        alphabet.append('<space>')

        #unknown character
        alphabet.append('<unk>')

        #letters in the alphabet
        for letter in range(ord('a'), ord('z')+1):
            alphabet.append(chr(letter))

        #ordinals
        for number in range(10):
            alphabet.append(str(number))

        return alphabet
