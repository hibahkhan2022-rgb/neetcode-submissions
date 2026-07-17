class Solution:
    def isPalindrome(self, s: str) -> bool:
        result_list = []
        for letters in s:
            if letters.isalnum():
                result_list.append(letters.lower())
    

    #Here we can ignore any spaces or punctuation
        for i in range(len(result_list)):
            opposite_index = len(result_list) - 1 - i

            if result_list[i] != result_list[opposite_index]:
                return False
        return True
        


'''
The strategy here is to traverse through the input, add to a list, 
then set two pointers on the ends. If their values are equal to each other the output is true
Otherwise, it is false
'''
