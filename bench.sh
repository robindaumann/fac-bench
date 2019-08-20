#!/usr/bin/env bash
set -euo pipefail

function bench() {
  DIR=$1
  (
    cd "$DIR" && ./build
  )
  echo "Language $DIR"
  time ("$DIR/fac" >number)
  if ! diff -q expected number &>/dev/null; then
    echo -e "FAIL\n"
    exit 1
  else
    echo -e "PASS\n"
  fi
}

if [ -n "${1-}" ]; then
  bench "$1"
else
  export -f bench
  find . -type d -name '[!.]*' -maxdepth 1 -exec bash -c 'bench "$0"' {} \;
fi
