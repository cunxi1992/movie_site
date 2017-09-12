# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

# 初始化Movie实例
finding_dory = media.Movie("Finding Dory","Finding Dory is a 2016 American 3D computer-animated comedy adventure film produced by Pixar Animation Studios and released by Walt Disney Pictures","http://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Finding_Dory.jpg/220px-Finding_Dory.jpg","https://www.youtube.com/watch?v=TmMz152GOA0")
inside_out = media.Movie("Inside Out","Inside Out is a 2015 American 3D computer-animated coming of age comedy-drama adventure film produced by Pixar Animation Studios and released by Walt Disney Pictures","http://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg","https://www.youtube.com/watch?v=GxQqs_NnByw")
the_boss_baby = media.Movie("The Boss Baby","The Boss Baby is a 2017 American computer-animated comedy film loosely based on the 2010 picture book of the same name written and illustrated by Marla Frazee[4] and produced by DreamWorks Animation","http://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg","https://www.youtube.com/watch?v=b_yRedsGnDk")
hunger_games = media.Movie("Hunger Games","Find out more about the story that set the world on fire.","http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg","https://www.youtube.com/watch?v=PbA63a7HObo")
midnight_in_paris = media.Movie("Midnight in Paris","Midnight in Paris is a 2011 fantasy comedy film written and directed by Woody Allen","http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=atLg2wQQxvU")
ratatouille = media.Movie("Ratatouille","Storyline:It is the eighth film produced by Pixar and was co-written and directed by Brad Bird, who took over from Jan Pinkava in 2005","http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://www.youtube.com/watch?v=c3sBBRxDAqk")
toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar","A marine on an alien planet","http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=-9ceBgWV8io")
school_of_rock = media.Movie("School Of Rock","Storyline:school of rock","http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")

# 将电影列表添加至数组
movies = [finding_dory,inside_out,the_boss_baby,hunger_games,midnight_in_paris,ratatouille,toy_story,avatar,school_of_rock]
# 创建 电影网站
fresh_tomatoes.open_movies_page(movies)

