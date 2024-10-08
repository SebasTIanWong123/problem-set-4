'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
def scatter_felony_vs_nonfelony(pred_universe):

    sns.lmplot(data=pred_universe, x='prediction_felony', y='prediction_nonfelony', hue='charge_degree')
    plt.savefig('./data/part5_plots/scatter_felony_vs_nonfelony.png', bbox_inches='tight')
    print('The group of dots, on the right side of the plot most likely can represent a person with high predictions for both nonfelony and felony rearrest.')
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
def scatter_felony_vs_actual_rearrest(pred_universe):

    sns.scatterplot(data=pred_universe, x='prediction_felony', y='actual_felony_rearrest')
    plt.savefig('./data/part5_plots/scatter_felony_vs_actual_rearrest.png', bbox_inches='tight')
    print('If the model is calibrated well, the scatter plot will show a clear connection between predicted and actual felony rearrest. If not, there could bne discrepancies.')
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?