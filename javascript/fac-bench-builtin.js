#!/usr/bin/env node

function fac(n) {
  let res = 1n;
  for (; n > 0; n--)
    res *= BigInt(n);
  return res;
}

function facbench(n) {
  let res = 0n;
  for (; n > 0; n--)
    res += fac(n);
  return res;
}

process.stdout.write(facbench(3000).toString());
