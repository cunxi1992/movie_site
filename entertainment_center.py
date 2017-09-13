# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

# 初始化Movie实例,每个电影赋值标题、简介、海报、预告/播放链接
finding_dory = media.Movie(
	"Finding Dory",
	"Finding Dory is a 2016 American 3D computer-animated comedy adventure film",
	"http://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Finding_Dory.jpg/220px-Finding_Dory.jpg",
	"https://www.youtube.com/watch?v=TmMz152GOA0")

inside_out = media.Movie(
	"Inside Out",
	"Inside Out is a 2015 American 3D computer-animated coming of age comedy-drama adventure film",
	"http://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
	"https://www.youtube.com/watch?v=GxQqs_NnByw")

the_boss_baby = media.Movie(
	"The Boss Baby",
	"The Boss Baby is a 2017 American computer-animated comedy film loosely based on the 2010 picture book of the same name written and illustrated by Marla Frazee",
	"http://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",
	"https://www.youtube.com/watch?v=b_yRedsGnDk")

tommy_boy = media.Movie(
    "Tommy Boy",
    "A college dropout has to save his father's company.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f8/Tommy_Boy.jpg/220px-Tommy_Boy.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6nQ4K2bvVxY&t=13s")

the_incredibles = media.Movie(
    "The Incredibles",
    "Superhero family comes out of retirement.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/The_Incredibles.jpg/220px-The_Incredibles.jpg",  # NOQA
    "https://www.youtube.com/watch?v=eZbzbC9285I")

happy_gilmore = media.Movie(
    "Happy Gilmore",
    "Washout hockey player becomes golf sensation.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Happygilmoreposter.jpg/220px-Happygilmoreposter.jpg",  # NOQA
    "https://www.youtube.com/watch?v=y1emDAYCfVQ")

indiana_jones = media.Movie(
    "Raiders of the Lost Ark",
    "Archaeology professor recovers Ark of the Covenant.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Raiders_of_the_Lost_Ark.jpg/220px-Raiders_of_the_Lost_Ark.jpg",  # NOQA
    "https://www.youtube.com/watch?v=XkkzKHCx154")

pirates_caribbean = media.Movie(
    "Pirates of the Caribbean",
    "Cursed undead pirates wreak havoc until another pirate intervenes.",
    "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",  # NOQA
    "https://www.youtube.com/watch?v=naQr0uTrH_s")

matrix = media.Movie(
    "The Matrix",
    "We are all really just batteries.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=vKQi3bBA1y8")


# 将电影列表添加至数组
movies = [
	finding_dory,
	inside_out,
	the_boss_baby,
	tommy_boy,
    the_incredibles,
    happy_gilmore,
    indiana_jones,
    pirates_caribbean,
    matrix
	]

# 创建 电影网站
fresh_tomatoes.open_movies_page(movies)

