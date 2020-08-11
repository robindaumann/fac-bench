module Main where

fac :: Integer -> Integer
fac n = foldl (*) 1 [1..n]

main :: IO ()
main = print . sum $ map fac [1..3000]
