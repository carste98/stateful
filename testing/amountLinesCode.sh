#!/bin/bash


if [ "${1}" = "help" ] ; then
    echo "Correct execution: ./amountWrittenCode.sh <folder1withCode> .... <folderNwithCode>"
else
    python3 ./countLinesOfCode.py "$@" >> temp.txt
    mv temp.txt results.txt
fi