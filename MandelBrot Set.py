import time

calcTotal = 0
timeStart = time.time()

ppmImage = [[[255 for c in range(3)] for w in range(1920)] for h in range(1080)]

# basic loop assignments and line equations
for Ya in range(0, 1080):
    y = Ya * (1.25/540) - 1.25
    for Xa in range(0, 1920):
        x = Xa * (1.25/960) - 1.3

# convert the numbers into a complex state
        
        z = complex(x, y)
        c = z

# attempt the recursive numbers
        for depth in range(255):
            z = z**2 + c
            calcTotal += 1

# if sqrt(x**2 + y**2) is greater then 4, the number is too far gone
            if abs(z) > 4:
                print(f'value{c} has devolved to infinity at {depth}')
                ppmImage[Ya][Xa] = [depth,depth,depth]
                break
        else:
            print(f'Did not Devolve, did not evolve: {z}')



# create the ppm image file
outputFile = open('MandelBrot.ppm', 'wb')
outputFile.write(bytearray(f'P6 1920 1080 255\n', 'ascii'))
for y in range(1080):
    for x in range(1920):
        outputFile.write(bytearray(ppmImage[y][x]))
outputFile.close()

# end of program, show statistics
print("--- %s seconds ---" % (time.time() - timeStart))
print(calcTotal)