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
        print("start single player game")
    elif game == "-m": # Join a server
        if n != 4:
            print("Please specify port ip and port number")
            return 
        print("start multiplayer game")
    elif game == "-c": # Create a server
        if n != 3:
            print("Please specify port num")
            return
        print("Start server")
    else:
        print(err_msg())
        return
    # window = Window(width=1300, height=700, caption='BlockBuilder', resizable=True) #Create Window
    # window.set_exclusive_mouse(True)                    # Hide the mouse cursor

    # glClearColor(0.5, 0.7, 1.0, 1)                      # Set the sky color

    # glEnable(GL_DEPTH_TEST)                             # Basic OpenGL setup
    # glEnable(GL_CULL_FACE)
    # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    # glEnable(GL_FOG)                                    # Create fog
    # glFogfv(GL_FOG_COLOR, (GLfloat * 4)(0.5, 0.69, 1.0, 1))
    # glHint(GL_FOG_HINT, GL_DONT_CARE)
    # glFogi(GL_FOG_MODE, GL_LINEAR)
    # glFogf(GL_FOG_START, 20.0)
    # glFogf(GL_FOG_END, 60.0)

    # pyglet.app.run()                                    # Start PyGlet app

def err_msg():
    return("Invalid Usage...\n"+
            "\tSingle Player:\tmain.py -s\n"+
            "\tJoin Server:\tmain.py -m <ip> <port>\n"+
            "\tCreate Server:\tmain.py -c <port>")

if __name__ == '__main__':
    main()
