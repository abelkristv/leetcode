class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        smallest_change = 1000000000
        for i in range(len(blocks) - k + 1):
            current_window = blocks[i:i + k]
            count = current_window.count('W')
            if count < smallest_change:
                smallest_change = count
        
        return smallest_change

