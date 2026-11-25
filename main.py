import os
import shutil


def main():
    # The word itself is already settled in entry.txt; this program
    # only carries it over to wherever the harness wants it, so the
    # delivered text never changes between runs.
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
