import itertools 
import math 
import time 

def is_cap(subset, memo):
    """check if a given subset of integers is a cap"""
    for quad in itertools.combinations(subset,4):
        quad_key = tuple(sorted(quad))
        if quad_key in memo:
            if memo[quad_key] == 0:
                return False
        else:
           xor_result = quad[0] ^ quad[1] ^ quad[2] ^ quad[3] #XOR Operation 
           memo[quad_key] = xor_result 
           if xor_result == 0: 
               return False
    return True 

def cap_function(n, k):
    """generate caps of size up to k in dimension n """
    deck = range(2**n)
    # caps = [[0], [1], ..., [2**n-1]]
    caps = [[i] for i in deck]
    for size in range(2, k+1):
        new_caps = []
        for cap in caps:
            # require that the cap is in numerical order
            for card in range(cap[-1] + 1, 2**n):
                # check if cap + card is a cap; if cap, add to new_caps list
                new_cap = cap + [card]
                if is_cap(new_cap, {}):
                    new_caps.append(new_cap)
        caps = new_caps 
    return caps 

def count_caps(n, max_r, sample_size):
    """compute Cr,n for r from 1 to max_r in dimension n"""
    results = {}
    for r in range(1, max_r+1):
        print(f"Computing C_{r},{n}...")
        caps = cap_function(n,r)
        total_caps = len(caps)
        total_processed = math.comb(2**n, r)
        results[r] = (total_caps, total_processed)
        print(f"Finished computing C_{r},{n}: {results[r]}") #debugging statement 
    return results 


if __name__ == "__main__":
    n = 4
    max_r = 13
    sample_size = 300000000

    #to measure performance 
    start_time = time.time()
    results_integers = count_caps(n, max_r, sample_size)
    integers_time = time.time() - start_time
    
    #print results 
    for r in range(1, max_r + 1):
        caps, processed = results_integers[r]
        print(f"C_{r},{n} = {caps}, Total subsets processed = {processed}")

    #print performance 
    print(f"Time using incremental caps: {integers_time} seconds")