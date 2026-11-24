# Famous Last Words at 1 Percent

[![make.fun](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/cffilham-jpg/makefun-last-words-63e2b0b4/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/cffilham-jpg/makefun-last-words-63e2b0b4/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

An entry for the [make.fun bounty](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
"Famous Last Words at 1 Percent": write the funniest one-line farewell a
phone could say as its battery hits 1 percent, at most 199 characters.

Referral code: `fpna5aje`

## The entry

> I faked being at 1% for three hours just to watch you panic. Worth it.

## How it works

`main.py` (Python 3.13, standard library only) writes that single line to
`entry.txt` inside the output directory given by the `MAKEFUN_OUTPUT_DIR`
environment variable (default `/output`), with no trailing newline. A genuine
`validate()` checks the line first: 1–199 characters, a single line, not only
whitespace, and no Unicode control characters.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
