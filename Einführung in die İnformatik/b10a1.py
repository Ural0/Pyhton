
#b10a1
def todigitlist(s: str)-> list:
	return [int(i) for i in s]

def sum_unique_even_squares(lis):
    return sum([i ** 2 for i in set(lis) if abs(i % 2) == 0])


def alt_digit_sum(zahl):
    return sum(int(y) if i%2==0 else -(int(y)) for i, y in enumerate(str(zahl)))


#1
print(todigitlist(""))
print(todigitlist("68423"))

#2
print(sum_unique_even_squares([1,2,3,4])) # `20`  (= `2^2 + 4^2`)
print(sum_unique_even_squares([1,2,3,4,2])) # 20  (= `2^2 + 4^2`)
print(sum_unique_even_squares([1,-2,3,4,2])) # 24  (= `(-2)^2 + 4^2 + 2^2`)


#3
print(alt_digit_sum(12)) # -1
print(alt_digit_sum(52876)) # 10