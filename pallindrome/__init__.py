import check50
import check50.c

@check50.check()
def exists():
    """pallindrome.c exists"""
    check50.exists("pallin.c")

@check50.check(exists)
def compiles():
    """pallindrome.c compiles"""
    check50.c.compiles("pallindrome.c", lsc50=True)

@check50.check(compiles)
def test1():
    """Identifies 11111 as a pallindrome"""
    check50.run("./pallindrome").stdin("11111").stdout("11111 is a pallindrome").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test2():
    """Identifies 12321 as a pallindrome"""
    check50.run("./pallindrome").stdin("12321").stdout("12321 is a pallindrome").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test3():
    """101010 is not a pallindrome"""
    check50.run("./pallindrome").sdtin("101010").stdout("101010 is not a pallindrome").stdout(check50.EOF).exit(0)

@check50.check(compiles)
    """120012 is not a pallindrome"""
    check50.run("./pallindrome").stdin("120012").stdout("1200012 is not a pallindrome").stdout(check50.EOF).exit(0)
