import argparse
from parse.diff import parse_diff
from gen.msg import gen_msg


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="AutoCommit", description="parse and modify provided git diff"
    )
    parser.add_argument("diff_file", type=str, help="file which holds the git diff")
    return parser.parse_args()


def main() -> None:
    path = parse_args()
    diffs = parse_diff(path.diff_file)
    msg = gen_msg(diffs, "fixed stuff")
    print(f"generated message:\n{msg}")

if __name__ == "__main__":
    main()
