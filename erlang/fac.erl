#!/usr/bin/env escript

main([]) ->
    S = lists:sum([fac(X) || X <- lists:seq(1,3000)]),
    io:write(S).

fac(N) ->
    lists:foldl(fun(X, Fac) -> X * Fac end, 1, lists:seq(1,N)).
