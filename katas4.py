
def instructorWithLongestName(course):
    n_length = []
    for i in range(len(course)):
        n_length.append((len(course[i]["name"])))
        print(n_length)
    return course[n_length.index(max(n_length))]

print(instructorWithLongestName([
  {"name": "Samuel", "course": "iOS"},
  {"name": "Jeremiah", "course": "Data"},
  {"name": "Ophilia", "course": "Web"},
  {"name": "Donald", "course": "Web"}
]))
print(instructorWithLongestName([
  {"name": "Matthew", "course": "Data"},
  {"name": "David", "course": "iOS"},
  {"name": "Domascus", "course": "Web"}
]))