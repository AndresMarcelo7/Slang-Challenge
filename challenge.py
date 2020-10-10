def calculateNGrams(text,n):
    """ given a piece of text and an integer n, it returns the n-grams for
        that text.

        According to python documentation: https://wiki.python.org/moin/TimeComplexity

        - Time Complexity for SLICE operation (python) -> O(k) where k is the slice size. 
        - Time Complexity for a loop -> O(n) where n is the number of iterations.
        
        in this function we do n times the slicing operation, so the final time
        complexity is O(n*k);
    """
    iterations = (len(text) - n) + 1
    ans = [text[i:i+n] for i in range(iterations)]
    return ans;

def mostFrequentNGram(text,n):
    """
         given a piece of text and an integer n, it returns only the most frequent n-gram for that text

         In this case there are several things to consider:

         - use of calculateNGrams -> O(n*k)
         - Time complexity for a loop -> O(n)
         - python Dict SET/GET Operations -> O(1) (O(n) in the worst case scenario)

         So the total Time complexity would be O(n) + O(n*k) = O(n*k) or O(n^2) in the worst case scenario.
         
    """
    nGrams = calculateNGrams(text,n)
    frequencies = {}
    ans = [0,None]
    for nGram in nGrams:
        if (nGram not in frequencies):
            frequencies[nGram] = 1
            
        else:
            frequencies[nGram] += 1
            
        if (ans[0] < frequencies[nGram]):
            ans[0] = frequencies[nGram]
            ans[1] = nGram
    return ans[1];
    
