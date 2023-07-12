from odmantic import Model
from database import Collection


class User(Model):
    email: str

    class Config:
        collection = Collection.USERS

    @property
    def collection(self):
        return self.Config.collection
