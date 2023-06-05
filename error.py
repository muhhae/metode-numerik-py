from math import *
from rich import *
from rich.console import Console
from rich.table import Table

def error(f, x, y):
    table = Table(title=" Error ")
    
    table.add_column("Error", style="cyan", no_wrap=True, justify = "left")
    table.add_column("Error %", style="magenta", no_wrap=True, justify = "left")
    
    er = []
    print("\n")
    for (a,b) in zip(x, y):
        er.append(abs(f(a)-b))

    # for (a,b) in zip(er, y):
    #     print("error = ", a, "= ", a/abs(b) * 100, "%")
        
    yRata = sum(abs(a) for a in y) / len(y)
    erRata = sum(er) / len(er)
    
    for a in er:
        table.add_row(str(a), str(a/abs(b) * 100) + " %")

    print(table)
    print("\nError rata : ", erRata, "= ", erRata / yRata * 100, "%")