import check50
import check.c

@check50.check()
def exists():
    """question3.c exists"""
    check50.exists("question3.c")
    
@check50.check(exists)
def compiles()
    """question3.c compiles"""
    check50.c.compiles(question3.c)
    
@check50.check(compiles)
def test()
    """expected output"""
    check50.run("./question3").stdou("First condition is true\nSecond condition is false\nThird condition is true", , regex=True).exit(0)
