import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from skills.base_skills import *
from skills.open_apps import *
from skills.radio import *
from langs.ru.voice import *
from langs.ru.listen import *
from langs.en.voice import *
from langs.en.listen import *




def recognize(data, vectorizer, clf):
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return
    
    data.replace(list(trg)[0], '')
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]
    speak_ru(answer.replace(func_name, ''))
    exec(func_name + '(user_command_ru, user_command_en)')


def main():
    global user_command_ru, user_command_en
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))
    
    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))
    
    del words.data_set
    
    speak_ru('шьпокс.')
    while True:
        user_command_en = ''
        user_command_ru = listen_ru()
        # user_command_ru = input("Запрос --->>>  ") этот код я оставил для очень нужных тестов
        print(user_command_ru)
        # print(user_command_en) этот код я оставил для очень нужных тестов
        recognize(user_command_ru, vectorizer, clf)


if __name__ == "__main__":
    main()