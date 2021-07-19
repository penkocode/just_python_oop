class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = [el for el in self.categories if el.id == category_id]
        if category:
            category = category[0]
            category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [el for el in self.topics if el.id == topic_id]
        if topic:
            topic = topic[0]
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = [el for el in self.documents if el.id == document_id]
        if document:
            document = document[0]
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [el for el in self.categories if el.id == category_id]
        if category:
            category = category[0]
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [el for el in self.topics if el.id == topic_id]
        if topic:
            topic = topic[0]
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [el for el in self.documents if el.id == document_id]
        if document:
            document = document[0]
            self.documents.remove(document)

    def get_document(self, document_id):
        document = [el for el in self.documents if el.id == document_id]
        if document:
            document = document[0]
            return repr(document)

    def __repr__(self):
        result = []
        for document in self.documents:
            result.append(repr(document))
        return '\n'.join(result)
