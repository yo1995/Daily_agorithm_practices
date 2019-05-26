from typing import List


class Solution:

    def lucky_numbers(self, nums: str, target: int) -> List[str]:
        """

        :param nums: the input phone number string
        :param target: the number we want to get with
        :return:
        """
        result = []
        self.helper(nums, target, "", 0, 0, 0, result)
        print(result)
        return result

    def helper(self, num: str, target: int, temp: str, pos: int, current: int, last: int, result: List[str]):
        if pos == len(num):
            if current == target:
                result.append(temp)
                pass
            return
        for i in range(pos, len(num)):
            if num[pos] == '0' and i != pos:
                break
                pass
            m: str = num[pos:i+1]
            n = int(m)
            if pos == 0:
                self.helper(num, target, temp + m, i+1, n, n, result)
            else:
                self.helper(num, target, temp + "+" + m, i + 1, current + n, n, result)
                self.helper(num, target, temp + "-" + m, i + 1, current - n, -n, result)
                self.helper(num, target, temp + "*" + m, i + 1, current - last + last * n, last * n, result)
                if n != 0 and last % n == 0:
                    self.helper(num, target, temp + "/" + m, i + 1, int(current - last + last / n), int(last / n), result)


if __name__ == '__main__':
    number = '7765332111'
    S = Solution()
    S.lucky_numbers(number, 888)
