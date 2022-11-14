#!/bin/bash
source venv/bin/activate
for file in ""./scripts/*""; do
    python $file &
done