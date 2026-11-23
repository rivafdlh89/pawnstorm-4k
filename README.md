# pawnstorm-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rivafdlh89/pawnstorm-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rivafdlh89/pawnstorm-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A tiny, original chess engine in under 4 KB of Python, built for make.fun's
"Build the strongest chess engine in 4 KB of Python" bounty.

`main.py` is a self-contained engine (Python 3.13 stdlib only, no files, no
network, no model calls): a 120-square mailbox board, FEN parsing, legal move
generation (castling, en passant, promotions), alpha-beta search with
quiescence, transposition table, killer moves, MVV-LVA ordering, null-move
pruning, and a material + piece-square-table evaluation. It searches to a
fixed node budget, so play is fully deterministic. `main.py` is packed with
the kit's own `makefun compress` (LZMA stub, 3,024 bytes) from the readable
source `engine.py` (7,098 bytes, kept in the repository folder), so the whole
engine fits in 4,096 bytes as committed.

## Practice results

Practice trials run locally with the kit's environment server and scorer
(6 games: depth-2/3/4, nodes-100k/250k/500k anchors):

- Trial 0: **Elo 1,191** (2W / 1D / 3L) — confirmed twice, and again with the
  packed `main.py`
- Trial 1: Elo 997 (0W / 3D / 3L)
- Trial 2: Elo 1,099 (2W / 0D / 4L)
- Mean of 3 trials: **1,096** — below the 1,154 practice floor and the
  ~1,365 house baseline, so this is a legitimate working entry, not a
  prize favourite.

## Run

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

The engine talks to the make.fun chess environment: it starts games with
`POST /game`, answers with `POST /move`, and plays until the gauntlet ends.

<sub>Entered on [make.fun](https://make.fun/?ref=rivafdlh89&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
