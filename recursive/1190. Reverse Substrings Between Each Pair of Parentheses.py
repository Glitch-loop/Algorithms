class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        final_s = ""

        def recursion(index, sub_str):
            current_sub = ""
            len_sub_str = len(sub_str)
            i = index

            while i < len_sub_str:
                if sub_str[i] == "(":
                    current_sub = "[" + current_sub
                    sub_problem = recursion(i + 1, sub_str)
                    current_sub = current_sub + sub_problem
                    i = i + len(sub_problem)
                elif sub_str[i] == ")":
                    current_sub += "]"
                    current_sub = current_sub[::-1]
                    break
                else:
                    current_sub += sub_str[i]
                
                i += 1
            
            return current_sub

        ordered_s = recursion(0, s)
        
        for char in ordered_s:
            if not(char in "[]"):
                final_s += char

        return final_s