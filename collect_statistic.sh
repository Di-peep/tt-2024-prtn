#!/bin/bash


if [ $# -eq 0 ]; then
  echo "Use the command in this way: $0 <filename>"
  exit 1
fi

filename=$1
DIR="$( dirname "${BASH_SOURCE[0]}" )"

python3 "$DIR/statistic.py" "$filename"
