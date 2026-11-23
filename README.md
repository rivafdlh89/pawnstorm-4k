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
fixed node budget, so play is fully deterministic. The source is shipped as a
zlib+base85 payload with a small unpacker so the whole engine fits in 4,096
bytes as committed.

## Run

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

The engine talks to the make.fun chess environment: it starts games with
`POST /game`, answers with `POST /move`, and plays until the gauntlet ends.

<sub>Entered on [make.fun](https://make.fun/?ref=rivafdlh89&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
