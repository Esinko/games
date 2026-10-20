#!/usr/bin/env python3
"""Solver for <challenge name>. See "Solver script" in the guidelines (README.md in the repository root).

Usage (keep the one that fits your challenge, delete the other):
  hosted:     python3 solve.py HOST PORT [PORT ...]   ports in the order of your "Open ports" list
  file-based: python3 solve.py FILES_DIR              the directory with exactly the files players get

Prints every flag it finds on stdout, one per line, everything else on stderr.
Exit code 0 only when all flags were found.
"""
import argparse
import signal
import sys

FLAG_COUNT = 1  # how many flags this challenge has
TIMEOUT = 300  # seconds; the whole run should take about 5 minutes at most


def log(*args):
    """Progress and debug output: stderr, so stdout holds nothing but flags."""
    print(*args, file=sys.stderr, flush=True)


def solve_hosted(host, ports):
    """Solve against the running challenge and return the flags found, in order.
    Be nice to the live challenge: random names for anything you create, no shared password changes, clean up."""
    flags = []
    # Example:
    # import urllib.request
    # page = urllib.request.urlopen(f"http://{host}:{ports[0]}/", timeout=10).read().decode()
    # flags += re.findall(r"DISOBEY\[[^\]]+\]", page)
    return flags


def solve_files(files_dir):
    """Solve from the player files only (no source code, generator or secrets) and return the flags found."""
    flags = []
    # Example:
    # data = (Path(files_dir) / "capture.pcap").read_bytes()
    return flags


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", nargs="+", help="HOST PORT [PORT ...] or FILES_DIR")
    a = ap.parse_args()
    signal.signal(signal.SIGALRM, lambda *_: sys.exit("timeout"))  # Unix only; drop it if you need Windows
    signal.alarm(TIMEOUT)

    if len(a.target) == 1:
        flags = solve_files(a.target[0])
    else:
        host, ports = a.target[0], [int(p) for p in a.target[1:]]
        flags = solve_hosted(host, ports)

    for f in flags:
        print(f, flush=True)
    if len(flags) < FLAG_COUNT:
        log(f"found {len(flags)} of {FLAG_COUNT} flag(s)")
        sys.exit(1)


if __name__ == "__main__":
    main()
