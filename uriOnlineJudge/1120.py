while True:
    d, s = input().split()
    if int(d) == 0 and int(s) == 0:
        break

    r = s.replace(d, "")

    print(0 if r.count("0") == len(r) else int(r))
