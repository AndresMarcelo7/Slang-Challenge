def calculateNGrams(text,n):
    ans = [text[i:i+n] for i in range(n)]
    return ans;

def main():
    print(calculateNGrams("Slang",3))
main()
    
