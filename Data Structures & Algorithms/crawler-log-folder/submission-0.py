import re

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_count = 0
        for op in logs:
            if op == "../":
                if folder_count > 0:
                    folder_count -= 1
            elif op == "./":
                continue 
            else:
                folder_count += 1

        return folder_count