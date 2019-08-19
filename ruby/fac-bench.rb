#!/usr/bin/env ruby

def fac(n)
  (1..n).inject :*
end

def fac_bench(n)
  (1..n).map {|n| fac n}.inject :+
end

print fac_bench 3000
