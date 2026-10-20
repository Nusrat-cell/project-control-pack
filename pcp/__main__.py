import sys
import tempfile

from . import report


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "demo"
    out = sys.argv[2] if len(sys.argv) > 2 else tempfile.mkdtemp()
    if cmd != "demo":
        print("usage: python -m pcp demo [outdir]")
        return
    b = report.write(out)
    print(report.markdown(b))
    print(f"written: {out}/status_report.md and {out}/control_pack.xlsx")


main()
