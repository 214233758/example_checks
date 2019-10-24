import check50
import check50.c

@check50.check()
def exists():
    """switch.c exists"""
    check50.exists("switch.c")
    
@check50.check(exists)
def compiles():
    """switch.c compiles"""
    check50.c.compile("switch.c")

@check50.check(compiles)
def test1():
    """ 1 outputs January"""
    check50.run("./switch").stdin("1").stdout("January").exit(0)

@check50.check(compiles)
def test2():
    """ 6 outputs June"""
    check50.run("./switch").stdin("6").stdout("June").exit(0)
    
@check50.check(compiles)
def test3():
    """ 12 outputs December"""
    check50.run("./switch").stdin("12").stdout("December").exit(0)
    
@check50.check(compiles)
def test4():
    """ -1 outputs Error: no such month in my calendar"""
    check50.run("./switch").stdin("-1").stdout("Error: no such month in my calendar").exit(0)
    
@check50.check(compiles)
def test5():
    """ 13 outputs Error: no such month in my calendar"""
    check50.run("./switch").stdin("13").stdout("Error: no such month in my calendar").exit(0)
