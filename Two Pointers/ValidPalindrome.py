class Solution:

    @staticmethod
    def make_lower_string(s):
        """ 
        Making the string without any simbols like %$#@ 
        .isalnum() return True if string doesn't contain symbols
        """
        new_str = ""
        for ch in s:
            if ch.isalnum():
                new_str += ch.lower()
        return new_str

    def isPalindromeWithTwoPointers(self, s: str) -> bool:
        """
        Using Two Pointers algorithm, I made a function which
        mark the point at the start and at the end,
        and then I try to compare two characters, and if they aren't 
        simillar I return False, else I just increase the value of
        'right' and 'left' variables  

        """
        reformated_string = self.make_lower_string(s)
        len_of_string = len(reformated_string)
        left = 0 
        right = len_of_string - 1
    
        if len_of_string in (0, 1):
            return True

        while left < right:
            if reformated_string[left] != reformated_string[right]:
                return False
            else:
                left += 1
                right -= 1

        return True
        
    def isPalindromeWithSlice(self, s: str) -> bool:
        """
        Here I am trying to make a new_string without symbols,
        and then just with slices comparing two new_string
        """
        new_str = ""
        for ch in s:
            if ch.isalnum(): # Цифры и буквы символы удаляет
                new_str += ch.lower()
        return True if new_str[::-1] == new_str[::1] else False

if __name__ == "__main__":
    string = "A man, a plan, a canal: Panama"
    s = Solution()
    print(s.isPalindromeWithTwoPointers(string))