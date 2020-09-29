# Import the pypng library
from png import Reader, Writer

# Ask for input
textImage = input("Which image do you want to modify? : ")

# Format the input in order to only keep necessary data
image = Reader("{}.png".format(textImage))
i = image.read()
i = list(i[2])

# Initialize empty lists
n = 0
outputR = []
outputG = []
outputB = []
outputC = []
outputM = []
outputY = []

""" Loop exploring the image """

# Handling the presence or absence of the alpha channel
m = 3
if len(i) > (image.width * 3):
    m = 4

for k in i:
    # Iterate through the lines

    outputR.append([])
    outputG.append([])
    outputB.append([])
    outputM.append([])
    outputY.append([])
    outputC.append([])

    j = 0
    for l in k:
        # Iterate through the columns

        # Check based on the index, which color channel is being examined, and act accordingly
        if j%m == 0:
            outputR[n].append(l)
            outputG[n].append(0)
            outputB[n].append(0)
            outputM[n].append(l)
            outputY[n].append(l)
            outputC[n].append(0)

        elif j%m == 1:
            outputR[n].append(0)
            outputG[n].append(l)
            outputB[n].append(0)
            outputM[n].append(l)
            outputY[n].append(0)
            outputC[n].append(l)

        elif j%m == 2:
            outputR[n].append(0)
            outputG[n].append(0)
            outputB[n].append(l)
            outputM[n].append(0)
            outputY[n].append(l)
            outputC[n].append(l)

        if j%m == 3:
            outputR[n].append(l)
            outputG[n].append(l)
            outputB[n].append(l)
            outputM[n].append(l)
            outputY[n].append(l)
            outputC[n].append(l)


        j += 1
    
    n += 1

# Set up the Writer object for creating new images out of the lists
w = Writer(image.width, image.height, greyscale=False)

# Write each of the images
f = open("{}R.png".format(textImage), "wb")
w.write(f, outputR)

f = open("{}B.png".format(textImage), "wb")
w.write(f, outputB)

f = open("{}G.png".format(textImage), "wb")
w.write(f, outputG)

f = open("{}M.png".format(textImage), "wb")
w.write(f, outputM)

f = open("{}Y.png".format(textImage), "wb")
w.write(f, outputY)

f = open("{}C.png".format(textImage), "wb")
w.write(f, outputC)

print("RGB Separation Complete")