# cocoslides - a slides framework built in Cocos2d
# by Flávio Ribeiro (email@flavioribeiro.com)

from cocos.sprite import *
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.actions import *
from cocos.sprite import *
from cocos.menu import *
from cocos.text import *
from pyglet import font

from pyglet.window import key

import config

class Presentation(Scene):

    def __init__(self, background = None):

        super(Presentation, self).__init__()

        self.background = pyglet.resource.image(config.MEDIA_PATH +\
                                                    background)

    def draw(self):
        glPushMatrix()
        self.transform()
        self.background.blit(0,0)
        glPopMatrix()
