# Dibs!

This script will generate some entries to import into dibs from
templates that are laid out in the script.  There are different
types of events that you specify with `--type`:

* practice:  This will create two entries for locker room monitors.
* home_game:  This will create locker room monitors, a penalty box,
  a scorekeeper, and a clock/scoreboard item.
* away_game:  This will create two locker room monitors and a penalty
  box item.
* home_tournament_game:  Creates a welcome table, scorekeeper,
  clock/scoreboard, two locker room monitors, and a penalty box
  for tournament games where we are playing.
* home_tournament_otherteams:  Creates a welcome table, scorekeeper,
  clock/scoreboard for tournament games where our team isn't
  playing.

You need to supply a start date/time in this format:
```
01/22/2026 03:30 pm
```
and a category needs to be specified too, like `18U` or `10U`.

If you want to specify that it's an all day event, like you
don't know when the event will be specifically (like for a possible
playoff game in a tournament), use `--allday TRUE` to make that happen.

You can also specify a `--prefix` so that you can prepend something
onto the name of every item.

## Output

By default, it will write out an `events.csv` file that you can import
into dibs.  If an `events.csv` exists, it will append the entries you
specified onto it.

You can specify a different filename by using `-o`.  So something like
`-o file.csv` will write it out to `file.csv`.

## Examples!

```
./dibs.py --type home_game --start "01/22/2027 06:25 PM" --category 18U
./dibs.py --type practice --start "01/23/2027 05:25 PM" --category 10U
./dibs.py --type away_game --start "01/24/2027 04:25 PM" --category 14U --prefix Testing
./dibs.py --type away_game --start "01/25/2027 03:25 PM" --category 14U --prefix Testing -o myfile.csv
./dibs.py --type away_game --start "01/25/2027 03:25 PM" --category 14U --prefix Testing --allday TRUE
```

