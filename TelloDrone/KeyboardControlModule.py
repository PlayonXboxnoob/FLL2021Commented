import pygame # Library for games

def init():
    pygame.init() # initializing
    win = pygame.display.set_mode((480, 480)) #

def close(): # stop the code
    pygame.display.quit()

def getKey(keyName): # function for detecting keypresses KeyName is the key it is looking for
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True

    pygame.display.update()
    return ans

if __name__ == '__main__':
    init()
    while True:
        if getKey('LEFT'):
            print('Left key pressed')
            close()
            break


