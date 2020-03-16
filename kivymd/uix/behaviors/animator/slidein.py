
from kivy.animation import Animation
from functools import partial

from base import Animator

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
