#!/bin/sh

exec dotnet run --no-build -p "$(dirname "$0")" -c Release
