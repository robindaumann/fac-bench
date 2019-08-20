#!/usr/bin/env bash
set -euo pipefail

function bench() {
  DIR=$1
  printf "Language %s\n" "$DIR"
  (
    cd "$DIR" && ./build
  ) || return 1
  time ("$DIR/fac" >number)
  if ! diff -q expected number &>/dev/null; then
    printf "FAIL\n"
    return 1
  else
    printf "PASS\n"
  fi
}

if [ -n "${1-}" ]; then
  bench "$1" || exit 1
else
  export -f bench
  find . -type d -name '[!.]*' -maxdepth 1 -exec bash -c 'bench "$0"; printf "\n"' {} \;
fi
