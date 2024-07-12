class Solution(object):
    def minimumOperations(self, num):
        """
        :type num: str
        :rtype: int
        """
        arr_sol = [101]
        visited = set()

        def dfs(candiate_num, operations):
            len_num = len(candiate_num)
            if len_num == 0:
                arr_sol[0] = min(arr_sol[0], operations)
                return 
            elif len_num == 1:
                if candiate_num[len_num - 1] == "0":
                    arr_sol[0] = min(arr_sol[0], operations)
                    return
            else:
                if (
                        candiate_num[len_num - 2] == "0" and candiate_num[len_num - 1] == "0"
                    or  candiate_num[len_num - 2] == "2" and candiate_num[len_num - 1] == "5"
                    or  candiate_num[len_num - 2] == "5" and candiate_num[len_num - 1] == "0"
                    or  candiate_num[len_num - 2] == "7" and candiate_num[len_num - 1] == "5"
                    ):
                        arr_sol[0] = min(arr_sol[0], operations)
                        return
            
            if candiate_num in visited:
                return 

            for i in range(len_num - 1, -1, -1):
                current_num = ""
                for j in range(len_num):
                    if j != i:
                        current_num += candiate_num[j]

                dfs(current_num, operations + 1)
                visited.add(current_num)

        dfs(num, 0)
        return arr_sol[0]
        
