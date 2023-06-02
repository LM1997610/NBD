

from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
from numpy import mean, sort, arange

class make_plots:

    def coeff_plot(ut_coeffs, c_ut_coeffs):

        fig, axarr = plt.subplots(1, 2, figsize=(13, 6))

        fig.suptitle('\n Utilization coefficients \n', fontsize=18)

        axarr[0].bar(range(64), ut_coeffs)
        axarr[0].set_ylim((0,1))
        axarr[0].grid(linewidth=0.4)
        axarr[0].set_xlabel('Server_ID', fontsize=13)
        axarr[0].set_ylabel('Utilization', fontsize=13)
        axarr[0].axhline(mean( ut_coeffs), color='r', linestyle=':')
        axarr[0].set_title("\nBaseline implementation\n", fontsize=16)

        axarr[1].bar(range(64), c_ut_coeffs, color='orange')
        axarr[1].set_ylim((0,1))
        axarr[1].grid(linewidth=0.4)
        axarr[1].set_xlabel('ServerID', fontsize=13)
        axarr[1].set_ylabel('Utilization', fontsize=13)
        axarr[1].axhline(mean(c_ut_coeffs), color='r', linestyle=':')
        axarr[1].set_title("\nCustom implementation\n", fontsize=16)

        fig.tight_layout(); 
        fig.subplots_adjust(top=0.65, wspace=0.40); 

        plt.show()


    def ECDF(data):
        x = sort(data)
        n = x.size
        y = arange(1, n+1) / n
        return(x,y)
    
    def ecdf_plot(b_r_t, c_r_t, bsd, csd):

        bq_t, bp_t = make_plots.ECDF(b_r_t)
        cq_t, cp_t = make_plots.ECDF(c_r_t)
        
        bq_s, bp_s = make_plots.ECDF(bsd)
        cq_s, cp_s = make_plots.ECDF(csd)
        
        fig, axarr = plt.subplots(1, 2, figsize=(13, 6))

        axarr[0].plot(bq_t, 1-bp_t, label='Baseline')
        axarr[0].plot(cq_t, 1-cp_t, label='Custom')
        axarr[0].set_xscale('log')
        axarr[0].set_xlabel('\nLog (job reponse time)', fontsize=13)
        axarr[0].set_ylabel('eCCDF\n', fontsize=13)
        axarr[0].grid(linewidth=0.4)
        axarr[0].legend()
        axarr[0].set_title("\nJob response time R\n", fontsize=16)
        
        axarr[1].plot(bq_s, 1-bp_s, label='Baseline')
        axarr[1].plot(cq_s, 1-cp_s, label='Custom')
        axarr[1].set_xscale('log')
        axarr[1].set_xlabel('\nLog (job slow down)', fontsize=13)
        axarr[1].set_ylabel('eCCDF\n', fontsize=13)
        axarr[1].grid(linewidth=0.4)
        axarr[1].legend()
        axarr[1].set_title("\nJob slowdown S\n", fontsize=16)
        
        fig.tight_layout(); 
        fig.subplots_adjust(top=1, wspace=0.50); 
            
        plt.show()