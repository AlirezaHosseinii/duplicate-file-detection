from difPy import dif

path = str(input("Enter the path: "))

search_for_duplicated_photos = dif(path)

duplicated_photos = search_for_duplicated_photos.result

print(duplicated_photos)
