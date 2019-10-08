#!/usr/bin/env perl6

sub postfix:<!> (Int $n) { [*] 2..$n }
print [+] (1..3000)>>.!
