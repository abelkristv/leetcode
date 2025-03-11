class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        str_win = list(s)
        length = len(str_win)
        i = 0
        k = 0
        counter = {'a': 0, 'b': 0, 'c': 0}
        counterAll = 0
        isabc = False
        while k < length:
            # print(k)
            counter[str_win[k]] += 1
            while counter['a'] > 0 and counter['b'] > 0 and counter['c'] > 0:
                counterAll += length - k
                counter[str_win[i]] -= 1
                i += 1
            k += 1
        return counterAll