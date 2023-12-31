import numpy

class Translation():

    def toBinary(self, n):
        """
        Convertit un entier n en un string contenant la séquence sur un octet (ou 8 bits).

        Args:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        Returns:
            str_bin (string): Forme binaire de l'entier en string.
        """
        str_bin =''.join(str(1 & int(n) >> i) for i in range(8)[::-1])
        return str_bin

    def toInt(self, str_bin):
        """
        Convertit un string contenant la séquence sur un octet (ou 8 bits) en un entier n.

        Args:
            str_bin (string): Forme binaire de l'entier en string.
        Returns:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        """
        n = int(str_bin, 2)
        return n

    def translateToMachine(self, phrase):
        """
        Convertit une phrase (encodée comme un string) en une liste de strings d'octets (ou 8 bits).

        Args:
            phrase (string): Phrase en français ou en anglais.
        Returns:
            phrase_bin (list of strings): Liste de strings, chaque string représente un octet/8 bits
        """
        phrase_bin = [self.toBinary(ord(char)) for char in phrase]
        return phrase_bin

    def translateToHuman(self, bin_phrase):
        """
        Convertit une liste de strings d'octets (ou 8 bits) en une phrase (encodée comme un string).

        Args:
            bin_phrase (list of strings): Liste de strings, chaque string représente un octet/8 bits
        Returns:
            phrase (string): Phrase en français ou en anglais.
        """
        phrase = ""
        for bin_str in bin_phrase:
            phrase += chr(self.toInt(bin_str))
        return phrase

class BinaryDomains():

    def toBinary(self, n):
        """
        Convertit un entier n en un string contenant la séquence sur un octet (ou 8 bits).

        Args:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        Returns:
            string: Forme binaire de l'entier en string.
        """
        return ''.join(str(1 & int(n) >> i) for i in range(8)[::-1])

    def addCayley(self, x, y):
        '''
        Compare deux entrées dans la table de Cayley d'addition
        :param x: 0 ou 1
        :param y: 0 ou 1
        :return: la sortie du tableau pour les deux entrées x et y
        '''

        if (x == "0" and y == "1") or (x == "1" and y == "0"):
            return "1"
        return "0"
    
    def add(self, x, y):
        """
        Additionne deux séquences binaires (x+y) reçues sous la forme de string.

        Exemple : "10111001" + "10010100" = "00101101".

        Args:
            x (string): Premier élément de l'addition.
            y (string): Deuxième élément de l'addition.

        Returns:
            string: Résultat de l'addition x+y en binaire.
        """

        #BEGIN TODO
        z = ""
        for i in range(len(x)):
            z += self.addCayley(x[i], y[i])
        return z
        #END TODO

    def transformToBinary(self, x):
        '''
        Transforme un polynome à coefficients quelconques à coefficents binaires
        :param x: Une liste contenant les coefficients non binaires
        :return: Une liste contenant les coefficient binaires
        '''
        for i in range(len(x)):
            if x[i] % 2 == 0:
                x[i] = 0
            else:
                x[i] = 1
        return x

    def multiply(self, x, y, pol):
        """
        Multiplie deux séquences binaires (x*y) reçues sous la forme de string, en utilisant
        le polynôme irréductible choisi pour le corps.

        Exemple : "10111001" * "10010100" = "10110010" avec comme pol: "101001101"

        Args:
            x (string): Premier élément de la multiplication.
            y (string): Deuxième élément de la multiplication.
            pol (string): Polynome irréductible

        Returns:
            string: Résultat de la multiplication x*y en binaire.
        """
        #BEGIN TODO
        mult = "0"*8
        while y != "0"*8:
            if y[-1] == "1":
                mult = self.add(mult, x)
            x += "0"
            if x[0] == "1":
                x = self.add(x, pol)[1:]
            else:
                x = x[1:]
            y = "0" + y[:-1]
        return mult
        #END TODO
    
    
    def inverse(self, x, pol):
        """
        Inverse un élément x du corps donné (donne x^(-1)) sous la forme d'une séquence binaire.

        Exemple : ("10111001")^(-1) = "10001110" avec comme pol: "101001101"

        Args:
            x (string): Elément à inverser.
            pol (string): Polynome irréductible

        Returns:
            string: Résultat de l'inversion en binaire.
        """
        #BEGIN TODO
        z = "00000001"
        for i in range(7):
            x = self.multiply(x, x, pol)
            z = self.multiply(z, x, pol)

        return z
        #END TODO

class ReedSolomon():
    def __init__(self, k, n, y, pol):
        """
        Args:
            k (int): dimension des messages à transmettre.
            n (int): taille du bloc que l'on souhaite transmettre.
            y (liste de string de taille n): les points d'interpolation yi.
            pol (string): polynome irréductible.
        """
        self.f = BinaryDomains()
        self.t = Translation()
        self.k = k
        self.n = n
        self.y = y
        self.pol = pol

    def _evaluate(self, polynome, x):
        """
        Evalue le polynome A(x) au point x

        Args:
            polynome (liste de strings (octets) de taille k): le polynome
            x (string): point d'évaluation
        Returns:
            (string): la valeur du polynome en x
        """
        y = polynome[-1]
        for i in range(len(polynome)-2, -1, -1):
            y = self.f.add(self.f.multiply(y, x, self.pol), polynome[i])
        return y

    def encoding(self, message_original):
        """
        Encode le message à stocker sous la forme d'une liste comportant n bytes/octets.

        Args:
            message_original (string): Le message original a encodé.
        
        Returns:
            (liste de string de taille n): Le message encodé.
        """
        #BEGIN TODO
        a = self.t.translateToMachine(message_original)
        I = [self._evaluate(a, self.y[i]) for i in range(self.n)]
        return I
        #END TODO

    def vandermonde(self, y):
        '''
        Créé une matrice de Vandermonde
        :param y: (liste de string de taille k): Les points yi.
        :return: matrice de Vandermonde
        '''
        V = numpy.full((self.k, self.k), "00000000")
        for i in range(self.k):
            V[i][0] = "00000001"
            for j in range(self.k - 1):
                V[i][j + 1] = self.f.multiply(V[i][j], y[i], self.pol)
        return V
    def gaussian_elimination(self, y, I):
        """
        Ex: k = 4: retourne les coefficients (ai) du polynôme A(Y) = a0 + a1*Y + a2*Y^2 + a3*Y^3
        en partant de 4 points (yi,A(yi)) = (yi,Ii).

        Ce problème est généralisé pour tout k.
        Pour le résoudre -> Effectuer l'élimination de Gauss-Jordan sur le système Va = I.
        Avec V la matrice de Vandermonde.
        
        Args:
            y (liste de string de taille k): Les points yi.
            I (liste de string de taille k): Les points Ii=A(yi).
        
        Returns:
            (liste de string de taille k): Les coefficients (ai) de l'interpolation.
        """
        #BEGIN TODO
        V = self.vandermonde(y)
        Y = numpy.array([I])
        P = numpy.concatenate((V, Y.T), axis=1) # matrice augmentée
        x = []

        for i in range(self.k):
            for j in range(self.k):
                if i!=j:
                    ### P[i,j]/P[i,i]
                    r = self.f.multiply(P[j, i], self.f.inverse(P[i, i], self.pol), self.pol)
                    for m in range(self.k+1):
                        ### a = -a
                        P[j,m] = self.f.add(P[j, m], self.f.multiply(r, P[i, m], self.pol))
        for i in range(self.k):
            x1 = self.f.multiply(P[i, self.k], self.f.inverse(P[i, i], self.pol), self.pol)
            x.append(x1)

        return x
        #END TODO

    def decoding(self, message_corrupted):
        """
        Décode le message corrompu sous la forme d'une liste comportant k bytes.

        Args:
            message_corrupted (liste de string de taille n): Le message 'corrompu' reçu.
        
        Returns:
            (bool): True s'il est possible de décoder le message corrompu, False sinon.
            (liste de string de taille k): Le message décodé. (si bool = False, alors retourner []).
        """
        #BEGIN TODO
        nbrCorrupted = 0
        messageNotCorrupted = []
        y = []
        for i in range(len(message_corrupted)):
            if "x" in message_corrupted[i]:
                nbrCorrupted +=1
            else:
                messageNotCorrupted.append(message_corrupted[i])
                y.append(self.y[i])

        minSafe = self.n-self.k
        if nbrCorrupted > minSafe:
            return False,[]
        
        I = messageNotCorrupted[:-len(messageNotCorrupted)+self.k]
        Y = y[:-len(y)+self.k]
        G = self.gaussian_elimination(Y, I)
        message = self.t.translateToHuman(G)
        return True,message
        
        #END TODO
