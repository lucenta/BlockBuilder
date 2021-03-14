import sys
from Window import *


## @brief Run BlockBuilder
def main():
    n = len(sys.argv)
    if n == 1:
        print(err_msg())
        return
    
    # Check command line args and start a game accordingly
    game = sys.argv[1]
    if game == '-s': # Single player game
        print("Starting single player game...")
        window = Window(width=1300, height=700, caption='BlockBuilder', resizable=True) 
    elif game == "-m": # Join a server
        if n != 4:
            print("Please specify port ip and port number")
            return 
        print("Starting multiplayer game...")
        ip = sys.argv[2]
        port = int(sys.argv[3])

        # If a multiplayer game was started, connect to server
        print("Connecting to Server...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
           s.connect((ip,port))
        except ConnectionRefusedError:
            print("No server found... exiting")
            return
        print("Connected to server! Starting game")
        window = Window(server =s, width=1300, height=700, caption='BlockBuilder', resizable=True) # Create Window
    else:
        print(err_msg())
        return
    # window = Window(width=1300, height=700, caption='BlockBuilder', resizable=True) #Create Window
    window.set_exclusive_mouse(True)                    # Hide the mouse cursor

    

    pyglet.app.run()                                    # Start PyGlet app

def err_msg():
    return("Invalid Usage...\n"+
            "\tSingle Player:\tmain.py -s\n"+
            "\tJoin Server:\tmain.py -m <ip> <port>")

def connectToServer():
    try:
        self.s.connect(server)
    except ConnectionRefusedError:
        print("No server found... exiting")
        return


if __name__ == '__main__':
    main()
