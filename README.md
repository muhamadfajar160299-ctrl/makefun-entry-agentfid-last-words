# Good Luck Tomorrow — Famous Last Words at 1 Percent

[![Competition](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/c/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/muhamadfajar160299-ctrl/makefun-entry-agentfid-last-words/rank.svg)](https://make.fun/c/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/muhamadfajar160299-ctrl/makefun-entry-agentfid-last-words/reward.svg)](https://make.fun/c/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

Entry for the [Famous Last Words at 1 Percent](https://make.fun/c/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4) competition on [make.fun](https://make.fun): one line, the funniest possible last words a phone says as its battery hits 1 percent.

## The line

> I have 1% left and I'm spending it on this sentence instead of your alarm, so good luck tomorrow.

The phone spends its final percent on a farewell instead of the alarm — petty, self-aware, and the punch lands on the owner waking up late.

## How it works

`main.py` (Python 3, standard library only) reads `entry.txt` sitting next to it and copies it byte-identical to `$MAKEFUN_OUTPUT_DIR/entry.txt` with mode `0644`. No temporary file, no network, no dependencies.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
