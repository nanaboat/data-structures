class HashTable:
    '''Hashtable implementation with python list using linear probing.
       Attributes:
       -_size: number of key-value entries in hashtable.
       -_slots: size allocated for key-value entries.
                Default value is 11 (integer).
       -_keys: list for key entries.
       -_values: list for value entries.
    '''

    def __init__(self, slots=11):
        self._size = 0
        self._slots = slots  # should be treated as immutable
        self._keys = [None] * self._slots
        self._values = [None] * self._slots

    def _alpha(self):
        '''Computes the load factor of the Hashtable.
           Returns:
             load factor (float).
        '''
        return self._size / self._slots  # load factor n/m

    def _prehash(self, word):
        '''Computes the ascii equivalent of a String or character.
           Args:
             word: String/character to be converted
           Returns:
             Ascii equivalent (Integer)
        '''
        sum = 0
        for char in word:
            sum += ord(char)
        return sum

    def _hash(self, key):
        '''Computes the hash using the division method
           Args:
             key: String/Integer/Character. Should be immutale.
           Returns:
             Hash of the key (Integer)
        '''
        if type(key) == str:
            val = self._prehash(key)
            return val % self._slots

        return key % self._slots

    def _rehash(self, oldhash):
        ''' Computes new hash when collision occurs. Uses linear probing.
            Args:
              oldhash: Previous hash (Integer)
            Returns:
              New hash (Integer)
        '''
        return (oldhash + 1) % self._slots

    def add(self, key, value):
        '''Adds new key - value pair to map.
           Args:
             key: String/Integer/Character. Should be immutable.
             value: String/Integer/Character
        '''
        hashVal = self._hash(key)
        # case 1: key doesn't exist
        if self._keys[hashVal] is None:
            self._keys[hashVal] = key
            self._values[hashVal] = value
            self._size += 1
        else:
            # case 2: key exists; we update value
            if self._keys[hashVal] == key:
                self._values[hashVal] = value
            # case 3: key slot is occupied with another key; rehash until
            # you find new / rightful slot
            else:
                nHashVal = self._rehash(hashVal)
                while self._keys[nHashVal] is not None and \
                        self._keys[nHashVal] != key:
                    nHashVal = self._rehash(nHashVal)
                if self._keys[nHashVal] == key:
                    self._values[nHashVal] = value
                else:
                    self._keys[nHashVal] = key
                    self._values[nHashVal] = value
                    self._size += 1
        if self._alpha() >= 0.7:
            self._resize()

    def exists(self, key):
        '''Checks if key exists in Hashtable.
           Args:
             key: Immutable object (Integer/String/Character)
           Returns:
             Boolean - True if key exists and False if otherwise
        '''
        success, hashVal = self._search(key)
        if success:
            return True
        else:
            return False

    def _search(self, key):
        '''Finds key in the hashtable. This is a helper method.
           Args:
             key: Immutable object (Integer/String/Character)
           Returns:
             Returns a tuple of a boolean and key's associated hashValue
        '''
        hashVal = self._hash(key)
        stop = False
        data = None
        pos = hashVal
        while self._keys[pos] is not None and not stop:
            if self._keys[pos] == key:
                stop = True
                data = pos
            else:
                pos = self._rehash(pos)
                if pos == hashVal:
                    stop = True
        if data:
            return stop, data
        else:
            return stop, data

    def get(self, key, default=None):
        '''Get the value associated to the key
           Args:
             key: Immutable object (Integer/String/Character)
             default: Value to return if Key not found. Default is None
           Returns:
             Value associated with key or default arg
        '''
        success, hashVal = self._search(key)
        if success:
            return self._values[hashVal]
        else:
            return default

    def remove(self, key):
        ''' Deletes a key from the hashtable.
            Raises a KeyError if key doesn't exist
        '''
        success, hashVal = self._search(key)
        if success:
            self._keys[hashVal] = False
            self._values[hashVal] = None
            self._size -= 1
        elif self._alpha() <= 1 / 3:
            self._resize(True)
        else:
            raise KeyError('{0} not found'.format(key))

    def __getitem__(self, key):
        '''Get the value associated to the key
           Args:
             key: Immutable object (Integer/String/Character)
           Returns:
             Value associated with key or raise a KeyError
        '''
        success, hashVal = self._search(key)
        if success:
            return self._values[hashVal]
        else:
            raise KeyError('{0} not found'.format(key))

    def __setitem__(self, key, value):
        '''Adds new key - value pair to map.
           Args:
             key: String/Integer/Character. Should be immutable.
             value: String/Integer/Character
        '''
        self.add(key, value)

    def __delitem__(self, key):
        ''' Deletes a key from the hashtable.
            Raises a KeyError if key doesn't exist
        '''
        self.remove(key)

    def _resize(self, shrink=False):
        '''Resize hashtable. Either expand or shrink.
           Args:
             shrink: Flag to indicate reduce hashtable slots
        '''
        if shrink:
            self._slots = self._slots // 2
        else:
            self._slots = self._slots * 2
        oldKeys = self._keys
        oldVals = self._values
        self._keys = [None] * self._slots
        self._values = [None] * self._slots
        self._size = 0
        for i, key in enumerate(oldKeys):
            if key is not None:
                self.add(key, oldVals[i])
            else:
                continue

    def size(self):
        '''Returns the size of the hashtable '''
        return self._size

    def __len__(self):
        '''Returns the size of the hashtable '''
        return self._size

# TODO: test methods, __repr__, __str__ methods
