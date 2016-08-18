import os


directory_of_file = os.path.dirname(__file__)

print('directory_of_file (where this test.py file is) - {0}'.format(directory_of_file))

directory_higher = os.path.dirname(directory_of_file)
print('directory_higher - {}'.format(directory_higher))

join = os.path.join(directory_of_file, 'test')
print('joined dir - {0}'.format(join))

join = os.path.join(directory_of_file, '/test')
print('joined dir - {0}'.format(join))

join = os.path.join(directory_of_file, './test')
print('joined dir - {0}'.format(join))

join = os.path.join(directory_of_file, '../test')
print('joined dir - {0}'.format(join))