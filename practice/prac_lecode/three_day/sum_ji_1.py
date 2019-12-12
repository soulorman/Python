# enconding: utf-8
def test(n):
    if 1 <= n <= 10**5:
        Product = 1
        Sum = 0
        while(n):
            Product *= n % 10
            Sum += n % 10
            n //= 10

        return Product - Sum

n = 234
print(test(n))
