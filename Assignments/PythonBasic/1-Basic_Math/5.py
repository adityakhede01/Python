# 5. If it costs 1600 rs. to fence a rectangular park of length 20 m at the rate of 25 rs. per m², find the breadth of the park and its perimeter. Also, find the area of the field.

length = 20
cost_to_fence = 1600
rate = 25

perimeter = cost_to_fence/rate
breadth = (perimeter / 2) - length
area = length * breadth

print("Breadth =", breadth, "m")
print("Perimeter =", perimeter, "m")
print("Area =", area, "m²")