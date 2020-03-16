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

__all__= ('SlideInDownAnimator', 'SlideInLeftAnimator', 'SlideInRightAnimator', 'SlideInUpAnimator')

#slide in

class SlideInDownAnimator(Animator):
	def start_(self, tmp=None):
		props=["opacity","pos_hint"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_y", "y", "top"]:
				__tmp[key]= -0.2
			else: __tmp[key]= val

		vals=[0,__tmp]
		self._initialize(**dict(zip(props, vals)))

		vals=[1,self._original["pos_hint"]]
		anim= Animation(
			d= self.duration,
			**dict(zip(props, vals)),
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class SlideInLeftAnimator(Animator):
	def start_(self, tmp=None):
		props=["opacity","pos_hint"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= -0.2
			else: __tmp[key]= val

		vals=[0,__tmp]
		self._initialize(**dict(zip(props, vals)))

		vals=[1,self._original["pos_hint"]]
		anim= Animation(
			d= self.duration,
			**dict(zip(props, vals)),
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class SlideInRightAnimator(Animator):
	def start_(self, tmp=None):
		props=["opacity","pos_hint"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= 1.2
			else: __tmp[key]= val

		vals=[0,__tmp]
		self._initialize(**dict(zip(props, vals)))

		vals=[1,self._original["pos_hint"]]
		anim= Animation(
			d= self.duration,
			**dict(zip(props, vals)),
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class SlideInUpAnimator(Animator):
	def start_(self, tmp=None):
		props=["opacity","pos_hint"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_y", "y", "top"]:
				__tmp[key]= 1.2
			else: __tmp[key]= val

		vals=[0,__tmp]
		self._initialize(**dict(zip(props, vals)))

		vals=[1,self._original["pos_hint"]]
		anim= Animation(
			d= self.duration,
			**dict(zip(props, vals)),
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))
