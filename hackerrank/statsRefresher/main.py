import sys

if __name__ == '__main__':
    input = sys.stdin.readlines()
    first = int(input[0].strip())
    second = input[1].strip()

    second_array = list(map(int, second.split()))
    # mean 
    mean = sum(second_array) / first
    print(f"{mean:.1f}")

    second_array.sort()
    # median 
    # To get the median:
    # 1. Check if the number of elements is odd or even.
    # 2. If odd, the median is the middle element.
    # 3. If even, the median is the average of the two middle elements. 

    if first % 2 == 1: 
        median = second_array[first // 2]
    else:
        median = (second_array[first // 2 - 1] + second_array[first // 2]) / 2
    print(f"{median:.1f}")
    
    # mode
    # To find the mode:
    # 1. Count the frequency of each number.
    # 2. Identify the number(s) with the highest frequency.
    # 3. If multiple numbers have the same highest frequency, return the smallest one.

    # 1. Count the frequency of each number.
    count = {}
    for num in second_array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # 2. Identify the number(s) with the highest frequency.
    max_count = max(count.values())
    #
    mode_candidates = [num for num, cnt in count.items() if cnt == max_count]
    mode = min(mode_candidates)
    print(f"{mode:.1f}")

    # Standard Deviation
    variance = 0

    for num in second_array:
        variance += (num - mean) ** 2
    variance /= first
    stddev = variance ** 0.5
    print(f"{stddev:.1f}")

    # can we now implement Lower and Upper Boundary of the 95% Confidence Interval for the mean, separated by a space.
    # To calculate the 95% confidence interval for the mean:
    # 1. Calculate the standard error (SE) of the mean: SE = standard deviation / sqrt(sample size).
    # 2. Determine the z-score for a 95% confidence level (approximately 1.96 for large samples).
    # 3. Calculate the margin of error (ME): ME = z-score * SE.
    # 4. The confidence interval is then: (mean - ME, mean + ME).

    z_score = 1.96  # for 95% confidence
    margin_of_error = z_score * (stddev / (first ** 0.5))
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    print(f"{lower_bound:.1f} {upper_bound:.1f}")