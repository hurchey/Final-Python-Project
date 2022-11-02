#Eric Hurchey
#Programming Assignment #2
#2/8/2022
#

def main():
    top_and_bottom_line()
    top_half()
    bottom_half()
    top_and_bottom_line()
    
def top_and_bottom_line():
    print ("| " + "-" * 59 + " |")

def stars():
    print ("|  " + "*  " * 6 + "#" * 40 + " |")
    print ("|   " + "*  " * 5 + " " * 43 + "|")
    print ("|  " + "*  " * 6 + " " * 41 + "|")
    
def line_strip():
    print("| " + "#" * 59 + " |")
    
def top_half():
    stars()
    print ("|   " + "*  " * 5 + " " * 2 + "#" * 40 + " |")
    print ("|  " + "*  " * 6 + " " * 41 + "|")
    print ("|   " + "*  " * 5 + " " * 43 + "|")
    stars()

def bottom_half():
    for line in range (3):
        line_strip()
        print ("|" + " " * 61 + "|")
        print ("|" + " " * 61 + "|")
    line_strip()
    
main()
