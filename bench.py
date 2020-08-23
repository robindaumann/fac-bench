#!/usr/bin/env python3
import math
import sys
import os
import re
import operator
import tabulate
import subprocess
from multiprocessing import Pool
from typing import NamedTuple


def main(argv):
    if len(argv) > 1:
        langs = argv[1:]
    else:
        langs = subdirs('.')

    with Pool() as p:
        times = p.map(bench, langs)
    times.sort(key=operator.attrgetter('time'))
    print_table(times)

    failed = [time for time in times if time.status != 'pass']

    return 1 if any(failed) else 0


class BenchResult(NamedTuple):
    lang: str
    status: str
    time: float = math.inf


def bench(lang: str) -> BenchResult:
    build = subprocess.run("./build", cwd=lang, capture_output=True)
    if build.returncode != 0:
        status = 'builderror'
        if os.getenv("FACBENCH_DEBUG"):
            print(lang, status, "\n", build.stderr.decode(), file=sys.stderr)
        return BenchResult(lang, status)

    bench = subprocess.run(["time", "-p", f"{lang}/fac"], capture_output=True)
    if bench.returncode != 0:
        status = 'error'
        return BenchResult(lang, status)

    time = parse_time(bench.stderr)

    number = to_number(bench.stdout)
    expected = get_expected()
    status = 'pass' if number == expected else 'fail'

    return BenchResult(lang, status, time)


def subdirs(path):
    """Yield directory names not starting with '.' under given path."""
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_dir():
            yield entry.name


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
    code = main(sys.argv)
    sys.exit(code)
