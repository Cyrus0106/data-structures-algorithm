# O(n) Manacher's Algorithm
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # Transform s to add boundaries to handle even length palindromes
    t = "#" + "#".join(s) + "#"
    n = len(t)

    P = [0] * n  # Array to store palindrome radii
    center = right = 0  # Current center and right boundary
    max_len = 0  # Length of longest palindrome found
    max_center = 0  # Center of longest palindrome found

    for i in range(n):
        mirror = 2 * center - i  # Mirror position of i with respect to center

        # If i is within the right boundary, use previously computed value
        if i < right:
            P[i] = min(right - i, P[mirror])

        # Attempt to expand palindrome centered at i
        a, b = i + (1 + P[i]), i - (1 + P[i])
        while a < n and b >= 0 and t[a] == t[b]:
            P[i] += 1
            a += 1
            b -= 1

        # Update center and right boundary if expanded past right
        if i + P[i] > right:
            center, right = i, i + P[i]

        # Update max palindrome length and center
        if P[i] > max_len:
            max_len = P[i]
            max_center = i

    # Extract the longest palindrome from the original string
    start = (max_center - max_len) // 2
    return s[start : start + max_len]


# O(n^2) Solution: Expand Around Center
def longestPalindrome2(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    start, end = 0, 0  # Indices of the longest palindrome found

    def expand(left, right):
        # Expand as long as the substring is a palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  # Return the bounds of the palindrome

    for i in range(len(s)):
        # Odd length palindrome
        l1, r1 = expand(i, i)
        # Even length palindrome
        l2, r2 = expand(i, i + 1)

        # Update longest palindrome if necessary
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start : end + 1]


# O(n^3) Solution: Brute Force
def longestPalindrome3(s):
    """
    :type s: str
    :rtype: str
    """
    longest = ""
    n = len(s)

    for i in range(n):
        start_char = s[i]
        # Find all occurrences of start_char after position i
        j = s.find(start_char, i + 1)
        while j != -1:
            substring = s[i : j + 1]
            # Check if substring is a palindrome and longer than current longest
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
            j = s.find(start_char, j + 1)

    # If no multi-char palindrome found, return first character
    return longest if longest else s[0]
