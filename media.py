# -*- coding: utf-8 -*-
import webbrowser
class Movie():
	"""定义Movie类的构造函数"""
	def __init__(self, movie_title,movie_storyline,poster_image,trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
	#定义实例方法，用于播放电影预告片
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

