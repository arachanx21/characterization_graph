import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt


class read_excel(object):
    def __init__(self,file,sheetname):
        self.file=file
        self.sheetname=sheetname
        self.dir=pd.read_excel(self.file,sheet_name=self.sheetname)
        self.temp=np.array(self.dir['Temp Cel'][1:])
        self.tg=np.array(self.dir['TG %'][1:])
        self.dta=np.array(self.dir['DTA uV/mg'][1:])
        self.dtg=np.array(self.dir['DTG %/Cel'][1:])

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

def plot_the_graph(tga,title,full_scale=False):
    """
    plot the tga result to graph
    input:
    tga a read excel class consisting tg-dta data such as temp in celcius,
    thermal gravimetric, differential thermal, differential gravimetric
    
    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    offset = 60
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right",
                                        axes=par2,
                                        offset=(offset, 0))

    par2.axis["right"].toggle(all=True)

    host.set_xlim(min(tga.temp), max(tga.temp))
    #host.set_ylim(0, 100)

    host.set_xlabel("Temperature")
    host.set_ylabel("%Mass")
    par1.set_ylabel("DTA uV/mg")
    par2.set_ylabel("DTG %/Cel")

    p1, = host.plot(tga.temp, tga.tg+100, label="Thermal Gravimetric")
    p2, = par1.plot(tga.temp, tga.dta, label="DTA uV/mg")
    p3, = par2.plot(tga.temp, tga.dtg, label="DTG %/Cel")

    par1.set_ylim(0, 4)
    par2.set_ylim(1, 65)

    host.legend()

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["left"].label.set_color(p2.get_color())
    par2.axis["right"].label.set_color(p3.get_color())

    plt.draw()
    plt.show()
"""

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    offset = 60
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right",
                                        axes=par2,
                                        offset=(offset, 0))

    par2.axis["right"].toggle(all=True)
    host.axis["left"].toggle(all=True)
    par1.axis["right"].toggle(all=True)

    host.set_xlabel("Temperature")
    host.set_ylabel("%Mass")
    par1.set_ylabel("DTA uV/mg")
    par2.set_ylabel("DTG %/Cel")

    if full_scale == True:
        plt.ylim(0,100)
    p1, = host.plot(tga.temp, tga.tg+100, label="Thermal Gravimetric")
    p2, = par1.plot(tga.temp, tga.dta, label="DTA")
    p3, = par2.plot(tga.temp, tga.dtg, label="DTG")

    host.legend()

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    par2.axis["right"].label.set_color(p3.get_color())
    plt.xlim(30,600)
    plt.title(title)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.075), shadow=True, ncol=3)
    plt.draw()
    plt.show()
    return None

def plot_one_only(x,y,x_name=None,y_name=None,xlim=[],title=None,ylim=[]):
    plt.plot(x,y,'k')
    plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    if xlim == [] or len(xlim)<2 or len(xlim)>2:
        pass
    else:
        plt.xlim(xlim)
    if ylim == [] or len(ylim)<2 or len(ylim)>2:
        pass
    else:
        plt.ylim(ylim)
    plt.grid()
    plt.show()
    return None

dmf=read_excel('/media/arachan/37E23CAE71B08C4E/research/Research Docs/MOF/experiment/TGDTA/ZIF 1-4 DMF.xlsx','Sheet4')
#plot_the_graph(dmf,'TG-DTA ZIF 1:4 DMF')
plot_one_only(dmf.temp,dmf.tg+100,x_name='Temperature ($^o$C)',y_name='%mass',xlim=[min(dmf.temp),max(dmf.temp)],ylim=[0,100])
#plt.plot(dmf.temp,dmf.tg)
#plt.xlim(30,600)
#plt.ylim(50,100)
#plt.show()
