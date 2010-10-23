# cocoslides - a slides framework built in Cocos2d
# by Flávio Ribeiro (email@flavioribeiro.com)

import os

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

class Background(Scene):

    def __init__(self, bg_img = None):

        super(Presentation, self).__init__()

        self.background = pyglet.resource.image(os.path.join(
                                    config.MEDIA_PATH, background))

    def draw(self):
        glPushMatrix()
        self.transform()
        self.background.blit(0,0)
        glPopMatrix()

class Slide(Layer):

    is_event_handler = True

    def on_key_press(self, _key, modifiers):
        if _key == key.LEFT:
            SlidesManager.previous()
        elif _key == key.RIGHT:
            SlidesManager.next()


class SlidesManager(object):

    def previous(self):
        pass

    def next(self):
        pass

