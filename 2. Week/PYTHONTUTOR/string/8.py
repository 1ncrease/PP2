str_ = input()
print(str_[:str_.find('h')] + str_[str_.rfind('h'):str_.find('h'):-1] + str_[str_.rfind('h'):])
