import check50
import check50.c

@check50.check()
def exists():
    """pallindrome.c exists"""
    check50.exists("pallindrome.cpp")

@check50.check(exists)
def compiles():
    """pallindrome.cpp compiles"""
    check50.c.compile("pallindrome.cpp", lcs50=True)

@check50.check(compiles)
def test1():
    """Identifies 11111 as a pallindrome"""
    check50.run("./pallindrome").stdin("11111").stdout("11111 is a palindrome").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test2():
    """Identifies 12321 as a pallindrome"""
    check50.run("./pallindrome").stdin("12321").stdout("12321 is a palindrome").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test3():
    """101010 is not a pallindrome"""
    check50.run("./pallindrome").stdin("101010").stdout("101010 is not a palindrome").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test4():
    """120012 is not a pallindrome"""
    check50.run("./pallindrome").stdin("120012").stdout("120012 is not a palindrome").stdout(check50.EOF).exit(0)
