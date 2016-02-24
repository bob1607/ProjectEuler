low = 100
high = 999
HighestPalindrome = 0
lenghtOfMaxNumber = len(str(high*high))
mid = int(lenghtOfMaxNumber/2)

for x in range(low, high):
    for y in range(low, high):
        if((str(x * y)[mid:] == str(x * y)[::-1][mid:]) and ((x * y) > HighestPalindrome)):
            HighestPalindrome = x * y
print(HighestPalindrome)
