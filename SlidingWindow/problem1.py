# def prm_in_str(str , patt):
#     pat_len = len(patt)
#     window_start = 0
#     premu_arr = {}
#     for window_end in range(len(str)):
#         right_char = str[window_end]
#         if window_end == pat_len:
#             if right_char  not in premu_arr:
#                 window_start+=1
# neet code
def checkInclusion(s1,s2)-> bool:
    if len(s1) > len(s2) : return False
    
    s1count , s2count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1count[ord(s1[i]) - ord("a")] +=1
        s2count[ord(s2[i])- ord("a")] +=1
    matches = 0
    for i in range(26):
        matches +=(1 if s1count[i] == s2count[i] else  0 )
    left = 0
    for right in range(len(s1), len(s2)):
        if  matches == 26 : return True
        index = ord(s2[right]) - ord("a")
        s2count[index] +=1
        if s1count[index] == s2count[index]:
            matches +=1
        elif  s1count[index] + 1 == s2count[index]:
              matches -=1
        # left
        index = ord(s2[left]) - ord("a")
        s2count[index] -=1
        if s1count[index] == s2count[index]:
            matches +=1
        elif  s1count[index] - 1 == s2count[index]:
              matches -=1
        left +=1
        return matches == 26

def main():
    print(" permutation occur " + str(checkInclusion("abc", "oidbcaf")))
main()