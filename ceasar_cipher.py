import sys

key =int(sys.argv[1])

def encrypt(msg):

    msg = msg.upper()
    nmsg = ""
    block = 0
    blocks = 0

    for i in range(len(msg)):
        
        char = msg[i]

        if ord(char) + key > 90:

            nchar = chr(ord(char) + key - 26)
        
        else:
            
            nchar = chr(ord(char) + key)

        if 65 <= ord(nchar) <= 90:
        
            if block ==  4:

                if blocks < 9:

                    nmsg = nmsg + nchar + " "
                    blocks += 1
            
                else:
                
                    nmsg = nmsg + nchar + "\n"
                    blocks = 0

                block = 0

            else:

                nmsg = nmsg + nchar
                block += 1

    return nmsg

for line in sys.stdin:
    print(encrypt(line))
