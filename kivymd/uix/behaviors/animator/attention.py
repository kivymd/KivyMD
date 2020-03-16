
from kivy.animation import Animation
from functools import partial

from base import Animator

__all__ = ('FlashAnimator','PulseAnimator', 'RubberBandAnimator','ShakeAnimator', 'SwingAnimator', 'WobbleAnimator', 
	'TadaAnimator', 'WaveAnimator')

# Attention------------
class FlashAnimator(Animator):
	def start_(self, tmp=None):
		anim= Animation(
			t= 'linear',
			d= self.duration/4,
			opacity=0
			)
		anim+= Animation(
			t= 'linear',
			d= self.duration/4,
			opacity=1
			)
		anim+= Animation(
			t= 'linear',
			d= self.duration/4,
			opacity=0
			)
		anim+= Animation(
			t= 'linear',
			d= self.duration/4,
			opacity=1
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class PulseAnimator(Animator):
	def start_(self, tmp=None):
		props=["height","width"]
		vals= [self._original["height"]*1.08,self._original["width"]*1.08]

		anim= Animation(
			t= 'in_circ',
			d= self.duration/2,
			**dict(zip(props,vals))
			)
		anim+= Animation(
			t= 'out_circ',
			d= self.duration/2,
			**self._original
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class RubberBandAnimator(Animator):
	def start_(self, tmp=None):
		props=["height","width"]
		vals= [self._original["height"]*0.75,self._original["width"]*1.25]

		anim= Animation(
			t= 'out_circ',
			d= self.duration/4,
			**dict(zip(props,vals))
			)

		vals= [self._original["height"]*1.25,self._original["width"]*0.75]
		anim+= Animation(
			t= 'out_circ',
			d= self.duration/4,
			**dict(zip(props,vals))
			)

		vals= [self._original["height"]*0.85,self._original["width"]*1.15]
		anim+= Animation(
			t= 'out_circ',
			d= self.duration/4,
			**dict(zip(props,vals))
			)

		anim+= Animation(
			t= 'out_circ',
			d= self.duration/4,
			**self._original
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class ShakeAnimator(Animator):
	def start_(self, tmp=None):
		props=["pos_hint",]
		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val+0.025
			else: __tmp[key]= val
		vals=[__tmp,]

		anim= Animation(
			d= self.duration/10,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.025
			else: __tmp[key]= val
		vals=[__tmp,]

		anim+= Animation(
			d= self.duration/10,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val+0.025
			else: __tmp[key]= val
		vals=[__tmp,]
		anim+= Animation(
			t= 'linear',
			d= self.duration/10,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.025
			else: __tmp[key]= val
		vals=[__tmp,]
		anim+= Animation(
			d= self.duration/10,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val+0.015
			else: __tmp[key]= val
		vals=[__tmp,]
		anim+= Animation(
			d= self.duration/10,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.015
			else: __tmp[key]= val
		vals=[__tmp,]
		anim+= Animation(
			t= 'linear',
			d= self.duration/10,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val+0.006
			else: __tmp[key]= val
		vals=[__tmp,]
		anim+= Animation(
			t= 'linear',
			d= self.duration/10,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.006
			else: __tmp[key]= val
		vals=[__tmp,]
		anim+= Animation(
			t= 'linear',
			d= self.duration/10,
			**dict(zip(props,vals))
			)

		anim+= Animation(
			t= 'out_circ',
			d= self.duration/10,
			**self._original
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class SwingAnimator(Animator):
	def start_(self, tmp=None):
		props=["angle"]

		vals=[self._original["angle"]-10]
		anim= Animation(
			d= self.duration/7,
			**dict(zip(props, vals))
			)

		vals=[self._original["angle"]+10]
		anim+= Animation(
			d= self.duration/7,
			**dict(zip(props, vals))
			)

		vals=[self._original["angle"]-6]
		anim+= Animation(
			d= self.duration/7,
			**dict(zip(props, vals))
			)

		vals=[self._original["angle"]+6]
		anim+= Animation(
			d= self.duration/7,
			**dict(zip(props, vals))
			)

		vals=[self._original["angle"]-3]
		anim+= Animation(
			d= self.duration/7,
			**dict(zip(props, vals))
			)

		vals=[self._original["angle"]+3]
		anim+= Animation(
			d= self.duration/7,
			**dict(zip(props, vals))
			)

		anim+= Animation(
			t= 'out_circ',
			d= self.duration/7,
			**self._original
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class WobbleAnimator(Animator):
	def start_(self, tmp=None):
		props=["pos_hint","angle"]

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.085
			else: __tmp[key]= val
		vals=[__tmp,self._original["angle"]+5]
		anim= Animation(
			d= self.duration/6,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val+0.080
			else: __tmp[key]= val
		vals=[__tmp,self._original["angle"]-3]
		anim+= Animation(
			d= self.duration/6,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.075
			else: __tmp[key]= val
		vals=[__tmp,self._original["angle"]+3]
		anim+= Animation(
			d= self.duration/6,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val+0.070
			else: __tmp[key]= val
		vals=[__tmp,self._original["angle"]-2]
		anim+= Animation(
			d= self.duration/6,
			**dict(zip(props,vals))
			)

		__tmp={}
		for key, val in self._original["pos_hint"].items():
			if key in ["center_x", "x", "left"]:
				__tmp[key]= val-0.065
			else: __tmp[key]= val
		vals=[__tmp,self._original["angle"]+2]
		anim+= Animation(
			d= self.duration/6,
			**dict(zip(props,vals))
			)

		anim+= Animation(
			t= 'out_circ',
			d= self.duration/6,
			**self._original
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class TadaAnimator(Animator):
	def start_(self, tmp=None):
		props=["height", "width","angle"]
		vals=[self._original["height"]*0.8,self._original["width"]*0.8,self._original["angle"]+3,]
		
		anim= Animation(
			d= self.duration/9,
			**dict(zip(props, vals))
			)

		vals=[self._original["height"]*0.8,self._original["width"]*0.8,self._original["angle"]+3,]
		anim+= Animation(
			d= self.duration/9,
			**dict(zip(props, vals))
			)

		vals=[self._original["height"]*1.1,self._original["width"]*1.1,self._original["angle"]-3,]
		anim+= Animation(
			d= self.duration/9,
			**dict(zip(props, vals))
			)

		vals=[self._original["height"]*1.1,self._original["width"]*1.1,self._original["angle"]+3,]
		anim+= Animation(
			d= self.duration/9,
			**dict(zip(props, vals))
			)

		vals=[self._original["height"]*1.1,self._original["width"]*1.1,self._original["angle"]-3,]
		anim+= Animation(
			d= self.duration/9,
			**dict(zip(props, vals))
			)

		vals=[self._original["height"]*1.1,self._original["width"]*1.1,self._original["angle"]+3,]
		anim+= Animation(
			d= self.duration/9,
			**dict(zip(props, vals))
			)

		vals=[self._original["height"]*1.1,self._original["width"]*1.1,self._original["angle"]-3,]
		anim+= Animation(
			d= self.duration/9,
			**dict(zip(props, vals))
			)

		vals=[self._original["height"]*1.1,self._original["width"]*1.1,self._original["angle"]+3,]
		anim+= Animation(
			d= self.duration/9,
			**dict(zip(props, vals))
			)

		anim+= Animation(
			t= 'out_circ',
			d= self.duration/9,
			**self._original,
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))

class WaveAnimator(Animator):
	def start_(self, tmp=None):
		props=["angle"]
		
		vals=[self._original["angle"]-12]
		anim= Animation(
			d= self.duration/5,
			**dict(zip(props,vals))
			)

		vals=[self._original["angle"]+12]
		anim+= Animation(
			d= self.duration/5,
			**dict(zip(props,vals))
			)

		vals=[self._original["angle"]-3]
		anim+= Animation(
			d= self.duration/5,
			**dict(zip(props,vals))
			)

		vals=[self._original["angle"]+3]
		anim+= Animation(
			d= self.duration/5,
			**dict(zip(props,vals))
			)

		anim+= Animation(
			d= self.duration/5,
			**self._original
			)

		anim.cancel_all(self.widget)
		anim.start(self.widget)
		anim.bind(on_complete= partial(self.anim_complete, self))
# Attention------------
