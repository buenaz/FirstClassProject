class Post:
    def __init__(self, text, title, description, author):
        self.likes = 0
        self.dislikes = 0
        self.comments = []
        self.text = text
        self.title = title
        self.description = description
        self.author = author
    def like(self):
        self.likes += 1
    def dislike(self):
        self.dislikes += 1
    def comment(self, comment):
        self.comments.append(comment)
    def get_info(self):
        return f"Опубликована новая статья. \n Автор: {self.author} \n Заголовок: {self.title} \n Описание: {self.description} \n Текст: {self.text} \n Статья набрала {self.likes} лайк \n Свежие комментарии к статье: {self.comments}"

class Review:
    def __init__(self, text_customer, stars):
        self.text_customer = text_customer
        self.stars = stars # не больше 5
    def get_info(self):
        return f"Отзыв читателя: {self.text_customer} \n Отзыв набрал: {self.stars} звезд"

class Feedback:
    def __init__(self, theme, text, phone, name):
        self.name = name
        self.theme = theme
        self.text = text
        self.phone = phone
    def get_info(self):
        return f"Пользователь под ником {self.name} обратился в обратную связь \n Тема: {self.theme} \n Номер телефона: {self.phone} \n Текст: {self.text} \nСкоро мы вам перезвоним!"

def main():
    emails = []
    text_post = Post(text="Текст статьи", title="Название статьи", description="Описание статьи", author="Автор статьи")
    text_post.like()
    text_post.comment("Комментарий")
    text_review = Review(text_customer="Отзыв", stars=5)

    print(text_post.get_info())
    print(' ')
    print(text_review.get_info())
    print(' ')

    q = input("Желаете оставить заявку обратной связи (Да\Нет): ")
    if q.lower() == 'да':
        text_feedback = Feedback(name=input("Введите имя: "),
                                 theme=input("Введите тему обращения: "),
                                 text=input("Введите текст: "),
                                 phone=input("Введите номер телефона для обратной связи: "))
        print(text_feedback.get_info())
        print("Спасибо за чтение статьи, как только выйдет новая мы обязательно к вам обратимся!")
        email = input("Не могли бы вы оставить свою почту для рассылки: ")
        emails.append(email)
        print(f"В нашем сервисе зарегистрировано {len(emails)} почт")
    else:
        print("Спасибо за чтение статьи, как только выйдет новая мы обязательно к вам обратимся!")
        email = input("Не могли бы вы оставить свою почту для рассылки: ")
        emails.append(email)
        print(f"В нашем сервисе зарегистрировано {len(emails)} почт")

if __name__ == '__main__':
    main()