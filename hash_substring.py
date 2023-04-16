# python3

def read_input():
    input_type = input().rstrip()
    if "I" in input_type:
        pattern = input().rstrip()
        text = input().rstrip()
    elif "F" in input_type:
        test_numurs = input("Ievadi testa numuru: ")
        with open(f"tests/{test_numurs}", "r") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    d = 256
    q = 101
    p_len = len(pattern)
    t_len = len(text)
    p_hash = 0
    t_hash = 0
    h = pow(d, p_len-1, q)

    occurrences = []

    for i in range(p_len):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                occurrences.append(i)
        if i < t_len - p_len:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i+p_len])) % q
            if t_hash < 0:
                t_hash += q

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
