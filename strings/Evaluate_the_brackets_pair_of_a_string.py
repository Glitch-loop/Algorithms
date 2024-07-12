import re

class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        thisDict = {}
        final_s = ""
        key = ""
        is_key = False

        # Convert array to dictionary
        for item in knowledge:
            thisDict[item[0]] = item[1]

        # Search for all the keys in the text
        for character in s:
            if character == '(':
                is_key = True
            elif character == ')':
                if key in thisDict:
                    final_s += thisDict[key]
                else:
                    final_s += "?"
                
                is_key = False
                key = ""
            else:
                if is_key:
                    key += character
                else:
                    final_s += character

        return final_s

    def regex_solution(s, knowledge):
        pattern = r'\(([a-z]+)\)'
        res_s = s

        # Replace the matches with the values in knowledge list.
        for item in knowledge:
            current_pattern = '\(' + item[0] + '\)'
            
            res_s = re.sub(current_pattern, item[1], res_s)

        # Replace those reamining keys that we don't know
        res_s = re.sub(pattern, "?", res_s)

        return res_s