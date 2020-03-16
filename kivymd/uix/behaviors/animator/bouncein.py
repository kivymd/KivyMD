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
from kivy.animation import Animation
from functools import partial

from .base import Animator

__all__= ('BounceInAnimator', 'BounceInDownAnimator', 'BounceInLeftAnimator', 'BounceInRightAnimator', 'BounceInUpAnimator')

#Bounce in
class BounceInAnimator(Animator):
	def start_(self, tmp=None):
		props=["height", "width", "opacity"]

		vals=[self._original["height"]*0.3,self._original["width"]*0.3,0]
		self._initialize(**dict(zip(props,vals)))

		vals=[self._original["height"]*1.05,self._original["width"]*1.05,1]
		anim= Animation(
			d= self.duration/3,
			**dict(zip(props,vals)),
			)

		vals=[self._original["height"]*0.9,self._original["width"]*0.9,1]
		anim+= Animation(
			d= self.duration/3,
			**dict(zip(props,vals)),
			)

		anim+= Animation(
			d= self.duration/3,
			**self._original,
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class BounceInDownAnimator(Animator):
	def start_(self, tmp=None):
		props=["pos_hint","opacity"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_y", "y", "top"]:
				__tmp[key]= val+0.2
			else: __tmp[key]= val
		vals=[__tmp, 0]
		self._initialize(**dict(zip(props,vals)))
		
		__tmp={}
		for _key, _val in self._original["pos_hint"].items():
			if _key in ["center_y", "y", "top"]:
				__tmp[_key]= _val-0.04
			else: __tmp[_key]= _val

		vals=[__tmp, 1]
		anim= Animation(
			d= self.duration/3,
			**dict(zip(props,vals)),
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_y", "y", "top"]:
				__tmp[key]= val+0.02
			else: __tmp[key]= val
		vals=[__tmp, 1]

		anim+= Animation(
			d= self.duration/3,
			**dict(zip(props,vals)),
			)

		anim+= Animation(
			d= self.duration/3,
			**self._original,
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class BounceInLeftAnimator(Animator):
	def start_(self, tmp=None):
		props=["pos_hint","opacity"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.2
			else: __tmp[key]= val
		vals=[__tmp, 0]
		self._initialize(**dict(zip(props,vals)))

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val+0.04
			else: __tmp[key]= val
		vals=[__tmp, 1]

		anim= Animation(
			d= self.duration/3,
			**dict(zip(props,vals)),
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.02
			else: __tmp[key]= val
		vals=[__tmp, 1]

		anim+= Animation(
			d= self.duration/3,
			**dict(zip(props,vals)),
			)

		anim+= Animation(
			d= self.duration/3,
			**self._original,
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class BounceInRightAnimator(Animator):
	def start_(self, tmp=None):
		props=["pos_hint","opacity"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val+0.2
			else: __tmp[key]= val
		vals=[__tmp, 0]
		self._initialize(**dict(zip(props,vals)))

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.04
			else: __tmp[key]= val
		vals=[__tmp, 1]

		anim= Animation(
			d= self.duration/3,
			**dict(zip(props,vals)),
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val+0.02
			else: __tmp[key]= val
		vals=[__tmp, 1]
		anim+= Animation(
			d= self.duration/3,
			**dict(zip(props,vals)),
			)

		anim+= Animation(
			d= self.duration/3,
			**self._original,
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class BounceInUpAnimator(Animator):
	def start_(self, tmp=None):
		props=["pos_hint","opacity"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_y", "y", "top"]:
				__tmp[key]= val-0.2
			else: __tmp[key]= val
		vals=[__tmp, 0]
		self._initialize(**dict(zip(props,vals)))

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_y", "y", "top"]:
				__tmp[key]= val+0.04
			else: __tmp[key]= val
		vals=[__tmp, 1]

		anim= Animation(
			d= self.duration/3,
			**dict(zip(props,vals)),
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_y", "y", "top"]:
				__tmp[key]= val-0.02
			else: __tmp[key]= val
		vals=[__tmp, 1]
		anim+= Animation(
			d= self.duration/3,
			**dict(zip(props,vals)),
			)

		anim+= Animation(
			d= self.duration/3,
			**self._original,
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))
# Bounce in------------------
