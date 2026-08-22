"""Minimal example for TimeLogger."""

from timelogger import timelogger


def main():
 runner = timelogger({"name": "TimeLogger", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()