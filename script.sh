#!/bin/bash

echo "First argument: $1"
echo "Second argument: $2"

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 letter directory" >&2
  exit 1
fi

if [ ! -d "$2" ]; then
  echo "Error: '$2' is not a directory" >&2
  exit 1
fi

ls -d "$2/$1"* > /dev/null 2>&1 && printf "dir: %s\n" "$2/$1"*/ && printf "file: %s\n" "$2/$1"*


