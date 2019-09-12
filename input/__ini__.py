import check50
import check50.c

@check50.check()
def exists():
    """input.c exists."""
    check50.exists("input.c")

@check50.check(exists)
def compiles():
    """input.c compiles."""
    check50.c.compile("input.c", lcs50=True)

@check50.check(compiles)
def test1():
    """give out 5 when 5 is the input"""
    check50.run("./input").stdin("5").stdout("Number = 5\n").stdout(check50.EOF).exit(0)
