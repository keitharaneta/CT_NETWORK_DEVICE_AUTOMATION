excel_value = ['DEVICE_TYPE', 'SWITCH', 'MODEL', 'C9000-SWITCH', 'REGION',
               'ASIAPAC', None, None, 'COUNTRY', 'INDIA', 'SITE', 'KALYANI']

brackets = {}
for rows in range(0, len(excel_value), 2):
    if excel_value[rows] is not None:
        brackets[excel_value[rows]] = excel_value[rows + 1]
    else:
        continue


print(brackets)