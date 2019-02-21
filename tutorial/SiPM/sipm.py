import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Set path to current directory
PATH = os.getcwd()
#Set path to data directory
DATA = os.path.join(PATH,'data')
#Find data files
FILES = os.listdir(DATA)
#Make the directory for the plots
if not os.path.exists(os.path.join(PATH,'plots')):
    os.mkdir('plots')

#Define functions
def gauss(x,mu,sig,A):
    return A*np.exp(-(x-mu)**2/2/sig**2)
def bimodal(x,mu1,sig1,A1,mu2,sig2,A2):
    return gauss(x,mu1,sig1,A1)+gauss(x,mu2,sig2,A2)
def trimodal(x,mu1,sig1,A1,mu2,sig2,A2,mu3,sig3,A3):
    return gauss(x,mu1,sig1,A1)+gauss(x,mu2,sig2,A2)+gauss(x,mu3,sig3,A3)

#Set up dictionaries
data_dict={};volt_dict={};count_dict={};fit_dict={};fig_dict={};plot_dict={};tmp1=[];tmp2=[]
for files in FILES:
	if files[-6:-4] == 'mV':
		names = files[:-4]
		data_dict['%s'%names]=np.recfromtxt('%s'%os.path.join(DATA,files),dtype='float') 
		fig_dict['%s'%names],plot_dict['%s'%names]=plt.subplots(1,1,figsize=(12,6))
		for j in range(len(data_dict['%s'%names])-1):
			tmp1.append(data_dict['%s'%names][j+1][0])
			tmp2.append(data_dict['%s'%names][j+1][1])
			volt_dict['%s'%names]=tmp1
			count_dict['%s'%names]=tmp2
		tmp1=[]
		tmp2=[]
		try:
			fit_dict['fit_popt_%s'%names],fit_dict['fit_pcov_%s'%names]=curve_fit(bimodal,volt_dict['%s'%names],count_dict['%s'%names])#,sigma=np.sqrt(count_dict['count_%s'%i])+1)
			plot_dict['%s'%names].plot(volt_dict['%s'%names],bimodal(volt_dict['%s'%names],fit_dict['fit_popt_%s'%names][0],fit_dict['fit_popt_%s'%names][1],fit_dict['fit_popt_%s'%names][2],fit_dict['fit_popt_%s'%names][3],fit_dict['fit_popt_%s'%names][4],fit_dict['fit_popt_%s'%names][5]),'b--')
		except:
			print('\nthe first fit loop failed')
		plot_dict['%s'%names].errorbar(volt_dict['%s'%names],count_dict['%s'%names],np.sqrt(count_dict['%s'%names]),fmt='ro')
		plt.savefig('plots/plot_%s.png'%names)
	if files[-7:-4] == '_lt':
		names = files[:-4]
		print names
		data_dict['%s'%names]=np.recfromtxt('%s'%os.path.join(DATA,files),dtype='float') 
		fig_dict['%s'%names],plot_dict['%s'%names]=plt.subplots(1,1,figsize=(12,6))
		for j in range(len(data_dict['%s'%names])-1):
			tmp1.append(data_dict['%s'%names][j+1][0])
			tmp2.append(data_dict['%s'%names][j+1][1])
			volt_dict['%s'%names]=tmp1
			count_dict['%s'%names]=tmp2
		tmp1=[]
		tmp2=[]
		try:
			fit_dict['fit_popt_%s'%names],fit_dict['fit_pcov_%s'%names]=curve_fit(trimodal,volt_dict['%s'%names],count_dict['%s'%names])#,sigma=np.sqrt(count_dict['count_%s'%i])+1)
			plot_dict['%s'%names].plot(volt_dict['%s'%names],trimodal(volt_dict['%s'%names],fit_dict['fit_popt_%s'%names][0],fit_dict['fit_popt_%s'%names][1],fit_dict['fit_popt_%s'%names][2],fit_dict['fit_popt_%s'%names][3],fit_dict['fit_popt_%s'%names][4],fit_dict['fit_popt_%s'%names][5],fit_dict['fit_popt_%s'%names][6],fit_dict['fit_popt_%s'%names][7],fit_dict['fit_popt_%s'%names][8]),'b--')
		except:
			print('\nthe second fit loop failed')
			try:
				fit_dict['fit_popt_%s'%names],fit_dict['fit_pcov_%s'%names]=curve_fit(bimodal,volt_dict['%s'%names],count_dict['%s'%names])#,sigma=np.sqrt(count_dict['count_%s'%i])+1)
				plot_dict['%s'%names].plot(volt_dict['%s'%names],bimodal(volt_dict['%s'%names],fit_dict['fit_popt_%s'%names][0],fit_dict['fit_popt_%s'%names][1],fit_dict['fit_popt_%s'%names][2],fit_dict['fit_popt_%s'%names][3],fit_dict['fit_popt_%s'%names][4],fit_dict['fit_popt_%s'%names][5]),'b--')
			except:
				print('\nthe first fit loop failed')
		plot_dict['%s'%names].errorbar(volt_dict['%s'%names],count_dict['%s'%names],np.sqrt(count_dict['%s'%names]),fmt='ro')
		plt.savefig('%s/plots/plot_%s.png'%(PATH,names))



#plt.show()




















