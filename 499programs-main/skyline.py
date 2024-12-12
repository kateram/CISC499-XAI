class Solution(object):
    def nse(self,arr):
        st = []
        ans = [len(arr) for i in range(len(arr))]

        for i in reversed(range(len(arr))):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            ans[i] = st[-1] if st else len(arr)
            st.append(i)
        return ans

    def pse(self,arr):
        st = []
        ans = [len(arr) for i in range(len(arr))]

        for i in range(len(arr)):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        nse = self.nse(heights)
        pse = self.pse(heights)
        max_diff = 0

        for i in range(len(heights)):
            diff = nse[i]-pse[i]-1
            height = heights[i]*diff

            max_diff = max(max_diff,height)

        return max_diff

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        start = 0
        max_value = 0
        
        while start < len(matrix[0]):
            prefix = 0
            for row in range(len(matrix)):
                prefix = prefix + int(matrix[row][start])
                if int(matrix[row][start]) != 0:
                    matrix[row][start] = prefix
                else:
                    matrix[row][start] = int(0)
                    prefix = 0
            start += 1
        
        for mat in matrix:
            value = self.largestRectangleArea(mat)
            max_value = max(value,max_value)
        
        return max_value

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
solution = Solution()
print(solution.maximalRectangle(matrix))