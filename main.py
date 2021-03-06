from author_recognition import *

classifier = AuthorClassifier()
classifier.train([["Text/Tolstoy_train"], ["Text/Dostoevsky_train"], ["Text/Turgenev_train"], ["Text/Gogol_train"], ["Text/Strug_train"], ["Text/Bulych_train"], ["Text/Bulgakov_train"], ["Text/IP_train"]], ["Толстой", "Достоевский", "Тургенев", "Гоголь", "Стругацкие", "Булычёв", "Булгаков", "Ильф и Петров"])
print(classifier.predict([  "Text/Dostoevsky_test1", "Text/Dostoevsky_test2", "Text/Tolstoy_test1", "Text/Tolstoy_test2", "Text/Tolstoy_test3", 
                            "Text/Turgenev_test1", "Text/Turgenev_test2", "Text/Gogol_test1", "Text/Gogol_test2", "Text/Gogol_test3", 
                            "Text/Strug_test1", "Text/Strug_test2", "Text/Bulych_test1", "Text/Bulych_test2", "Text/Bulych_test3",
                            "Text/Bulgakov_test1", "Text/IP_test1", "Text/IP_test1"]))
