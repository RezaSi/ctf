from pwn import *
import random
import copy

# A Python program to count all subsets with given sum.
 
# dp[i][j] is going to store True if sum j is
# possible with array elements from 0 to i.
dp = [[]]
 
found = None
def display(v):
    print(v)
 
# A recursive function to print all subsets with the
# help of dp[][]. list p[] stores current subset.
def printSubsetsRec(arr, i, sum, p):
    global found
    if found:
        return
   
    # If we reached end and sum is non-zero. We print
    # p[] only if arr[0] is equal to sum OR dp[0][sum]
    # is True.
    if (i == 0 and sum != 0 and dp[0][sum]):
        p.append(arr[i])
        found = copy.deepcopy(p)
        return
 
    # If sum becomes 0
    if (i == 0 and sum == 0):
        found = copy.deepcopy(p)
        p = []
        return
 
    # If given sum can be achieved after ignoring
    # current element.
    if (dp[i-1][sum]):
        # Create a new list to store path
        b = []
        b.extend(p)
        printSubsetsRec(arr, i-1, sum, b)
 
    # If given sum can be achieved after considering
    # current element.
    if (sum >= arr[i] and dp[i-1][sum-arr[i]]):
        p.append(arr[i])
        printSubsetsRec(arr, i-1, sum-arr[i], p)
 
# Prints all subsets of arr[0..n-1] with sum 0.
def printAllSubsets(arr, n, sum):
    if (n == 0 or sum < 0):
        return
 
    # Sum 0 can always be achieved with 0 elements
    global dp
    dp = [[False for i in range(sum+1)] for j in range(n)]
 
    for i in range(n):
        dp[i][0] = True
 
    # Sum arr[0] can be achieved with single element
    if (arr[0] <= sum):
        dp[0][arr[0]] = True
 
    # Fill rest of the entries in dp[][]
    for i in range(1, n):
        for j in range(0, sum + 1):
            if (arr[i] <= j):
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i]])
            else:
                dp[i][j] = dp[i - 1][j]
 
    if (dp[n-1][sum] == False):
        return
 
    # Now recursively traverse dp[][] to find all
    # paths from dp[n-1][sum]
    p = []
    printSubsetsRec(arr, n-1, sum, p)

items = [184899, 180940, 177495, 179175, 186460, 132672, 179992, 175127, 182064, 190849, 180142, 166687, 135873, 138238, 139042, 171338, 188709, 94108, 181443, 186329, 188198, 176833, 123861, 180518, 138651, 178432, 139498, 139631, 182653, 135308, 177690, 185098, 181968, 143365, 172008, 134759, 181115, 180009, 135360, 81995, 179259, 187957, 83339, 135139, 179925, 175843, 183503, 88852, 170594, 136926, 181928, 133161, 138758, 184936, 171663, 174990]
coins = [43250, 46663, 49640, 42053, 41259, 40728, 49556, 46103, 40806, 48824, 47375, 40249, 49575, 43920, 40276, 49967, 41168, 45948, 46583, 47116, 43758, 41777, 41290, 44027, 48691, 41652, 42990, 44613, 40445, 42227, 43547, 48701, 42702, 47468, 48063, 40862, 45871, 44349, 40496, 45571, 45810, 41900, 48950, 44451, 45214, 48421, 45458, 45763, 49020, 42193, 44520, 43303, 49608, 47475, 41519, 44623, 45511, 45396, 42234, 48329, 49339, 40542, 41121, 48161, 45270, 40565, 44268, 40662, 43632, 41613, 45506, 49314, 49420, 45295, 49644, 44427, 44303, 48474, 44701, 47951, 42023, 43061, 41087, 47884, 47855, 49015, 43198, 45525, 47939, 49915, 42492, 47583, 45707, 47555, 42558, 46034, 49012, 47755, 46963, 45351, 46170, 41923, 46482, 40455, 41660, 47366, 44867, 49561, 48577, 45331, 40440, 46613, 42626, 49202, 41615, 47783, 48791, 40161, 46162, 47399, 45904, 44405, 43623, 42463, 43145, 46707, 42453, 44482, 45271, 47697, 49434, 49182, 47526, 48160, 45894, 49878, 43247, 44843, 41925, 43076, 47867, 41643, 47109, 46179, 42921, 43539, 49647, 44200, 42270, 48382, 43479, 42137, 44409, 40572, 44479, 42997, 43544, 46947, 49129, 45073, 46985, 40319, 40476, 48754, 44177, 41433, 40789, 49053, 46257, 47890, 49882, 41021, 42241, 48165, 47385, 40026, 46681, 42519, 44120, 45709, 45287, 45697, 46973, 44518, 48798, 49793, 45539, 43252, 40954, 48880, 42184, 45136, 41070, 46260, 43834, 44299, 42970, 40640, 49550, 44305]
for item in items:
    for i in range(0, 30):
        sum = 184899
        printAllSubsets(coins, len(coins), item + i)
        if found:
            print(item, i, found)
            for f in found:
                del coins[coins.index(f)]
            found = None
            break
 
# This code is contributed by Lovely Jain