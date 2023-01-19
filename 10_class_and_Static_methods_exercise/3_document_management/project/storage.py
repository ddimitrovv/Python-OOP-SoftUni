from project1.category import Category
from project1.document import Document
from project1.topic import Topic


class Storage:
    def __init__(self):
        self.categories = list()
        self.topics = list()
        self.documents = list()

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_by_id(self.categories, category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_by_id(self.topics, topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_by_id(self.documents, document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.__find_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_by_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_by_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.__find_by_id(self.documents, document_id)

    def __repr__(self):
        output = [repr(document) for document in self.documents]
        return '\n'.join(output)

    def __find_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity
