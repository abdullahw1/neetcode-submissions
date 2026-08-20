class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        if n == 0:
            return 0
        
        write_idx = 0
        i = 0
        
        while i < n:
            char = chars[i]
            count = 0
            
            # Count consecutive repeating characters
            while i < n and chars[i] == char:
                count += 1
                i += 1
                
            # Write the character
            chars[write_idx] = char
            write_idx += 1
            
            # If count is greater than 1, convert to string and write digits
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write_idx] = digit
                    write_idx += 1
                    
        return write_idx