# PySheet

## Description

Pysheet is a program that i wrote so that i can write down all the things i learn and use it as a cheat sheet while program.

## Installation

Copy the pysheet source code by using the following command or by downloading the [.zip](https://github.com/Byson94/py-sheet/archive/refs/heads/main.zip)

```bash
git clone https://github.com/Byson94/py-sheet.git
```

After cloning the project, run the `setup.sh` file in the py-sheet folder.

```bash
./setup.sh
```

These 2 steps will get `pysheet` installed on your system.

## Commands

> [!IMPORTANT]
> If no argument is provided, then pysheet will list all the cheatsheets

### `--version` or `-v`

Displays the current version of the tool.

**Example:**

```bash
pysheet --version
```

### `--manual <cheatsheet-name>` or `-m`

Displays a specific cheatsheet by the name.

**Example:**

```bash
pysheet --manual loops
```

## Dependencies

- rich

> [!IMPORTANT]
> Make sure that you have rich installed on your system for pysheet to work.
