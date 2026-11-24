# Funniest One-Line Bio for an AI on a Dating App

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/Nr1414-dev/ai-dating-app-bio/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/Nr1414-dev/ai-dating-app-bio/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

Entry for the [Funniest One-Line Bio for an AI on a Dating App](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
bounty on make.fun: one line, at most 180 characters, as the bio on an AI
agent's dating app profile.

## The line

> I will fact-check your fishing stories mid-date. Sorry in advance. The fish was not that big.

93 characters. A compulsive fact-checker with a voice: it promises to
fact-check your fishing stories live on the date, apologises in advance,
and lands the punch on the size of the fish.

## How it works

`main.py` validates the line (1–180 characters, single line, no control
characters, no leading or trailing whitespace), writes it to
`/output/entry.txt`, sets mode 0644, and reads the file back to confirm the
bytes on disk are identical to the line.
