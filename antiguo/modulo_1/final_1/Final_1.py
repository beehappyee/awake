import numpy as np

class Piano:

    var_hash = '#'
    var_hashes = '##'
    var_result = []
    var_valids = {'C':1, 'D':3, 'E':5, 'F':6, 'G':8, 'A':10, 'B':12, '#':1}

    def keyNum(self, in_song):

        try:

            in_song = in_song.upper()

            self.validateSong(in_song)
            self.validateHash(in_song)
            self.convertSong(in_song)

        except Exception:

            self.printStatus('No es posible procesar tu cancion')

        else:

            self.printStatus('Cancion procesada')

    def validateSong(self, in_song):

        var_keys = list(self.var_valids.keys())

        var_song = np.array(list(in_song))

        if not np.all(np.isin(var_song, var_keys)):

            self.printStatus('La cadena no cumple con el patrón')

            raise Exception()

    def validateHash(self, in_song):

        if self.var_hashes in in_song:

            self.printStatus('La cadena contiene más de un # consecutivo')

            raise Exception()

    def convertSong(self, in_song):

        var_hash = 0

        for var_char in in_song:

            if var_char == self.var_hash:

                var_hash = 1

            else:

                self.var_result.append(self.var_valids.get(var_char) + var_hash)

                var_hash = 0

        print(self.var_result)

    def printStatus(self,in_status):

        print(in_status)

in_song = 'e#ee#a'
piano = Piano()
piano.keyNum(in_song)