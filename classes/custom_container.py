class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags.items())


cloud = TagCloud()
# Add tags
cloud.add("Python")
cloud.add("Python")
cloud.add("java")
cloud.add("Java")

# # Access the count of specific tags using __getitem__
# python_count = tag["python"]
# java_count = tag["java"]
# cpp_count = tag["cpp"]

# print(f"Python Count: {python_count}")  # Output: Python Count: 2
# print(f"Java Count: {java_count}")      # Output: Java Count: 2
# print(f"C++ Count: {cpp_count}")        # Output: C++ Count: 0

# # Set counts for specific tags using __setitem__
# tag["python"] = 5
# tag["java"] = 3
# tag["cpp"] = 1

# print(tag["python"])  # Output: 5
# print(tag["java"])    # Output: 3
# print(tag["cpp"])     # Output: 1

# # Get the length of the tag cloud using __len__
# tag_count = len(tag)
# print(f"Total Tags: {tag_count}")  # Output: Total Tags: 3

# # Iterate over the tag cloud using __iter__
# for tag_name, count in tag:
#     print(f"Tag: {tag_name}, Count: {count}")
print(cloud["PYTHON"])
print(cloud._TagCloud__tags)
