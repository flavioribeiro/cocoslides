# -*- conding: utf-8 -*-
# cocoslides - a slides framework built in Cocos2d
from cocoslides.slides import CocoSlides

def test_run_slides_method_exists():
    assert hasattr(CocoSlides, 'run_slides')