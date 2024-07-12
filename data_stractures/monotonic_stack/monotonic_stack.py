class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        monotonic_stack = []

        def add_monotonic_stack_increasing(stack, item):
            # For this stack an item will be made up of [0, 1]
            # Each position represents [warmness, position in the array]
            added = False

            while not(added) and len(stack) > 0:
                top = len(stack) - 1
                if item[0] > stack[top][0]:
                    stack.append(item)
                    added = True
                else:
                    stack.pop()

            # If added is in false, that means that the stack got empty.
            if not(added):
                stack.append(item)
        
        def add_monotonic_stack_decreasing(stack, item):
            # For this stack one item will be made up of [0, 1]
            # Each position represents [warmness, position in the array]
            added = False

            while not(added) and len(stack) > 0:
                top = len(stack) - 1
                if item[0] < stack[top][0]:
                    stack.append(item)
                    added = True
                else:
                    stack.pop()

            # If added is in false, that means that the stack got empty.
            if not(added):
                stack.append(item)
          

        for i in range(len(temperatures)):
          add_monotonic_stack_decreasing(monotonic_stack, [temperatures[i], i])  
        
        print(monotonic_stack)
            
        return []
                    
def main():
    s = Solution()
    
    # print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
    # print(s.dailyTemperatures([30,40,50,60]))
    
    print(s.dailyTemperatures([73, 76, 72, 69]))

main()