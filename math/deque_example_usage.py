from collections import deque
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        values_deque = deque()
        operation_deque = deque()

        remaining_values_deque = deque()
        remaining_operation_deque = deque()

        current_numer = ""

        # The string only contains numbers
        if not("+" in s) and not("-" in s) and not("*" in s) and not("/" in s):
            return int(s)

        # Getting symbols and numbers
        for i, char in enumerate(s):
            top = None

            if char == " ":
                continue

            if char == "/" or char == "*" or char == "+" or char == "-":
                operation_deque.append(char)
                current_numer = ""
            else:
                if current_numer == "":
                    # A new number has been identfied.
                    current_numer += char
                    values_deque.append(int(current_numer))
                else:
                    # A number with 2 or more digits.
                    current_numer += char
                    values_deque[len(values_deque) - 1] = int(current_numer)

        
        # Solve * and / operations.
        while len(operation_deque) > 0 and len(values_deque) > 0:
            front =  operation_deque[0]
            
            if front == "+" or front == "-":
                x = values_deque.popleft()
                op = operation_deque.popleft()

                remaining_values_deque.append(x)
                remaining_operation_deque.append(op)
                

            if front == "/" or front == "*":
                # Perform the operation
                # Getting value for operation
                
                x = values_deque.popleft()
                y = values_deque.popleft()

                # Getting the operand
                op = operation_deque.popleft()
                # Performing operation
                if op == "/":
                    if y == 0:
                        values_deque.appendleft(0)
                    else:

                        values_deque.appendleft(int(x / y))
                else:
                    values_deque.appendleft(x * y)


        if len(values_deque) > 0:
            remaining_values_deque.append(values_deque.pop())

        # Solving + and - operations
        while len(remaining_operation_deque) > 0:
            op = remaining_operation_deque.popleft()

            x = remaining_values_deque.popleft()
            y = remaining_values_deque.popleft()

            if op == "+":
                remaining_values_deque.appendleft(x + y)
            else:
                remaining_values_deque.appendleft(x - y)


        return remaining_values_deque[0]