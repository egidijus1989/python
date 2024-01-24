#ivedamas laikas valandomis ir minutemis, parasyti programa, kuri parod kiek bus po minutes
# jei ivedam 15 59 bus 16 00, jei 23 59 bus 0 0

# val = int(input('Valanda = '))
# min = int(input('Minute = '))

# def poMinutes (x, y):
#     if val == 23 and min == 59:
#         print("00 valandu ir 00 min")
#     elif min == 59:
#         print(f'{val + 1} valandos ir 00 minutes')
#     else:
#         print(f'{val} valandos ir {min + 1} minutes')
        
# poMinutes(val, min)

val = int(input('Valanda = '))
min = int(input('Minute = '))
min1 = min + 1
val1 = val + (min1//60)
min1 = min1 % 60
val1 = val1 % 24
print(f'po minutes bus {val1}:{min1}')