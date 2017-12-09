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
#
#
# plt.ion()                    #sets plot to animation mode
#
# length = 500                 #determines length of data taking session (in data points)
# # dist1 = [0]*length
# # dist2 = [0]*length
# # dist3 = [0]*length
# # dist4 = [0]*length
# # Ax = [0]*length               #create empty variable of length of test
# # Ay = [0]*length
# # Az = [0]*length
# # Gx = [0]*length               #create empty variable of length of test
# # Gy = [0]*length
# Gz = [0]*length
#
# # dist1line, = plt.plot(dist1)
# # dist2line, = plt.plot(dist2)
# # dist3line, = plt.plot(dist3)
# # dist4line, = plt.plot(dist4)
# # Axline, = plt.plot(Ax)         #sets up future lines to be modifed
# # Ayline, = plt.plot(Ay)
# # Azline, = plt.plot(Az)
# # Gxline, = plt.plot(Gx)         #sets up future lines to be modifed
# # Gyline, = plt.plot(Gy)
# Gzline, = plt.plot(Gz)
# plt.ylim(-20000,20000)        #sets the y axis limits
# fig, axes = plt.subplots(nrows=1)
# fig.show()
# fig.canvas.draw()
# styles = ['r-']
# def plot(ax, style):
#     return ax.plot(length, np.array(Gz) style, animated=True)[0]
#
# lines = [plot(ax, style) for ax, style in zip(axes, styles)]
#
# while(True):     #while you are taking data
    # data = ser.readline()    #reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
    # sep = data.split()      #splits string into a list at the tabs
    # # print data
    # try:
    #     # dist1.append(int(sep[0]))
    #     # dist2.append(int(sep[1]))
    #     # dist3.append(int(sep[2]))
    #     # dist4.append(int(sep[3]))
    #     # Ax.append(int(sep[4]))
    #     # Ay.append(int(sep[5]))
    #     # Az.append(int(sep[6]))
    #     # Gx.append(int(sep[7]))
    #     # Gy.append(int(sep[8]))
    #     Gz.append(int(sep[9]))
    #
    # except:
    #     # dist1.append(dist1[-1])
    #     # dist2.append(int(sep[-1]))
    #     # dist3.append(int(sep[-1]))
    #     # dist4.append(int(sep[-1]))
    #     # Ax.append(int(sep[-1]))
    #     # Ay.append(int(sep[-1]))
    #     # Az.append(int(sep[-1]))
    #     # Gx.append(int(sep[-1]))
    #     # Gy.append(int(sep[-1]))
    #     Gz.append(int(sep[-1]))
    #
    #
    # # del dist1[0]
    # # del dist2[0]
    # # del dist3[0]
    # # del dist4[0]
    # # del Ax[0]
    # # del Ay[0]
    # # del Az[0]
    # # del Gx[0]
    # # del Gy[0]
    # del Gz[0]
#     tstart = time.time()
#     # dist1line.set_xdata(np.arange(len(dist1)))
#     # dist2line.set_xdata(np.arange(len(dist2)))
#     # dist3line.set_xdata(np.arange(len(dist3)))
#     # dist4line.set_xdata(np.arange(len(dist4)))
#     # Axline.set_xdata(np.arange(len(Ax)))
#     # Ayline.set_xdata(np.arange(len(Ay)))
#     # Azline.set_xdata(np.arange(len(Az)))
#     # Gxline.set_xdata(np.arange(len(Gx)))
#     # Gyline.set_xdata(np.arange(len(Gy)))
#     Gzline.set_xdata(np.arange(len(Gz)))
#
#     # dist1line.set_ydata(dist1)
#     # dist2line.set_ydata(dist2)
#     # dist3line.set_ydata(dist3)
#     # dist4line.set_ydata(dist4)
#     # Axline.set_ydata(Ax)
#     # Ayline.set_ydata(Ay)
#     # Azline.set_ydata(Az)
#     # Gxline.set_ydata(Gx)
#     # Gyline.set_ydata(Gy)
#     Gzline.set_ydata(Gz)
#
#     backgrounds = [fig.canvas.copy_from_bbox(ax.bbox) for ax in axes]
#
#     tstart = time.time()
#     for i in xrange(1, 2000):
#         items = enumerate(zip(lines, axes, backgrounds), start=1)
#         for j, (line, ax, background) in items:
#             fig.canvas.restore_region(background)
#             line.set_ydata(np.sin(j*x + i/10.0))
#             ax.draw_artist(line)
#             fig.canvas.blit(ax.bbox)
#     plt.pause(0.001)                   #in seconds
#     plt.draw()                         #draws new plot
#     print (500/(time.time() - tstart))
# ser.close() #closes serial connection (very important to do this! if you have an error partway through the code, type this into the cmd line to close the connection)


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

y = np.array(Gz)
#plt.ylim(-20000,20000)        #sets the y axis limits
fig, axes = plt.subplots(nrows=10, figsize=(15,15))

fig.show()

# We need to draw the canvas before we start animating...
fig.canvas.draw()

styles = ['r-', 'g-','r-', 'g-','r-', 'g-','r-', 'g-','r-', 'g-']
def plot(ax, style):
    ax.set_ylim(-300, 300)
    return ax.plot(x, y, style, animated=True)[0]

lines = [plot(ax, style) for ax, style in zip(axes, styles)]

# Let's capture the background of the figure
backgrounds = [fig.canvas.copy_from_bbox(ax.bbox) for ax in axes]

tstart = time.time()
while True:
        data = ser.readline()    #reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
        sep = data.split()      #splits string into a list at the tabs
        print data
        if len(sep)==10:
            try:
                dist1.append(int(sep[0]))
                dist2.append(int(sep[1]))
                dist3.append(int(sep[2]))
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

        data_sets = [dist1, dist2, dist3, dist4, Ax, Ay, Az, Gx, Gy, Gz]
        items = enumerate(zip(data_sets,lines, axes, backgrounds), start=1)
        for j, (data_set,line, ax, background) in items:
            fig.canvas.restore_region(background)
            line.set_ydata(np.array(data_set))
            if j>=5:
                ax.set_ylim(-40000, 40000)
            ax.draw_artist(line)
            fig.canvas.blit(ax.bbox)
# for i in xrange(1, 2000):
#     items = enumerate(zip(lines, axes, backgrounds), start=1)
#     for j, (line, ax, background) in items:
#         fig.canvas.restore_region(background)
#         line.set_ydata(np.sin(j*x + i/10.0))
#         ax.draw_artist(line)
#         fig.canvas.blit(ax.bbox)

print 'FPS:' , 2000/(time.time()-tstart)
