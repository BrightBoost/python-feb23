class Cat:
  # @property
  def __init__(self, name, nr_of_lives):
    self._name = name
    self.__nr_of_lives = nr_of_lives
    self._blabla = "blabla"

  def get_nr_of_lives(self):
    print("in nr of lives get")
    return self.__nr_of_lives

  @property
  def blabla(self):
    return self._blabla

  @blabla.setter
  def set_blabla(self, value):
    self._blabla = value

  def get_name(self):
    print("in name get")
    return self._name

  def set_name(self, name):
    self._name = name

  def del_name(self):
    del self._name

  name = property(get_name, set_name, del_name)

cat1 = Cat("Minoes", 9)
print(cat1.get_nr_of_lives(), cat1.name)
print(cat1.get_name())

print(cat1.blabla)
cat1.blabla = "jaja"
print(cat1.blabla)

