import argparse
from parse.diff import parse_diff
from gen.msg import gen_msg


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="AutoCommit", description="parse and modify provided git diff"
    )
    parser.add_argument("diff_file", type=str, help="file which holds the git diff")
    parser.add_argument("original_message", type=str, help="original commit message")
    parser.add_argument("--verbosity", "-v", type=int, default=0, help="verbosity")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    diffs = parse_diff(args.diff_file, args.verbosity)
    msg = gen_msg(diffs, args.original_message, args.verbosity)
    if args.verbosity > 0:
        print("generated message:")
    print(f"{msg}")

if __name__ == "__main__":
    main()
