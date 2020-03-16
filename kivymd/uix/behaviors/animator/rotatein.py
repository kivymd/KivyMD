
from kivy.animation import Animation
from functools import partial

from base import Animator

__all__= ('RotateInAnimator', 'RotateInDownLeftAnimator', 'RotateInDownRightAnimator', 'RotateInUpLeftAnimator', 'RotateInUpRightAnimator')

#rotate in
class RotateInAnimator(Animator):
	def start_(self, tmp=None):
		props=["angle","opacity"]

		vals=[200,0]
		self._initialize(**dict(zip(props,vals)))

		vals=[0,1]
		anim= Animation(
			d= self.duration,
			**dict(zip(props,vals))
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class RotateInDownLeftAnimator(Animator):
	def start_(self, tmp=None):
		pivot= (self.widget.x-self.widget.width/2,self.widget.y)
		self.widget.origin_= pivot

		props=["angle","opacity"]
		vals=[90,0]
		self._initialize(**dict(zip(props,vals)))

		vals=[0,1]
		anim= Animation(
			d= self.duration,
			**dict(zip(props,vals))
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class RotateInDownRightAnimator(Animator):
	def start_(self, tmp=None):
		pivot= (self.widget.x+3*self.widget.width/2,self.widget.y)
		self.widget.origin_= pivot

		props=["angle","opacity"]
		vals=[-90,0]
		self._initialize(**dict(zip(props,vals)))

		vals=[0,1]
		anim= Animation(
			d= self.duration,
			**dict(zip(props,vals))
			)
		
		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class RotateInUpLeftAnimator(Animator):
	def start_(self, tmp=None):
		pivot= (self.widget.x-self.widget.width/2,self.widget.y)
		self.widget.origin_= pivot

		props=["angle","opacity"]
		vals=[-90,0]
		self._initialize(**dict(zip(props,vals)))

		vals=[0,1]
		anim= Animation(
			d= self.duration,
			**dict(zip(props,vals))
			)
		
		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class RotateInUpRightAnimator(Animator):
	def start_(self, tmp=None):
		pivot= (self.widget.x+3*self.widget.width/2,self.widget.y)
		self.widget.origin_= pivot

		props=["angle","opacity"]
		vals=[90,0]
		self._initialize(**dict(zip(props,vals)))

		vals=[0,1]
		anim= Animation(
			d= self.duration,
			**dict(zip(props,vals))
			)
		
		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))
