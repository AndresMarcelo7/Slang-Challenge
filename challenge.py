def calculateNGrams(text,n):
    iterations = (len(text) - n) + 1
    ans = [text[i:i+n] for i in range(iterations)]
    return ans;

def mostFrequentNGram(text,n):
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
    
def main():
    print(mostFrequentNGram("to be or not to be",2))
main()
    
