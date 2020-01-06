#!/usr/bin/env python3
import math
import sys
import os
import re
import operator
import tabulate
import subprocess
from dataclasses import dataclass


def main(argv):
    if len(argv) > 1:
        langs = [argv[1]]
        debug = True
    else:
        langs = subdirs(".")
        debug = False

    times = []
    for lang in langs:
        times.append(bench(lang, debug))

    times.sort(key=operator.attrgetter('time'))
    print_table(times)

    return len([time for time in times if time.res != "pass"])


def bench(lang, debug):
    res = BenchResult(lang)

    build = subprocess.run("./build", cwd=lang, capture_output=True)
    if build.returncode != 0:
        res.res = "builderror"
        if debug:
            print(lang, res.res, "\n", build.stderr.decode(), file=sys.stderr)
        return res

    bench = subprocess.run(["time", "-p", f"{lang}/fac"], capture_output=True)
    if bench.returncode != 0:
        res.res = "error"
        return res

    res.time = parse_time(bench.stderr)

    number = to_number(bench.stdout)
    expect = get_expected()
    res.res = "pass" if number == expect else "fail"

    return res


def subdirs(path):
    """Yield directory names not starting with '.' under given path."""
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_dir():
            yield entry.name


def get_expected():
    with open("expected") as f:
        return int(f.read())


def parse_time(s):
    match = re.search(r"(\d+\.\d+)", s.decode())
    try:
        num = match.group(1)
        return float(num)
    except IndexError:
        return math.inf


def to_number(s):
    try:
        return int(s)
    except ValueError:
        return math.nan


def print_table(times):
    rows = [time.fields() for time in times]
    header = ['Language', 'Time', 'Result']
    t = tabulate.tabulate(rows, headers=header, showindex=range(1, len(rows)+1))
    print(t)


@dataclass
class BenchResult:
    lang: str
    res: str = ''
    time: int = math.inf

    def fields(self):
        return [self.lang, self.time, self.res]


if __name__ == "__main__":
    code = main(sys.argv)
    sys.exit(code)
