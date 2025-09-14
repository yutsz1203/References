"""
Predict the Number

The example sequence 011212201220200112 ... is constructed as follows:  
1. The first element in the sequence is 0.  
2. For each iteration, repeat the following action: take a copy of the entire current sequence, replace 0 with 1, 1 with 2, and 2 with 0, and place it at the end of the current sequence. E.g.  
0 -> 01 -> 0112 -> 01121220 -> ...  
Create an algorithm which determines what number is at the Nth position in the sequence (using 0-based indexing).
Input:
Your program should read lines from standard input. Each line contains an integer N such that 0 <= N <= 3000000000.
Output:
Print out the number which is at the Nth position in the sequence.
#### Test 1
##### Input
5
##### Output
2
#### Test 2
##### Input
25684
##### Output
0
"""


def predict_number(N):
    count = 0
    while N > 0:
        # Find the largest power of 2 less than or equal to N
        p = 1 << N.bit_length() - 1
        N -= p
        count += 1  # popcount(N)
    return count % 3


if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        line = line.strip()
        if line:
            N = int(line)
            print(predict_number(N))

"""
Explanation:
Check N=5 across scales
At length 8 (half size 4): 5 ≥ 4, so N=5 is in the second half [4..7]; record one “second-half hit” and map to earlier half by N ← 5 - 4 = 1 (this corresponds to applying T once, i.e., +1 mod 3).

Now consider the smaller index N=1 at the next scale down (length 4, half size 2): 1 < 2, so it is in the first half; no hit here (no +1 at this scale).

Go one more scale (length 2, half size 1): 1 ≥ 1, so it is in the second half; record another hit and map N ← 1 - 1 = 0 (another +1 mod 3)

Falling into second half = number of transformations

1 transformation: 0 -> 1
2 transformations: 0 -> 1 -> 2
3 transformations: 0 -> 1 -> 2 -> 0

(no.of transform) mod % 3 gets the value at Nth 
"""
