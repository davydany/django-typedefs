import datetime

from typedefs.constants import DATE_FORMAT, DATETIME_FORMAT

class BaseTypeDefinition(object):
  """
  The BaseTypeDefinition class provides base model for 
  all custom TypeDefinitions to be inherited.

  Certain methods in the BaseTypeDefinition class needs
  to be overridded as they behave like interfaces, and 
  ensure the right behavior.
  """
  _value = None

  def __init__(self, value:str=None):

    self._value = value

  @property
  def raw_value(self):

    return self._value

  @property
  def value(self):

    return self.to_python()

  @value.setter
  def value(self, value):

    self._value = self.from_python(value)

  def to_python(self):
    """
    Override `to_python` to cast the
    value in `_value` to a object or
    value that is purely pythonic.
    
    Consider this method as the same
    as deserializing a string to an
    object.
    """
    raise NotImplementedError()

  def from_python(self, value):
    """
    Override `from_python` to convert
    the value provided in `value` to 
    a string format that is easy to 
    return to a pythonic object with
    `to_python`.

    Consider this method as the same 
    as serializing an object to a string.
    """
    raise NotImplementedError()

class Boolean(BaseTypeDefinition):
  """
  A container for Boolean Values.
  """
  def to_python(self) -> bool:

    if self._value:
      if self._value.lower() in ['true', '1', 't', 'y']:
        return True
      else:
        return False
    else:
      return False # basically this is None or '', which is False 

  def from_python(self, value:bool) -> str:

    if value:
      return '1'
    else:
      return '0'

    return self._value

class Integer(BaseTypeDefinition):
  """
  A container for Integer Values.
  """

  def to_python(self) -> int:

    if self._value:
      return int(self._value)
    else:
      return 0

  def from_python(self, value:int) -> str:

    if value:
      return str(value)
    else:
      return '0'

class Float(BaseTypeDefinition):
  """
  A container for Float Values.
  """

  def to_python(self) -> float:

    if self._value:
      return float(self._value)
    else:
      return 0

  def from_python(self, value:float) -> str:

    if value:
      return str(value)
    else:
      return '0'

class Date(BaseTypeDefinition):
  """
  A container for Date Values.
  """

  def to_python(self) -> datetime.date:

    return datetime.datetime.strptime(self._value, DATE_FORMAT).date()

  def from_python(self, value:datetime.date) -> str:

    return value.strftime(DATE_FORMAT)

class DateTime(BaseTypeDefinition):
  """
  A container for DateTime Values.
  """

  def to_python(self) -> datetime.datetime:

    return datetime.datetime.strptime(self._value, DATETIME_FORMAT)

  def from_python(self, value:datetime.datetime) -> str:

    return value.strftime(DATETIME_FORMAT)

class String(BaseTypeDefinition):
  """
  A container for String Values.
  """
  def to_python(self) -> str:

    return self._value

  def from_python(self, value:str) -> str:

    return value

TYPE_DEFINITIONS = (
  ('boolean', Boolean),
  ('integer', Integer),
  ('float', Float),
  ('date', Date),
  ('datetime', DateTime),
)