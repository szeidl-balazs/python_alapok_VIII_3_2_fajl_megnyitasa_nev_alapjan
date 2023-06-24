def read_file(file_name):
   target_file = open(file_name)
   content = target_file.read()
   print(content)
   target_file.close()


def get_file_name():
    return input('Which file you want to open? ')

read_file(get_file_name())