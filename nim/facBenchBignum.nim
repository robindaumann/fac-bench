import bignum

proc fac*(n: int): Int =
  result = newInt(1)
  for i in 1..n:
    discard result.mul(result, i)

proc facBench*(n: int): Int =
  result = newInt(0)
  for i in 1..n:
    discard result.add(result, fac(i))

stdout.write facBench 3000
