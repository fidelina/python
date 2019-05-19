import matplotlib.pyplot as plt

plt.figure(figsize=(7,5))
x = [18, 15, 11, 9, 8, 6]
labels = ['Java', 'C', 'C++', 'PHP', '(Visual) Basic', 'Python']
explode = [0, 0, 0, 0, 0, 0.2]

plt.pie(x, labels = labels, explode = explode, autopct = '%1.1f%%', shadow=True);
plt.show()