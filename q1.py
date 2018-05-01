def question1(s, t):
    len_t = len(t)
    len_s = len(s)
    list_t = list(t)
    list_t.sort()     # Quick sort O(n*log(n))

    for i in range(len_s - len_t + 1):
        if check_anagram(s[i: i+len_t], list_t):
            return True
    return False

def check_anagram(part_s, list_t):
    part_s = list(part_s)
    part_s.sort()   
    return part_s == list_t

def main():
    print question1("udacity", "ud")

if __name__ == '__main__':
    main()
