def scramble(s1, s2):
    # your code here
    for i in s2:
        if i not in s1:
            return False
    return True
print(scramble('scriptingjava', 'javascript'))
def func(a):
    print(a[:4])
func("blablabla")