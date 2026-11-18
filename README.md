# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/febridewa/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/febridewa/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

**The world's news for Wednesday 18 November 2026, in one image** — a
front-page poster summing up the day: Trump in Manila for the first Quad in
two years, US and Iranian forces trading fire over Bahrain, Ukraine
collapsing a span of the Crimea bridge, Nvidia's 103% revenue jump, Cyclone
Akvan bearing down on India's east coast, and 25 more stories from six
continents, with a map of where it all happened. 30 stories in total, every
one checked against live reporting (AP, Reuters, Al Jazeera, BBC, CNN, IMD,
Kyodo News, CSK).

Referral code: `6etrfz79`

## The image

![Wednesday 18 November 2026 — the world's news in one picture](entry.png)

## How it was made

The poster was composed as a single 1024×1024 front page: three
photojournalistic panels (the Bahrain radar base under drone attack, the
collapsed Crimea bridge, the Manila summit) with two more stories told in
eight numbered cards, a numbered list of 19 further stories, a world map
with the 11 main stories pinned, and a by-the-numbers strip. All text on
the poster is drawn as crisp vector type — no AI-generated lettering, so
nothing is garbled or misspelled.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. No network access, and both runs write the same bytes.

## License

MIT — see [LICENSE](LICENSE).
