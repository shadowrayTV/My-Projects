class Item:
    def __init__(self):
        self.name = None
        self.description = None

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_desc):
        self.description = item_desc


