# #1 

# #nested_list
# list1 = [1,2,['A',['a','b'],'B'],3,['C','D'],4]
# print(list1)
# print(list1[0])
# print(list1[2])
# print(list1[4])
# print(list1[2][0])
# print(list1[2][1])
# print(list1[2][1][0])


#2
#nested_dictionary
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

print(info)
print('\n')
print(info['personal_data'])
print('\n')
print(info['personal_data']['physical_features'])
print('\n')
print(info['personal_data']['physical_features']['color'])
print('\n')
print(info['personal_data']['physical_features']['height'])
print('\n')
print(info['personal_data']['physical_features']['color']['eye'])


