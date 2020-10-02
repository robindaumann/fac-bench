#!/usr/bin/env groovy

def fac(n) { (1G..n).inject { a, b -> a * b } }
println((1..3000).collect { fac it }.sum())
