def myAtoi(str):
        """
        :type str: str
        :rtype: int
        """
        int_max = 2**31 -1
        int_min = -2**31
        str_word = str.strip()
        if str_word == '':
            return 0
        #if str_word.startswith('+') or str_word.startswith('-'):
        else:
            if str_word.startswith('+') or str_word.startswith('-') or str_word[0].isdigit():
                length = len(str_word)
                i = 1
                int_word = str_word[0]
                while i < length and str_word[i].isdigit():
                    int_word += str_word[i]
                    i += 1
                import pdb; pdb.set_trace()
                if  len(int_word) == 1 and (int_word.startswith('+') or int_word.startswith('-')):
                    return 0
                else:
                    num = int(int_word)
                    if num > int_max:
                        return int_max
                    elif num < int_min:
                        return int_min
                    else:
                        return num
            return 0

if __name__ == "__main__":
    print(myAtoi('42'))
    print(myAtoi('+1'))
    print(myAtoi('-45 nana'))
    print(myAtoi('     '))