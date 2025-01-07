import os
from time import sleep

os.system('COLOR B')


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in range(len(self.users)):
            if self.users[i].nickname == nickname and self.users[i].password == password:
                self.users[i].nickname = nickname
                self.users[i].password = password

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.nickname = nickname
            self.users.password = password
            self.users.age = age

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for e in video:
            if e not in self.videos:
                self.videos.append(e)

    def get_videos(self, word):
        for e in self.videos:
            if e.title != word:
                self.videos.append(word)
                break

    def watch_video(self, title):
        pass


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

try:
    os.system('PAUSE')
except:
    os.system('CLS')
