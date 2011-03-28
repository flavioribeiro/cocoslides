# cocoslides - a slides framework built in Cocos2d
import sys

from slides import CocoSlides

def main(args):
	if len(args) > 1:
		content_slides = file(args[1:])
		if content_slides.exists():
			CocoSlides.run_slides(content_slides.read())
		else:
			print '[cocoslides] file does not exists.'
		
if __name__ == "__main__":
	main(sys.argv)