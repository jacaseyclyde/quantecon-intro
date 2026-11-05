# QuantEcon study repo

Personal study copy of *A First Course in Quantitative Economics with Python*
by Thomas J. Sargent and John Stachurski (https://intro.quantecon.org).
Course content belongs to QuantEcon and is licensed CC BY-SA 4.0
(https://creativecommons.org/licenses/by-sa/4.0/). This repo is a fork of
https://github.com/QuantEcon/lecture-python-intro.notebooks.

## Branches

- `main` is an untouched mirror of upstream. Never commit to it.
- `study` is the default branch, and all work goes here. Edit the notebooks in
  place, run the cells, and do the exercises.
- See what you changed in a notebook with
  `git diff main..study -- monte_carlo.ipynb`.

## Syncing with upstream

Upstream regenerates these notebooks whenever a lecture changes, so syncing is
optional. A finished lecture needs no update. To pull in changes:

```
gh repo sync OWNER/REPO --branch main    # updates main on GitHub
git fetch origin
git switch study && git merge origin/main
```

Expect merge conflicts only in notebooks you have edited. Keep your version
for lectures you have finished, or take upstream's if the change matters.

## Environment

Create the environment from `environment.yml` and start Jupyter from the repo
root so the notebooks resolve their relative paths.

## Progress

Progress is tracked in this repo's issues (QE 01 to QE 13, one per study day)
and in the "QuantEcon intro course" GitHub project, which has Effort, Start
date, and End date fields. Earlier rough reproductions live in `archive/`.
