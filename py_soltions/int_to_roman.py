class Solution:
    def intToRoman(self, num: int) -> str:
        all_integers = [1,5,10,50,100,500,1000,4,9,40,90,400,900]
        all_romans = ["I","V","X","L","C","D","M","IV","IX","XL","XC","CD","CM"]
        integers = [1,5,10,50,100,500,1000]
        roman = ["I","V","X","L","C","D","M"]
        res = ""
        while num > 0:
            ms_digit = get_ms_digit(num)
            if ms_digit in all_integers:
                num -= ms_digit
                res += all_romans[all_integers.index(ms_digit)]
            else:
                for i in range(len(integers) - 1, -1, -1):
                    if ms_digit > integers[i]:
                        num -= integers[i]
                        res += roman[i]
                        break
        return res


def get_ms_digit(num):
    factor = 0
    while num > 10:
        num = int(num / 10)
        factor += 1
    return num * (10 ** factor)

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3749))
    assert s.intToRoman(3749) == "MMMDCCXLIX"