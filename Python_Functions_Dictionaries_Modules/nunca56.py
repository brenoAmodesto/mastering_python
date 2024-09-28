# Introdução ás Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n

        if n > maximum:
            return

        n+= 1

gen = generator()


for n in gen:
    print(n)