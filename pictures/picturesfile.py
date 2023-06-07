import requests

link = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtshvnV97P9h_-O7We70XPzh7bmwSApVvD1sAVZ0Ooo1nSwSe3OdROAzXvnNNC6RwYueh-ypNo6Is:https://a.espncdn.com/i/teamlogos/nfl/500/sea.png&usqp=CAU&ec=48665701'
image = link

    #image  = input('please input your desired image link')

    #still working on how to ask for input of a link

     #we will learn how to pull an image link and display it somewhere next


picture = requests.get(image)

print(picture.content)

with open('imagefordemo:abcde.png','wb') as f:
    f.write(picture.content)