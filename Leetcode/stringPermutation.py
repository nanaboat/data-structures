class StringPermutation:
    def permute(self, astring: str):
        word_count = {}
        for char in astring:
            if char in word_count:
                word_count[char] += 1
            else:
                word_count[char] = 1
        word = [None] * len(word_count)
        count = [None] * len(word_count)
        i = 0
        for k, v in word_count.items():
            word[i] = k
            count[i] = v
            i += 1
        result = [None] * len(astring)
        self.permuteUtil(word, count, result, 0)
        #return result
    
    def permuteUtil(self, astr, count, result, level):
        #import pdb; pdb.set_trace()
        if level == len(result):
            print(''.join(result))
            return True
        for i, char in enumerate(astr):
            if count[i] > 0:
                result[level] = char
                count[i] -= 1
                self.permuteUtil(astr, count, result, level + 1)
                count[i] += 1
    
    def strPermutations(self, astring):
        return self.permUtil('', astring)
    
    def permUtil(self, astr, rem):
        if rem == '':
            print(astr)
        else:
            for i, char in enumerate(rem):
                temp = astr + char
                rest = rem[0:i] + rem[i+1:]
                self.permUtil(temp, rest)



if __name__ == '__main__':
    StringPermutation().permute('ab')
    StringPermutation().strPermutations('ab')