"""
  This problem can be easly solved using a monotonic stack, since you have to get
  the smallest lexicographical sub-sequence removing elements from the string, 
  you have to follow an "greedy algorithm approach", approach that might be
  possible using an monotonic stack.

  The problem is as follows:
    Removing the duplicate characters to get the smallest lexicographical sub-sequence

  Therefore:
    - We can delete the characters that has duplicate, so if a letter has not duplicates,
    that means that we can't remove it.
    - We have to get smallest lexicographical order for the subquences

  Having this considerations the solution for this problem could be:
    Use a increasing monotonic stack to maintain the order that is asked, so in this way 
    we are going to ask for the next greater letter; a -> b, b -> c, c -> k, k -> o, and so on,
    remember that it doesn't necessarely need to follow the alphabetic order.

    So, because it might appear lower letter than the current top, before of pop elements to 
    find the position where it will be we have to ask:
      - The charater to add is already in the stcak
        * If it is, then we can continue with the next letter; remember that by the type of stack
        that is being used, we always are going to maintain an increasing order, but it might be exceptions.

      - If the current letter is lower than top and top is going to appear later in the string.
        * That means that we have to pop the monotonic stack to find the position that will be the 
        current letter; It is in this case where the increasing order is being care.

      - If any of the previous statements were true, that means that this letter has not been appeared yet, so we can append it with any complications.

    Once we traverse all the string, we have only to retrive the information stored in the stack in a FIFO way to get the smallest lexicographical string.

    How to get the last time that a letter will appear in the string?
      It can easly be obtained using an dictionary, so you can traverse the string once, and being 
      updating the index for each letter, in this way, at the end of this preliminary loop, you will
      have in the stack the last time that a letter will appear.
      


"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        thisStack = []
        thisDict = {}
        solution = ""

        # Finding the last elements
        for i, char in enumerate(s):
            thisDict[char] = i


        for i, char in enumerate(s):
            lastPosition = thisDict[char]
            len_stack = len(thisStack)

            if len_stack > 0:
                if char in thisStack:
                    continue

                appended_char = False
                while len(thisStack) > 0:
                    top = thisStack[len(thisStack) - 1]
                    if char < top and i < thisDict[top]: 
                        # The current char is lower than top and it is not the last time that will appear the letter on the top
                        thisStack.pop()
                    else:
                        # That means that the letter is not going to appear later on the string
                        thisStack.append(char)
                        appended_char = True
                        break
                if not(appended_char):
                    thisStack.append(char)
            else:
                thisStack.append(char)

        for char in thisStack:
            solution += char

        return solution

