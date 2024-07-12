
"""
key: monotonic stack

"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        monotonic_stack = []
        temp_len = len(temperatures)
        answer = [0] * temp_len

        def add_monotonic_stack_decreasing(stack, item):
            # For this stack an item will be made up of [0, 1]
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


        for i in range(temp_len - 1, -1, -1):
            day_found = False
            current_day_temperature = temperatures[i]
            while len(monotonic_stack) > 0:
                candidate_day = monotonic_stack[len(monotonic_stack) - 1]
                if current_day_temperature < candidate_day[0] :
                    answer[i] = candidate_day[1] - i
                    day_found = True
                    break
                else:
                    monotonic_stack.pop()

            if not(day_found):
                # There are not warmer days.
                answer[i] = 0

            add_monotonic_stack_decreasing(monotonic_stack, [temperatures[i], i])

        return answer
                    