import csv
import matplotlib.pyplot as plt
from numpy import array
import pandas as pd
class xy_generator(object):
    """
    generate x,y coordinates from csv and xy file

    how it works:
    the filename is being inputted to class. the filename should contain extension
    csv or xy file. The file extension will be detected automatically.
    the x and y file will be generated after entering command get_raw_x_y
    """
    def __init__(self, file, label=None,xrd_type='Raw data'):
        """
        input:
        file (string): a filename
        label (string): label name for plotting name use, default =''

        variable in it:
        self.title (string) : a filename of input
        self.file_type (string): a file extension (.xy, .csv,.xls)
        self.x (list): 1-D array of x axis data plots
        self.y (list): 1-D array of y axis data plots
        """
        self.file = file
        # attempting to identify file extension
        try:
            self.file_type = self.file.split('.')[-1]
        except AttributeError:
            self.file_type = ''
        # attempting to identify label name for plot name
        if label == None or label == '':
            if '/' in self.file:
                self.label = xy_generator.get_label(self, self.file.split('/')[-1])
                self.label=self.label[6:]

            else:
                self.label = xy_generator.get_label(self, self.file)
        else:
            self.label = label
        self.data=xrd_type
        self.x, self.y = xy_generator.get_raw_x_y(self)

    def get_label(self, file):
        try:
            name = file.split('.')
            return name[0]
        except:
            return name

    def get_raw_x_y(self):
        """
        generate x,y file to self.x and self.y variabels
        automatically detects file extension and process it into list of data
        """
        if self.file_type == 'xy':
            open_file = open(self.file, 'r')
            raw_xy = open_file.readlines()
            pre_raw = []
            for i, j in enumerate(raw_xy):
                pre_raw.append([])
                # xy=[]
                raw_x = []
                raw_y = []
                for k in j.split(' '):
                    if k != '':
                        pre_raw[i].append(float(k))
            for i in pre_raw:
                raw_x.append(i[0])
                raw_y.append(i[1])
            self.x = array(raw_x)
            self.y = array(raw_y)
            open_file.close()
            self.label += ' (Simulated)'
        elif self.file_type == 'csv':
            raw_xy = []
            raw_x = []
            raw_y = []
            with open(self.file) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    try:
                        raw_xy.append(row)
                        raw_x.append(float(row[0]))
                        raw_y.append(float(row[1]))
                    except:
                        continue
            self.x = array(raw_x)
            self.y = array(raw_y)
        elif self.file_type == 'xls' or self.file_type == 'xlsx':
            raw_xy = pd.read_excel(self.file, sheet_name=self.data)
            raw_x = raw_xy['Pos. [°2Th.]'][1:]
            raw_y = raw_xy['Iobs [cts]'][1:]
            self.x = array(raw_x)
            self.y = array(raw_y)
            # print(raw_xy)
        else:
            print(self.file, "has no extension file.")
            return None
        return (self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class plot_graphs(object):
    def __init__(self,plot_a,plots='',norm_a=False,xrange=''):
        """
        Plot graph more efficiently
        :param plot_a: class of xy_generator (single)
        :param plots: list of xy_generator objects
        :param norm_a: (default=False) normalize the graph of A
        :param xrange: (default='') list of 2 values of range of the x axis
        """
        self.plot=plot_a
        self.plots=plots
        self.norm=norm_a
        self.xrange=xrange
    def get_plot(self,label=''):
        
        if label!='':
            label=label
        else:
            label=self.plot.label
        for i in self.plots:
            plt.figure(figsize=(10, 6.5), dpi=100)
            if len(self.xrange) == 2 and type(self.xrange) == list:
                plt.xlim(self.xrange[0], self.xrange[1])
            plt.title('Spektra XRD\n' + self.plot.label + '(Normalized: ' + str(self.norm) + ')')
            if self.norm == True:
                self.plot.y=self.plot.y/max(self.plot.y)*100
                plt.ylabel('intensity A.U')
            else:
                plt.ylabel('counts')
        plt.plot(self.plot.x,self.plot.y,label=label,linewidth=0.8)
        if i !='':
            plt.plot(i.x,i.y,label=i.label,alpha=0.8,linewidth=0.8)
        #plt.ylabel('Intensity')
        plt.xlabel('2θ')
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        plt.legend()
        plt.show()
        return None
    
    def plot_single(self,label=''):
        plt.figure(figsize=(10, 6.5), dpi=100)
        if len(self.xrange) == 2 and type(self.xrange) == list:
            plt.xlim(self.xrange[0], self.xrange[1])
        plt.title('Spektra XRD\n' + self.plot.label + '(Normalized: ' + str(self.norm) + ')')
        plt.plot(self.plot.x,self.plot.y,label=label,linewidth=0.8)
        plt.ylabel('Intensity Arbitrary Units')
        plt.xlabel('2θ')
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        plt.legend()
        plt.show()

    def plot_multiple_scale(self,label='',legend=True,offset=0,offset_ref=0,line=False,stack=False):
        from numpy import zeros
        if label!='':
            label=label
        else:
            label=self.plot.label
        plt.figure(figsize=(10, 6.5), dpi=100)
        if len(self.xrange) == 2 and type(self.xrange) == list:
            plt.xlim(self.xrange[0], self.xrange[1])
            plt.title(label + '(Normalized: ' + str(self.norm) + ')')
            plt.plot(self.plot.x,zeros(len(self.plot.x)),'k',alpha=0.1)
            plt.plot(self.plot.x,self.plot.y,label=self.plot.label,linewidth=0.8)
            if legend == False:
                plt.annotate(self.plot.label,(7,min(self.plot.y)+offset_ref),textcoords="offset points",xytext=(0,10),ha="center")
        for i,j in enumerate(self.plots):
            if stack:
                i=-1
            if line:
                import numpy as np
                y_line=np.zeros(len(j.y))
                y_line+=((i+1)*100)
                plt.plot(j.x,y_line,'k')
            if self.norm == True:
                y=j.y/max(j.y)*100+((i+1)*100)
                plt.ylabel('intensity A.U')
            else:
                plt.ylabel('counts')
            if i !='':
                plt.plot(j.x,y,label=j.label,alpha=0.8,linewidth=0.8)
                if legend == False:
                    label = j.label
                    plt.annotate(label,(7,offset+(i+1)*100),textcoords="offset points",xytext=(0,10),ha="center")

        #plt.ylabel('Intensity')
        plt.yticks([])
        plt.xlabel('2θ')
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        if legend:
            plt.legend()
        plt.show()
        return None
    
    def plot_single_only(self, label='',legend=True, offset=0,offset_ref=0):
        if label!='':
            label=label
        else:
            label=self.plot.label
        plt.figure(figsize=(10, 6.5), dpi=100)
        if len(self.xrange) == 2 and type(self.xrange) == list:
            plt.xlim(self.xrange[0], self.xrange[1])
            plt.title(label + '(Normalized: ' + str(self.norm) + ')')
            plt.plot(self.plot.x,self.plot.y,label=self.plot.label,linewidth=0.8)
            if legend == False:
                plt.annotate(self.plot.label,(7,min(self.plot.y)+offset_ref),textcoords="offset points",xytext=(0,10),ha="center")
        j=self.plots
        if self.norm == True:
            y=j.y/max(j.y)*100+((1)*100)
            plt.ylabel('intensity A.U')
        else:
            plt.ylabel('counts')
        if i !='':
            plt.plot(j.x,y,label=j.label,alpha=0.8,linewidth=0.8)
        if legend == False:
            label = j.label
            plt.annotate(label,(7,offset+(i+1)*100),textcoords="offset points",xytext=(0,10),ha="center")

        #plt.ylabel('Intensity')
        plt.ylim(0,)
        plt.yticks([])
        plt.xlabel('2θ')
        #plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        if legend:
            plt.legend()
        plt.show()
        return None

