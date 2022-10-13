with open('input', 'r') as f:
    for count, line in enumerate(f, start=1):
        if count % 2 == 0:
            print (line)