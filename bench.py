#!/usr/bin/env python3
import math
import sys
import os
import re
import operator
import tabulate
import subprocess
import argparse
import functools
from multiprocessing import Pool
from typing import NamedTuple


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dirs', metavar='dir', nargs='*', default=subdirs('.'),
                        type=is_dir, help="directory of the language to run")
    parser.add_argument('--debug', action="store_true",
                        help="print debug output if the build process fails")
    args = parser.parse_args()

    # This is done because lambdas can't be pickled, which is needed for pmap
    bench_p = functools.partial(bench, debug=args.debug)
    with Pool() as p:
        times = p.map(bench_p, args.dirs)
    times.sort(key=operator.attrgetter('time'))
    print_table(times)

    failed = [time for time in times if time.status != 'pass']

    return 1 if any(failed) else 0


class BenchResult(NamedTuple):
    lang: str
    time: float
    status: str


def bench(lang: str, debug: bool) -> BenchResult:
    time = math.inf

    build = subprocess.run("./build", cwd=lang, capture_output=True)
    if build.returncode != 0:
        status = 'builderror'
        if debug:
            print(lang, status, "\n", build.stderr.decode(), file=sys.stderr)
        return BenchResult(lang, time, status)

    bench = subprocess.run(["time", "-p", f"{lang}/fac"], capture_output=True)
    if bench.returncode != 0:
        status = 'error'
        return BenchResult(lang, time, status)

    time = parse_time(bench.stderr)

    number = to_number(bench.stdout)
    expected = get_expected()
    status = 'pass' if number == expected else 'fail'

    return BenchResult(lang, time, status)


def subdirs(path):
    """Yield directory names not starting with '.' under given path."""
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_dir():
            yield entry.name


def is_dir(path):
    if os.path.isdir(path):
        return path

    raise argparse.ArgumentTypeError(f"{path} does not exists")


def get_expected():
    with open('expected') as f:
        return int(f.read())


def parse_time(text):
    if match := re.search(r"(\d+\.\d+)", text.decode()):
        num = match.group(1)
        return float(num)

    return math.inf


def to_number(text):
    try:
        return int(text)
    except ValueError:
        return math.nan


def print_table(times):
    idxs = range(1, len(times)+1)
    t = tabulate.tabulate(times, headers='keys', showindex=idxs)
    print(t)


if __name__ == "__main__":
    code = main()
    sys.exit(code)
