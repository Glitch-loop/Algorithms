class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        string = ""
        changedCharater = False    
        if len(palindrome) <= 1:
            return string
        

        middle = ceil(len(palindrome) / 2)        

        for i, char in enumerate(palindrome):
            """
                If the characther is not a,
                it is not the middle of the string and
                the string has a odd lenght
            """
            
            if not(changedCharater):
                if len(palindrome) % 2 != 0: # Odd palindrome; exclude the middle
                    if ord(char) > 97 and i != middle: # If it is different from "a" andis not the middle
                        string += "a"
                        changedCharater = True
                    else:
                        string += char
                else: # Even palindrom; It has not a middle to exclude
                    print(ord(char))
                    if ord(char) > 97: # If it is different from "a"
                        string += "a"
                        changedCharater = True
                    else:
                        string += char
            else:
                string += char
        
        if palindrome[:] == string[:]:
            string = string[:-1] + "b"
        
        return string 