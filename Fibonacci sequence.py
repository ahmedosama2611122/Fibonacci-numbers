def main():
    num_terms = int(input("Enter the number of Fibonacci numbers you want: "))
    
    a, b = 0, 1
    
    print("Fibonacci sequence:")
    for _ in range(num_terms):
        print(a, end=" ")  
        a, b = b, a + b    

if __name__ == "__main__":
    main()
