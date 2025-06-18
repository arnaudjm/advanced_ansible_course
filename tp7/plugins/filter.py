def reverse(text):
    return text[::-1]

class FilterModule(object):

  def filters(self):
    return {
      'reverse': reverse
    }