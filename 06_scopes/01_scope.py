def chai_coder(num):
    def actual(x):
        return x**num

    return actual


f = chai_coder(2)
g = chai_coder(3)

print(f(2))
print(g(3))
