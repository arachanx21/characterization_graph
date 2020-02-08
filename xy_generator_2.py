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
def generate_reference():
    reference_path = [
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulation/ZIF-1 VEJYEP.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulation/ZIF-1 VEJYEP01.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulation/ZIF-2 VEJYIT.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulation/ZIF-2 VEJYIT01.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulation/ZIF-3 VEJYOZ.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulation/ZIF-4 VEJYUF.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulaton2/ZIF-75 HIFVUO.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulaton2/ZIF-61 IMIDZB07.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulaton2/ZIF-61 IMIDZB01.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulaton2/ZIF-61 IMIDZB.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulaton2/ZIF-10 VEJZIU.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulaton2/ZIF-6 EQOCOC01.xy',
        # '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulaton2/TIF-4 EQOCOC01.xy',
        '/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/Pattern_simulaton2/TIF-4 EQOCOC.xy']
    reference_path_class=[]
    for i in reference_path:
        reference_path_class.append(xy_generator(i))
    return reference_path_class

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




hasil_experiment={'ZIF-4 DMF':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/124-agenda 175/0762xrd.xls','ZIF-4 DMF'],
'ZIF-4 H2O':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/124-agenda 175/0763xrd.xls','ZIF 1:4 H2O']}

hasil_experiment_new={'ZIF 1:1 DMF': ['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/170-agenda 236/0966 XRD.xls', 'ZIF 1:1 DMF'],\
                       'ZIF 1:4 DMF': ['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/170-agenda 236/0967 XRD.xls', 'ZIF 1:4 DMF II'],\
                      'ZIF 1:4 H2O':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/170-agenda 236/0968 XRD.xls','ZIF 1:4 H2O II']}
hasil_experiment_oktober={'ZIF 1:4':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/204-agenda 263/1065xrd.xls','ZIF 1:4 DMF III'],
                          'ZIF 1:11':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/204-agenda 263/1064xrd.xls','ZIF 1:11 DMF']}

hasil_experiment_november={'ZIF-coi':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1104xrd.xls','ZIF 1:4 DMF III Ac'],
                           'ZIF 1:4 DMF IV':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1105xrd.xls','ZIF 1:4 DMF IV'],
                           'ZIF 1:4 DMF IV Ac':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1106xrd.xls','ZIF 1:4 DMF IV Ac']}

hasil_experiment_november_2={'ZIF 1:4 DMF V Ac':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/236-agenda 299/1185xrd.xls','ZIF 1:4 DMF V Ac'],
                             'ZIF 1:4 DMF V':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/236-agenda 299/1186xrd.xls','ZIF 1:4 DMF V'],
                             'ZIF 1:4 Hyd III':['/media/arachan/37E23CAE71B08C4E/research/Resear ch Docs/MOF/experiment/XRD/236-agenda 299/1187xrd.xls','ZIF 1:4 H2O III']}
hasil_experiment_autoklaf_dmf={'ZIF 1:4 DMF III':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/204-agenda 263/1065xrd.xls','ZIF 1:4 DMF III'],
                                'ZIF-coi':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1104xrd.xls','ZIF 1:4 DMF III Ac']}
                                
hasil_experiment_dmf={'ZIF 1:4 DMF IV':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1105xrd.xls','ZIF 1:4 DMF IV'],
                    'ZIF 1:4 DMF IV Ac':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1106xrd.xls','ZIF 1:4 DMF IV Ac'],
                    'ZIF 1:4 DMF V Ac':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/236-agenda 299/1185xrd.xls','ZIF 1:4 DMF V Ac'],
                    'ZIF 1:4 DMF V':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/236-agenda 299/1186xrd.xls','ZIF 1:4 DMF V'],
                    'ZIF 1:4 DMF III':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/204-agenda 263/1065xrd.xls','ZIF 1:4 DMF III'],
                    'ZIF 1:4 DMF III Ac':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1104xrd.xls','ZIF 1:4 DMF III Ac']}

hasil_experiment_botol_schott={'ZIF 1:4 DMF IV':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1105xrd.xls','ZIF 1:4 DMF IV'],
                    'ZIF 1:4 DMF IV Ac':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1106xrd.xls','ZIF 1:4 DMF IV Ac'],
                    'ZIF 1:4 DMF V Ac':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/236-agenda 299/1185xrd.xls','ZIF 1:4 DMF V Ac'],
                    'ZIF 1:4 DMF V':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/236-agenda 299/1186xrd.xls','ZIF 1:4 DMF V'],
                              'ZIF 1:11':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/204-agenda 263/1064xrd.xls','ZIF 1:11 DMF']}

hasil_experiment_hydrothermal={'ZIF 1:4 H2O I':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/124-agenda 175/0763xrd.xls','ZIF 1:4 $H_2$O'],
                                'ZIF 1:4 H2O II':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/170-agenda 236/0968 XRD.xls','ZIF 1:4 $H_2$O II'],
                                'ZIF 1:4 H2O III':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/236-agenda 299/1187xrd.xls','ZIF 1:4 $H_2$O III']}

hasil_experiment_botol_schott_dmf_new={'ZIF 1:4 DMF IV':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1105xrd.xls','48 Jam'],
                           'ZIF 1:4 DMF IV Ac':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/218-agenda 275/1106xrd.xls','48 Jam, Pemanasan $80^o$C\n 2Jam'],
                           'ZIF 1:4 DMF V Ac':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/236-agenda 299/1185xrd.xls','24 Jam, Pemanasan $80^o$C\n 2Jam'],
                             'ZIF 1:4 DMF V':['/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/XRD/236-agenda 299/1186xrd.xls','24 Jam']}
import time

print("""

###      ##  ###### ######  ########
## ##    ##  ##     ##         ##
##  ##   ##  ###### ######     ##
##   ##  ##  ##     ##         ##
##      ###  ###### ######     ##   Enterprise
    --Growing Performance--
""")
for i in range(100):
    print('*',end=' ')
    time.sleep(0.05)

print("""
NEET Enterprise -- Software and Artificial Intelligence Division
(Powered by Python and its great open-source Scientific Packages)

XRD plot generator version 0.1.2 (November 2019)

Welcome!

Disclaimer: This software has no warranty against the result you got
from this software, you agree to any risk taken by using this software

Have a nice day!
""")
print('Initiating the references..')
references=generate_reference()
print("References generation completed.. ")
print('Have a nice day!')



test=False
if test:
    experiment_dict={}
    for i in hasil_experiment_dmf.keys():
        experiment_dict[i]=xy_generator(hasil_experiment_dmf[i][0],hasil_experiment_dmf[i][1])
    experiment_list=[]
    for i in experiment_dict.keys():
        experiment_list.append(experiment_dict[i])
    plot=plot_graphs(references[5],experiment_list,norm_a=True,xrange=[5,25])
    plot.plot_multiple_scale('Sintesis ZIF DMF')

