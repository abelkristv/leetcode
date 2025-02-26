class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_num = ""
        while num > 0:
            if num / 1000 > 0:
                num = num - 1000
                roman_num += "M"
            elif (num + 100) / 1000 > 0:
                num = num - 1000 + 100
                roman_num += "CM"
            elif num / 500 > 0:
                num = num - 500
                roman_num += "D"
            elif (num + 100) / 500 > 0:
                num = num - 500 + 100
                roman_num += "CD"
            elif num / 100 > 0:
                num = num - 100
                roman_num += "C"
            elif (num + 10) / 100 > 0:
                num = num - 100 + 10
                roman_num += "XC"
            elif num / 50 > 0:
                num = num - 50
                roman_num += "L"
            elif (num + 10) / 50 > 0:
                num = num - 50 + 10
                roman_num += "XL"
            elif num / 10 > 0:
                num = num - 10
                roman_num += "X"
            elif (num + 1) / 10 > 0:
                num = num - 10 + 1
                roman_num += "IX"
            elif num / 5 > 0:
                num = num - 5
                roman_num += "V"
            elif (num + 1) / 5 > 0:
                num = num - 5 + 1
                roman_num += "IV"
            elif num / 1 > 0:
                num = num - 1
                roman_num += "I"
        return roman_num
        