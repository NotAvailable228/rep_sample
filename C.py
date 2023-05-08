
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0]*(n-k+1)
    ind = (k)//2
    arr = sorted([(a[i],i) for i in range(k)])
    
    cur_med = arr[ind]
    ans[0] = cur_med
    lower = set()
    higher = set()
    for i in range(k//2):
        lower.add(arr[i])
        higher.add(arr[i+ind+1])
    for i in range(k,n):
        new_pair = (a[i], i)
        old_pair = (a[i-k], i-k)
        if old_pair in lower:
            lower.remove(old_pair)
        elif old_pair in higher:
            higher.remove(old_pair)
        else:
            cur_med = None
        if cur_med:
            lower.add(cur_med)
        if len(higher)==0 and max(lower)[0] <= new_pair[0]:
            higher.add(new_pair)
        elif len(higher)==0 and max(lower)[0] >= new_pair[0]:
            lower.add(new_pair)
        elif new_pair[0] >= min(higher)[0]:
            higher.add(new_pair)
        else:
            lower.add(new_pair)
        if len(lower) == len(higher) - 1:
            cur_med = max(lower)
            lower.remove(max(lower))
        elif len(lower) == len(higher) + 1:
            cur_med = min(higher)
            higher.remove(min(higher))
        elif len(lower) == len(higher) + 3:
            lower.add(min(higher))
            higher.remove(min(higher))
            cur_med = min(higher)
            higher.remove(min(higher))
        else:
            higher.add(max(lower))
            lower.remove(max(lower))
            cur_med = max(lower)
            lower.remove(max(lower))
        ans[i-k+1] = cur_med[0]
    print(*ans)
        
        
            
def med(arr, ind):
    ans = sorted(list(arr))
    return ans[ind][0]

main()

