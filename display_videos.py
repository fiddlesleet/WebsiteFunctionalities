import media
import fresh_tomatoes

# fill in Fields
video1_title = "The School of Life: The Importance of Vulnerability"
video1_synopsis = "We often imagine that what will win us friends and esteem is strength. But surprisingly, it's vulnerability that's at the core of friendship and likeability."
video1_thumbnail = "http://i3.ytimg.com/vi/PJsJ96yyVk8/maxresdefault.jpg"
video1_link = "https://www.youtube.com/watch?v=PJsJ96yyVk8"

school_of_life1 = media.Video(video1_title, video1_synopsis, video1_thumbnail, video1_link)

# check it worked
print(school_of_life1.synopsis)

# launch video in browser
school_of_life1.play_video()

videos = [school_of_life1,
          school_of_life1,
          school_of_life1,
          school_of_life1,
          school_of_life1,
          school_of_life1]
fresh_tomatoes.open_movies_page(videos)
