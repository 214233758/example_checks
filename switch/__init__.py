import check50
import check50.c

@check50.check()
def exists():
    """month.c exists"""
    check50.exists("month.c")
    
@check50.check(exists)
def compiles():
    """prompt.c compiles"""
    check50.c.compile("month.c")

@check50.check(compiles)
def test1():
    """ 1 outputs January"""
    check50.run("./month").stdin("1", prompt = False).stdout("January").exit(0)

@check50.check(compiles)
def test2():
    """ 6 outputs June"""
    check50.run("./month").stdin("6", prompt = False).stdout("June").exit(0)
    
@check50.check(compiles)
def test3():
    """ 12 outputs December"""
    check50.run("./month").stdin("12", prompt = False).stdout("December").exit(0)
    
@check50.check(compiles)
def test4():
    """ -1 outputs Error: no such month in my calendar"""
    check50.run("./month").stdin("-1", prompt = False).stdout("Error: no such month in my calend[ae]r").exit(0)
    
@check50.check(compiles)
def test5():
    """ 13 outputs Error: no such month in my calendar"""
    check50.run("./month").stdin("13", prompt = False).stdout("Error: no such month in my calend[ae]r").exit(0)
