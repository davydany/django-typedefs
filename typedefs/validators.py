import datetime

from django.utils.timezone import now as timezone_now
from typedefs.definitions import Boolean, Integer, Float, Date, DateTime

class InvalidValidationTypeDefinitionMatch(Exception):
  
  pass

class BaseValidator(object):
  """
  The BaseValidator is the base class that all 
  Validators should inherit from.  

  Certain methods in the BaseValidator class needs
  to be overridded as they behave like interfaces, and 
  ensure the right behavior.
  """

  allowed_definitions = []

  constraint = None

  def __init__(self, constraint=None, allowed_values=None):

    self.constraint = constraint

  def validatable(self, typedef):

    if typedef not in self.allowed_definitions:
      raise InvalidValidationTypeDefinitionMatch()

  def validate(self, value):

    raise NotImplementedError()

class MinimumNumericValidator(BaseValidator):
  """
  Restricts numeric value in Integer and Float fields
  to have a minimum value. If the value is less than 
  the minimum value, an error is thrown.
  """

  allowed_definitions = [Integer, Float]

  def validate(self, value:[int, float]):

    min_value = float(self.constraint)
    value = float(value)

    if value < min_value:
      msg = "'%s' is less than the allowed minimum value of '%s'" % (
        value, min_value
      )
      raise ValueError(msg)

class MaximumNumericValidator(BaseValidator):
  """
  Restricts numeric value in Integer and Float fields
  to have a maximum value. If the value is greater than
  the maximum value, an error is thrown.
  """

  allowed_definitions = [Integer, Float]

  def validate(self, value:[int, float]):

    max_value = float(self.constraint)
    value = float(value)
    
    if value > max_value:
      msg = "'%s' is greater than the allowed maximum value of '%s'" % (
        value, max_value
      )
      raise ValueError(msg)

class FutureDateValidator(BaseValidator):
  """
  Restricts date and datetime values in Date and DateTime fields
  to have a value in the future. If the value is before today,
  then an error is thrown.
  """
  allowed_definitions = [Date, DateTime]

  def validate(self, value:[datetime.date, datetime.datetime]):

    now = timezone_now()
    if now > value:
      raise ValueError("Date/Time is in the past.")
    



VALIDATORS = (
  ('future-date-validator', FutureDateValidator),
  ('minimum-numeric-validator', MinimumNumericValidator),
  ('maximum-numeric-validator', MaximumNumericValidator),
)