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

__all__ =('FlyOutAnimator','FlyInAnimator', 'DropOutAnimator', 'HingLeftAnimator', 'HingRightAnimator', 'RollInAnimator', 'RollOutAnimator')

class FlyOutAnimator(Animator):
	def start_(self, tmp=None):
		self._initialize(opacity=1)
		props=["height", "width", "opacity"]

		vals=[self._original["height"]*2,self._original["width"]*2,0]
		anim= Animation(
			d= self.duration,
			**dict(zip(props,vals))
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class FlyInAnimator(Animator):
	def start_(self, tmp=None):
		props=["height","width","opacity"]
		vals=[self._original["height"]*2,self._original["width"]*2,0]
		self._initialize(**dict(zip(props,vals)))

		vals=[self._original["height"],self._original["width"],1]
		anim= Animation(
			d= self.duration,
			**dict(zip(props,vals)),
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class DropOutAnimator(Animator):
	def start_(self, tmp=None):
		props=["pos_hint","opacity"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_y", "y", "top"]:
				__tmp[key]= 1.2
			else: __tmp[key]= val
		vals=[__tmp, 0]
		self._initialize(**dict(zip(props,vals)))

		anim= Animation(
			t= 'out_bounce',
			d= self.duration,
			**self._original,
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class HingLeftAnimator(Animator):
	def start_(self, tmp=None):
		pivot= (self.widget.x,self.widget.y+self.widget.height)
		self.widget.origin_= pivot

		props=["angle","pos_hint"]
		
		vals=[-85, self._original["pos_hint"]]
		anim= Animation(
			t= 'out_bounce',
			d= self.duration,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= 1.2
			else: __tmp[key]= val
		vals=[-85,__tmp]
		anim+= Animation(
			t= 'out_sine',
			d= self.duration,
			**dict(zip(props,vals))
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class HingRightAnimator(Animator):
	def start_(self, tmp=None):
		pivot= (self.widget.x+self.widget.width,self.widget.y+self.widget.height)
		self.widget.origin_= pivot

		props=["angle","pos_hint"]
		
		vals=[85, self._original["pos_hint"]]
		anim= Animation(
			t= 'out_bounce',
			d= self.duration,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= -0.2
			else: __tmp[key]= val
		vals=[85,__tmp]
		anim+= Animation(
			t= 'out_sine',
			d= self.duration,
			**dict(zip(props,vals))
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class RollInAnimator(Animator):
	def start_(self, tmp=None):
		props=["angle","opacity","pos_hint"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= -0.2
			else: __tmp[key]= val

		vals=[90,0,__tmp]
		self._initialize(**dict(zip(props,vals)))

		vals=[self._original["angle"],1,self._original["pos_hint"]]
		anim= Animation(
			d= self.duration,
			**dict(zip(props,vals)),
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class RollOutAnimator(Animator):
	def start_(self, tmp=None):
		props=["angle","opacity","pos_hint"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= 1.2
			else: __tmp[key]= val
		vals=[-90,0,__tmp]
		anim= Animation(
			d= self.duration,
			**dict(zip(props,vals)),
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))
