class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        
        rows = [[0 for j in range((len(s)//2)+1)] for i in range(numRows)]
        
        active_row = 0
        active_column = 0
        
        topToBoottom = True
        
        for letter in s:
            rows[active_row][active_column]  = letter
            
            
            if(active_row == numRows - 1):
                topToBoottom = False
                
            if(active_row == 1 and not topToBoottom):
                topToBoottom = True
                active_row = -1
                active_column += 1
            
            if(topToBoottom):
                active_row += 1
            else:
                active_row -= 1
                active_column += 1
        
        
        result = ""
        for r in rows:
            for rr in r:
                if rr is not 0:
                    result += rr
        
        return result
          