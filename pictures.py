import requests

image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4rynfs1wJGEZ5iM4LYKkMesf8itB4r-5GIdHW9MfFBopmYTMKWIhx8HJwqI7ggGXZml0:https://a.espncdn.com/combiner/i%3Fimg%3D/i/teamlogos/nfl/500/sea.png&usqp=CAU'
    #image  = input('please input your desired image link')
    #still working on how to ask for input of a link
    #we will learn how to pull an image link and display it somewhere next

picture = requests.get(image)
print(picture.content)
with open('ryang:\abc.png','wb') as f:
    f.write(picture.content)