# '''
# Reads in data over a serial connection and plots the results live. Before closing, the data is saved to a .txt file.
# '''
#
import serial
import matplotlib.pyplot as plt
import numpy as np
import sys
import time

connected = False

#finds COM port that the Arduino is on (assumes only one Arduino is connected)
if(len(sys.argv) != 2):
  print 'Example usage: python showdata.py "/dev/tty.usbmodem411"'
  exit(1)

#strPort = '/dev/tty.usbserial-A7006Yqh'
comPort = sys.argv[1];

ser = serial.Serial(comPort, 115200) #sets up serial connection (make sure baud rate is correct - matches Arduino)
print ser;
while not connected:
    serin = ser.read()
    connected = True

import time

length = 500
x = np.arange(0,length, 1)


dist1 = [0]*length
dist2 = [0]*length
dist3 = [0]*length
dist4 = [0]*length
Ax = [0]*length
Ay = [0]*length
Az = [0]*length
Gx = [0]*length
Gy = [0]*length
Gz = [0]*length
pothole = [0]*length

y = np.array(dist1)
#plt.ylim(-20000,20000)        #sets the y axis limits
fig, axes = plt.subplots(nrows=6, figsize=(15,15))

fig.show()

# We need to draw the canvas before we start animating...
fig.canvas.draw()

styles = ['r-', 'g-','r-', 'g-','r-', 'g-']
def plot(ax, style):
    ax.set_ylim(200, 400)
    return ax.plot(x, y, style, animated=True)[0]

lines = [plot(ax, style) for ax, style in zip(axes, styles)]

# Let's capture the background of the figure
backgrounds = [fig.canvas.copy_from_bbox(ax.bbox) for ax in axes]

tstart = time.time()
while True:
        data = ser.readline()    #reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
        sep = data.split()      #splits string into a list at the tabs
        # print sep
        if len(sep)==10:
            try:
                dist1.append(int(sep[0]))
                dist2.append(int(sep[1]))
                dist3.append(int(sep[2])-10)
                dist4.append(int(sep[3]))
                Ax.append(int(sep[4]))
                Ay.append(int(sep[5]))
                Az.append(int(sep[6]))
                Gx.append(int(sep[7]))
                Gy.append(int(sep[8]))
                Gz.append(int(sep[9]))

            except:
                dist1.append(dist1[-1])
                dist2.append(dist2[-1])
                dist3.append(dist3[-1])
                dist4.append(dist4[-1])
                Ax.append(Ax[-1])
                Ay.append(Ay[-1])
                Az.append(Az[-1])
                Gx.append(Gx[-1])
                Gy.append(Gy[-1])
                Gz.append(Gz[-1])


            del dist1[0]
            del dist2[0]
            del dist3[0]
            del dist4[0]
            del Ax[0]
            del Ay[0]
            del Az[0]
            del Gx[0]
            del Gy[0]
            del Gz[0]

            dist_detect = [1 for distance in [dist1[-1], dist2[-1], dist3[-1]] if distance < 280]
            accel_detect = [1 for accel in [Ax[-1],Ay[-1],Az[-1]] if abs(accel)>50]
            if (len(dist_detect)>1 or len(accel_detect)>1):
                pothole.append(1)
            else:
                pothole.append(0)
            print pothole[-1]

        data_sets = [dist1, dist2,Ax, Ay, Az, pothole]#, Gx, Gy, Gz
        items = enumerate(zip(data_sets,lines, axes, backgrounds), start=1)
        for j, (data_set,line, ax, background) in items:
            try:
                fig.canvas.restore_region(background)

                line.set_ydata(np.array(data_set))
                if j>=3 and j<6:
                    ax.set_ylim(-40000, 40000)
                elif j>=6:
                    ax.set_ylim(0, 2)

                ax.draw_artist(line)
                print "hello"
                fig.canvas.blit(ax.bbox)
            except:
                pass
print 'FPS:' , 2000/(time.time()-tstart)
