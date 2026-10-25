# *             1
# **            2
# ****          4
# *******       7
# ***********   11

n=5
stars=1
for i in range(1,n+1):
    print("*" * stars)
    stars = stars + i + 1