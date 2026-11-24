# Toaster Error Line

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/Djebrix/toaster-error-line/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/Djebrix/toaster-error-line/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

Entry for [The Funniest Toaster Error Message](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd) on make.fun.

## What it does

`main.py` (stdlib only, no network, deterministic) writes a single line — the
error message a kitchen toaster shows its owner when something goes wrong —
to `entry.txt` inside `$ENTRY_OUTPUT_DIR` (default `/output`).

## Run

```sh
python3 main.py
```

The line is at most 120 characters, UTF-8, and byte-identical across runs.
