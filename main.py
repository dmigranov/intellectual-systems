from author_recognition import *

classifier = AuthorClassifier()
classifier.train([["Text/Tolstoy_train"], ["Text/Dostoevsky_train"], ["Text/Turgenev_train"]], ["Толстой", "Достоевский", "Тургенев",])
print(classifier.predict(["Text/Dostoevsky_test1", "Text/Dostoevsky_test2", "Text/Tolstoy_test1", "Text/Tolstoy_test2", "Text/Tolstoy_test3", "Text/Turgenev_test1", "Text/Turgenev_test2"]))
