def calculateNGrams(text,n):
    iterations = (len(text) - n) + 1
    ans = [text[i:i+n] for i in range(iterations)]
    return ans;

def main():
    print(calculateNGrams("Slang",1))
main()
    
