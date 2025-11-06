import matplotlib.pyplot as plt
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]
# Create bar chart
plt.bar(languages, popularity, color='skyblue')
# Add title and labels
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
# Show the plot
plt.show()
