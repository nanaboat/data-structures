'''
Implement a method to perform basic string compression using
the counts of repeated characters. For example, the string 'aabcccccaaa'
would become a2b1c5a3. If the "compressed" string would not become
smaller than the original string, your method should return the original string.
'''


def compress(astring):
    if len(astring) < 3:
        return astring
    i = 0
    result = []
    for idx in range(1, len(astring)):
        i += 1
        if astring[idx] != astring[idx - 1]:
            result.append(astring[idx - 1])
            result.append(str(i))
            i = 0
        
        # check if we are at the end of the string 
        if idx == len(astring) - 1:
            result.append(astring[idx])
            if astring[idx] != astring[idx - 1]:
                result.append('1')
            else:
                i += 1
                result.append(str(i))
        # check if compressed string so far exceeds original string
        if len(result) > len(astring):
            return astring
    
    return ''.join(result)


if __name__ == '__main__':
    print(compress('aabcccccaaa'))
