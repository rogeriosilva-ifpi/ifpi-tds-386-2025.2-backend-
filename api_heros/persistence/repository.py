from abc import ABC

class RepositoryCamera(ABC):

  def __init__(self):
    pass

  def create(self):
    raise not NotImplementedError()

  def all(self):
    raise not NotImplementedError()



class RepositoryCameraRaiz(RepositoryCamera):
  def __init__(self):
    pass

  def create(self):
    # codigo SQL Raiz
    ...

  def all(self):
    ...


class RepositoryCameraSQLModel(RepositoryCamera):
  def __init__(self):
    pass

  def create(self):
    # usando SQL Model
    ...

  def all(self):
    ...