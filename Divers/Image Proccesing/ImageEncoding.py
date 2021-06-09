from png import Reader, Writer

textImage = input("Which image do you want to decode ?")

image = Reader("{}.png".format(textImage))

if (image.width % 4 != 0) and (image.height % 4 != 0):
    raise TypeError

img = image.read()
img = img[2]

n = 0
output = []
for k in range(0, len(img), 2):
    # Iterate through the lines
    output.append([])

    for l in range(0, len(img[k]), 2):
        # Iterate through the columns
        # Check based on the index, which color channel is being examined, and act accordingly
        output[n].append(bin(j))