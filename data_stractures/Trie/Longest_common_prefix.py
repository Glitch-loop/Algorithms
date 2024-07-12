class Node(object):
    def __init__(self, num_array, terminal):
        self.alphabet = [None] * num_array
        self.terminal = False

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        trie = Node(26, False)

        def add_word_trie(trie, string, index):
            # Get the lenght of the string
            len_s = len(string)

            # Finish if we traverse all the string
            if index > len_s - 1:
                return

            # Get the ascii value
            ascii_value = ord(string[index])
            # We have to get the relative position in the current level of the Trie
            ascii_value -= 97
            
            # print("Value to add: ", string[index])

            # Verifying if the letter was not previously added.
            if trie.alphabet[ascii_value] == None:                
                # That means that in the current level of the trie, we are going to add a new trie.
                # The position represents the letter.
                trie.alphabet[ascii_value] = Node(26, False)


            if index == len_s - 1 and trie.alphabet[ascii_value]:
                # The current letter is the last one of the string.
                # That means, the node is a word.
                
                # print("Finish of a word")
                
                trie.alphabet[ascii_value].terminal = True

            add_word_trie(trie.alphabet[ascii_value], string, index + 1)

        def longest_common_prefix(trie, prefix):
            words_starting = 0
            position = 0

            for i in range(len(trie.alphabet)):
                # Exploring if there is not the current letter is not the beginning of a new word.
                if trie.alphabet[i] != None:
                    position = i
                    words_starting += 1 
            
            print(words_starting)
            if trie.alphabet[position].terminal == True and words_starting == 1:
                return prefix + chr(position + 97)
            elif trie.alphabet[position].terminal == True and words_starting >= 2:
                return prefix
            elif words_starting >= 2: 
                return prefix 
            else:
                return longest_common_prefix(trie.alphabet[position], prefix + chr(position + 97))

        # Validate if all strings starts with the same letter
        start_char = ""
        for string in strs:
            if string == "":
                return ""

            if start_char == "":
                start_char = strs[0][0]
                
            # The word is completly different (no common prefix)
            if string[0] != start_char:
             return ""

        # Creating Trie
        for string in strs:
            # Pass the words to add them in the Trie
            add_word_trie(trie, string, 0)

        # Longest Common Prefix
        prefix = longest_common_prefix(trie, "")
        
        return prefix