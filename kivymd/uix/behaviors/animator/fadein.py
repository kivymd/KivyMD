
from kivy.animation import Animation
from functools import partial

from base import Animator

__all__= ('FadeInAnimator', 'FadeInDownAnimator', 'FadeInLeftAnimator', 'FadeInRightAnimator', 'FadeInUpAnimator')

#fade in
class FadeInAnimator(Animator):
	def start_(self, tmp=None):
		props=["opacity",]
		vals=[0,]
		self._initialize(**dict(zip(props, vals)))
		
		vals=[1,]
		anim= Animation(
			d= self.duration,
			**dict(zip(props, vals)),
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class FadeInDownAnimator(Animator):
	def start_(self, tmp=None):
		props=["opacity","pos_hint"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_y", "y", "top"]:
				__tmp[key]= val+0.2
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

class FadeInLeftAnimator(Animator):
	def start_(self, tmp=None):
		props=["opacity","pos_hint"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.2
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

class FadeInRightAnimator(Animator):
	def start_(self, tmp=None):
		props=["opacity","pos_hint"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val+0.2
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

class FadeInUpAnimator(Animator):
	def start_(self, tmp=None):
		props=["opacity","pos_hint"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_y", "y", "top"]:
				__tmp[key]= val-0.2
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
