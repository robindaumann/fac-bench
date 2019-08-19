#!/usr/bin/env elixir

fac = fn n -> Enum.reduce(1..n, 1, &*/2) end
facBench = fn n -> 1..n
|> Enum.map(fac)
|> Enum.sum()
end

IO.write facBench.(3000)

