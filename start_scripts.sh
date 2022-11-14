#!/bin/bash
for file in ""./scripts/*""; do
    ./venv/bin/python $file &
done
