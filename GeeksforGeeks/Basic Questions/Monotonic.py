def isMonotonic(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 

if __name__ == "__main__":
    A = [5, 15, 20, 10]
    print(isMonotonic(A))