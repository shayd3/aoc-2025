def solve():
    try:
        with open('input[1].txt', 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: input[1].txt not found.")
        return

    # --- Part 1 ---
    # Find the largest possible number formed by exactly two batteries.
    total_joltage_p1 = 0
    for line in lines:
        digits = [int(c) for c in line]
        n = len(digits)
        max_val = -1
        
        # Iterate all pairs (i, j) with i < j
        for i in range(n):
            for j in range(i + 1, n):
                val = digits[i] * 10 + digits[j]
                if val > max_val:
                    max_val = val
        
        if max_val != -1:
            total_joltage_p1 += max_val

    print(f"Part 1 Total Output Joltage: {total_joltage_p1}")

    # --- Part 2 ---
    # Find the largest possible number formed by exactly twelve batteries.
    total_joltage_p2 = 0
    
    for line in lines:
        digits = [int(c) for c in line]
        n = len(digits)
        needed = 12
        
        if n < needed:
            continue
            
        current_idx = -1
        result_digits = []
        
        # We need to pick 'needed' digits one by one
        for k in range(needed, 0, -1):
            # To ensure we can still pick (k-1) digits after this one,
            # we must pick the current digit from the range:
            # [current_idx + 1, n - k]
            
            start_search = current_idx + 1
            end_search = n - k 
            
            best_digit = -1
            best_digit_idx = -1
            
            # Greedy Strategy: 
            # 1. Find the largest digit value in the valid range.
            # 2. If there are ties, pick the FIRST occurrence (smallest index).
            #    This leaves the largest possible suffix for the remaining digits.
            for i in range(start_search, end_search + 1):
                if digits[i] > best_digit:
                    best_digit = digits[i]
                    best_digit_idx = i
                # Optimization: 9 is the max possible digit
                if best_digit == 9:
                    break
            
            result_digits.append(best_digit)
            current_idx = best_digit_idx
            
        # Convert the list of 12 digits into a single integer and add to total
        val_str = "".join(str(d) for d in result_digits)
        total_joltage_p2 += int(val_str)

    print(f"Part 2 Total Output Joltage: {total_joltage_p2}")

if __name__ == '__main__':
    solve()
