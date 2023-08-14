# Strings (Matnlar)

# Biz " dan yoki ' dan foydalanishimiz mumkin, albatta vaziyatga qarab
ism = "John"
familiya = 'Smith'
yosh = '21'
info = ism + familiya

# print(info)
# JohnSmith

info = ism + ' ' + familiya
# print(info)
# John Smith

message = "Juda kulguli🤣😂😂"
# print(message)
# Juda kulguli🤣😂😂

info = "Men" + ' '  + ism + ' ' + familiya + " " + "va, men"  + " " + yosh + " " +  "daman."

# print(info)
# Men John Smith va, men 21 daman.
info = f'Men {ism} {familiya} va, men {yosh} daman.'

# print(info)
# Men John Smith va, men 21 daman.

warning = '1234567890!@#$%^"`&*()_+-=":?>\'<,./{}[]|'

# print(f"""{warning}
# Siz faqatgina shu belgilardan foydalana olasiz!""")
# 1234567890!@#$%^"&*()_+-=":?>'<,./{}[]|
# Siz faqatgina shu belgilardan foydalana olasiz!


# print(f"{warning}\nSiz faqatgina shu belgilardan foydalana olasiz!")
# 1234567890!@#$%^"&*()_+-=":?>'<,./{}[]|
# Siz faqatgina shu belgilardan foydalana olasiz!

# print(f"{ism}\t{familiya}")