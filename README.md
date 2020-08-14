# fac-bench

Factorial benchmark in different languages. Showcase expressivity and speed, in
development as well as execution.

## Specification

Calculate the first 3000 factorials, sum them and print the number out. To make the
tests pass you must not print a newline. Currently all languagues run sequentially but
most of the use libraries for bignums and/or factorial calculation.

## Structure

There is a subfolder per language. Each folder has to contain a file named `build` that
ensures an executable named `fac` is ready. For compiled languages `build` usually triggers
the compilation. Scripting languages only create a link to the script.

## CI

On push all benchmarks are executed and results checked. The output is sorted by execution
time. Under [Actions](https://github.com/robindaumann/fac-bench/actions?query=workflow%3A%22Benchmark+CI%22)
you can start the workflow with a single language as parameter.
