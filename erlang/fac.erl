#!/usr/bin/env escript
%%! -smp enable -sname factorial -mnesia debug verbose

main([]) ->
    S = lists:sum([fac(X) || X <- lists:seq(1,3000)]),
    io:write(S).

fac(1) ->
    1;
fac(N) ->
    N * fac(N - 1).
