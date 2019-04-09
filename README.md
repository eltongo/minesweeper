# Minesweeper

This is a CLI based minesweeper implementation I wrote in Python for fun. This is my first attempt really, so there
have been no optimizations whatsoever, but I imagine performance won't be an issue unless you're creating a really
large board.

## Running the game

The game has no dependencies, so you only need Python 3 installed on your machine. To run the game, simply type:
`python minesweeper.py`

By default there will be a 9x9 board with 10 bombs. There's a loop that runs until the game has finished, which will
print the board, and it accepts commands from the user.

The following characters are used to represent a board square:
* Unrevealed square: `?`
* Empty square: `_`
* Flagged square: `^`
* Bomb: `*`

Here's the default 9x9 board when the game starts:

```text
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
```

Here's the board mid game, with a flagged square:
```text
1 1 ? ? ? 1 _ 1 ?
^ ? ? ? ? 1 _ 1 ?
? ? ? 2 1 1 _ 1 1
? ? ? 1 _ _ _ _ _
? 2 1 1 _ _ _ _ _
? 1 _ _ _ _ _ _ _
? 1 1 _ _ _ _ _ _
? ? 3 1 1 _ _ 1 1
? ? ? ? 1 _ _ 1 ?
```

And here's the board after a game has finished (spoiler: I lost):

```text
1 1 _ 1 1 1 _ 1 1
* 2 1 1 * 1 _ 1 *
2 * 2 2 1 1 _ 1 1
2 3 * 1 _ _ _ _ _
* 2 1 1 _ _ _ _ _
1 1 _ _ _ _ _ _ _
1 1 1 _ _ _ _ _ _
2 * 3 1 1 _ _ 1 1
2 * 3 * 1 _ _ 1 *
```

## Commands

The game, as mentioned above, has a loop which reads a command from the user and then executes that command:

```text
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ?

Enter command: <enter command here>
```

Every command has the same format:
```text
<CMD> <row> <col>
```

`<CMD>` can be one of the following:
* `reveal`: reveal a square (ex. `reveal 0 3`)
* `flag`: flag a square (ex. `flag 5 1`)
* `unflag`: remove the flag from a previously flagged square (ex. `unflag 5 1`)

`<row>` and `<col>` are the zero-based coordinates to the square you are performing the action on.

The game also won't allow the user to reveal a flagged square as a protection measure. Neat, huh?

## What's next?

Our ambitions are high for Minesweeper. We are working hard for our MaaS cloud service (Minesweeper as a Service),
which will be a micro-services based cloud offering, for scalable Minesweeper (think 1e10 x 1e10 boards). You can email
us at cloud@sweeper.tldthatgooglemaysnatchuplater if you're interested.

I hope you didn't take this seriously. This is just a Minesweeper game. So there's a high chance there's nothing _next_.
I admit I'd like to add a GUI to the game, however, maybe using PyGame. Who knows.