"""
MIT License

Copyright (c) 2019 Shashi Ranjan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from kivy.clock import Clock
from kivy.graphics import PushMatrix, PopMatrix, Color, Rectangle, Rotate
from functools import partial
import time

class Animator():
	"""
	Animator
	========
	Base Class for Animators

	Parameters
	----------
	widget: widget to be animated

	duration: [optional], defaults to 1

	repeat: [optional], defaults to True
	
	Attributes
	----------
	anim_complete:
		Called internally upon completition of an animation

	_initialize:
		Used to set properties of the 'widget' prior to animation

	"""

	def __init__(self, widget, duration=1, repeat=True):
		self.widget= widget
		self.duration= duration
		self._repeat= repeat
		self._original= {}
		self.attr=['opacity','height','width','pos_hint','angle']

		"""
		setattr(self.widget, "origin_", None)
		setattr(self.widget, "angle", 0)
		setattr(self.widget, "axis", tuple((0,0,1)))
		
		with widget.canvas.before:
			PushMatrix()
			dsh= {
				"axis":getattr(self.widget, "axis"),
				"angle": getattr(self.widget, "angle"),
				"origin": getattr(self.widget, "origin_") or getattr(self.widget, "center")
			}
			print(dsh)
			Rotate(
			**dsh
			)
			PopMatrix()
		#with widget.canvas.after:
		#	PopMatrix()
		"""

		for key in self.attr:
			self._original[key]= getattr(self.widget, key)

	@classmethod
	def anim_complete(cls, obj, inst, widget):
		if obj._repeat:
			for key, val in obj._original.items():
				setattr(widget, key, val)

			inst.unbind(on_complete= obj.anim_complete)
			time.sleep(0.3)		#just to make repeatition visually clear
			Clock.schedule_once(partial(obj.start_, ), 0)

		else:
			inst.stop(widget)

	def _initialize(self, **kwargs):
		for key, val in kwargs.items():
			setattr(self.widget, key, val)
