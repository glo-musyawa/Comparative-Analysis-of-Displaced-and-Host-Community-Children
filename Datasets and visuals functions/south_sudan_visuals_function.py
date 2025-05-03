import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def possession_of_immunization_cards(results):
    """
    Generates a horizontal bar chart visualizing the possession of immunization cards 
    among two groups: 'Refugees North' and 'Host community North'.

    Parameters:
    - results (dict): A dictionary containing percentage values (as strings with '%') 
                      for 'Yes -----> (%)' and 'No -----> (%)' responses for each group.

    The function processes the input data, reverses the order for top-down plotting, 
    and creates a grouped horizontal bar chart using customized colors and formatting.
    Percentage values are annotated at the end of each bar for clarity.

    The chart includes:
    - Labels for "Yes" and "No" responses
    - A percentage axis from 0% to 100%
    - Grid lines for better readability
    - Inverted y-axis for top-down layout
    - A title and legend placed below the chart

    No return value. The function displays the plot directly.
    """
    # Process data
    group_labels = ['Refugees North', 'Host community North']
    values_yes = [
        float(results['Refugees']['Yes -----> (%)'].replace('%', '')),
        float(results['Host community North']['Yes -----> (%)'].replace('%', ''))
    ]
    values_no = [
        float(results['Refugees']['No -----> (%)'].replace('%', '')),
        float(results['Host community North']['No -----> (%)'].replace('%', ''))
    ]

    # Reverse order for top-down
    values_yes = values_yes[::-1]
    values_no = values_no[::-1]
    group_labels = group_labels[::-1]

    # Plotting
    y = np.arange(len(group_labels))
    height = 0.35

    fig, ax = plt.subplots(figsize=(9, 5))

    # Custom premium colors
    deep_blue = '#1f77b4'    # Deep premium blue
    light_blue = '#aec7e8'   # Soft premium skyblue

    # Bars
    bars1 = ax.barh(y - height/2, values_yes, height, label='Yes', color=deep_blue)
    bars2 = ax.barh(y + height/2, values_no, height, label='No', color=light_blue)

    # Labels
    ax.set_title('Possession of Immunization Cards', loc='left')
    ax.set_xlabel('Percentage')
    ax.set_yticks(y)
    ax.set_yticklabels(group_labels)
    ax.set_xlim(0, 100)
    ax.invert_yaxis()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False)

    # Grid lines
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    ax.set_axisbelow(True)

    # Add percentages at the end of bars
    for bars in [bars1, bars2]:
        for bar in bars:
            width_bar = bar.get_width()
            ax.annotate(f'{width_bar:.1f}%',
                        xy=(width_bar, bar.get_y() + bar.get_height()/2),
                        xytext=(2, 0),
                        textcoords='offset points',
                        va='center',
                        ha='left',
                        color='black',
                        fontsize=9,
                        fontweight='bold')

    plt.tight_layout()
    plt.show()

def presented_immunization_cards(results_card_show):
    """
    Generates a horizontal bar chart visualizing whether individuals presented their 
    immunization cards to the interviewer among two groups: 'Refugees North' and 
    'Host community North'.

    Parameters:
    - results_card_show (dict): A dictionary containing percentage values (as strings with '%') 
                                for 'Yes -----> (%)' and 'No -----> (%)' responses for each group.

    The function processes the input data, reverses the order for top-down plotting, 
    and creates a grouped horizontal bar chart using customized colors and formatting.
    Percentage values are annotated at the end of each bar for clarity.

    The chart includes:
    - Labels for "Yes" and "No" responses
    - A percentage axis from 0% to 100%
    - Grid lines for better readability
    - Inverted y-axis for top-down layout
    - A title and legend placed below the chart

    No return value. The function displays the plot directly.
    """
    # Process data
    group_labels = ['Refugees North', 'Host community North']
    values_yes = [
        float(results_card_show['Refugees']['Yes -----> (%)'].replace('%', '')),
        float(results_card_show['Host community North']['Yes -----> (%)'].replace('%', ''))
    ]
    values_no = [
        float(results_card_show['Refugees']['No -----> (%)'].replace('%', '')),
        float(results_card_show['Host community North']['No -----> (%)'].replace('%', ''))
    ]

    # Reverse order for top-down
    values_yes = values_yes[::-1]
    values_no = values_no[::-1]
    group_labels = group_labels[::-1]

    # Plotting
    y = np.arange(len(group_labels))
    height = 0.35

    fig, ax = plt.subplots(figsize=(9, 5))

    # Custom premium colors
    deep_blue = '#1f77b4'    # Deep premium blue
    light_blue = '#aec7e8'   # Soft premium skyblue

    # Bars
    bars1 = ax.barh(y - height/2, values_yes, height, label='Yes', color=deep_blue)
    bars2 = ax.barh(y + height/2, values_no, height, label='No', color=light_blue)

    # Labels
    ax.set_title('Presented the Immunization Cards to Interviewer', loc='left')
    ax.set_xlabel('Percentage')
    ax.set_yticks(y)
    ax.set_yticklabels(group_labels)
    ax.set_xlim(0, 100)
    ax.invert_yaxis()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False)

    # Grid lines
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    ax.set_axisbelow(True)

    # Add percentages at the end of bars
    for bars in [bars1, bars2]:
        for bar in bars:
            width_bar = bar.get_width()
            ax.annotate(f'{width_bar:.1f}%',
                        xy=(width_bar, bar.get_y() + bar.get_height()/2),
                        xytext=(2, 0),
                        textcoords='offset points',
                        va='center',
                        ha='left',
                        color='black',
                        fontsize=9,
                        fontweight='bold')

    plt.tight_layout()
    plt.show()

def measles_vaccination_status(measles_vacc_coverage_rate1):
    """
    Creates side-by-side horizontal bar charts showing measles vaccination coverage rates 
    for two groups: 'Host community North' and 'Refugees'.

    Parameters:
    - measles_vacc_coverage_rate1 (dict): A dictionary containing percentage values (as strings with '%') 
      for 'Vaccinated -----> (%)' and 'Not Vaccinated -----> (%)' under each group.

    This function visualizes the proportion of vaccinated and not vaccinated individuals 
    per group using consistent color-coding and formatting. Values are annotated directly 
    on the bars for clarity.

    The chart includes:
    - Two subplots (Host Community and Refugees)
    - Horizontal bars for "Vaccinated" and "Not Vaccinated" responses
    - Grid lines for readability
    - Inverted y-axis for top-down presentation
    - Custom x-axis percentage formatting
    - Labels at the end of each bar
    - A title below the plots

    No return value. The function displays the plot directly.
    """
    # Categories
    categories = ['Vaccinated', 'Not Vaccinated']

    # Extract values
    host_values = [
        float(measles_vacc_coverage_rate1['Host community North']['Vaccinated -----> (%)'].replace('%', '')),
        float(measles_vacc_coverage_rate1['Host community North']['Not Vaccinated -----> (%)'].replace('%', '')),
    ]
    refugee_values = [
        float(measles_vacc_coverage_rate1['Refugees']['Vaccinated -----> (%)'].replace('%', '')),
        float(measles_vacc_coverage_rate1['Refugees']['Not Vaccinated -----> (%)'].replace('%', '')),
    ]

    # Reverse for top-down plotting
    categories = categories[::-1]
    host_values = host_values[::-1]
    refugee_values = refugee_values[::-1]

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

    # Custom premium colors
    color_host = '#aec7e8'    # soft light blue
    color_refugee = '#1f77b4' # deep bold blue

    # Host Community Plot
    axes[0].barh(categories, host_values, color=color_host)
    axes[0].set_title('Host community North')
    axes[0].set_xlim(0, 100)
    axes[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[0].invert_yaxis()
    axes[0].xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    axes[0].set_axisbelow(True)

    # Refugee Plot
    axes[1].barh(categories, refugee_values, color=color_refugee)
    axes[1].set_title('Refugees')
    axes[1].set_xlim(0, 100)
    axes[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[1].invert_yaxis()
    axes[1].xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    axes[1].set_axisbelow(True)

    # Add value labels at end of bars
    for ax, values in zip(axes, [host_values, refugee_values]):
        for idx, value in enumerate(values):
            ax.annotate(f'{value:.1f}%',
                        xy=(value, idx),
                        xytext=(2, 0),
                        textcoords='offset points',
                        va='center',
                        ha='left',
                        color='black',
                        fontsize=9,
                        fontweight='bold')

    # Common title at bottom
    fig.text(0.01, 0.03, 'Measles Vaccination Status', ha='left', va='bottom', fontsize=12, fontweight='bold')

    # Layout and show
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.show()

def full_measles_vaccination_status(full_vacc_measles_rate):
    """
    Creates side-by-side horizontal bar charts showing full, incomplete, and no measles vaccination 
    coverage for 'Host community North' and 'Refugees'.

    Parameters:
    - full_vacc_measles_rate (dict): A dictionary with nested dictionaries for each group containing 
      percentage strings (with '%' symbols) for:
        - 'Full_Vaccination -----> (%)'
        - 'Incomplete Vaccination -----> (%)'
        - 'Not Yet Vaccinated -----> (%)'

    The function visualizes these proportions as horizontal bars per group, displayed top-down in reverse order.
    Each bar is annotated with its value and color-coded for clarity.

    Features:
    - Two subplots: Host Community and Refugees
    - Categories: Full, Incomplete, and Not Vaccinated
    - Inverted y-axis for top-down hierarchy
    - Custom x-axis percentage formatting
    - Grid lines for readability
    - Inline value annotations
    - Shared y-axis between plots

    No return value. The function directly displays the plot.
    """
    # Categories
    categories = ['Full_Vaccination', 'Not Vaccinated', 'Incomplete Vaccination']

    # Extract values
    host_values = [
        float(full_vacc_measles_rate['Host community North']['Full_Vaccination -----> (%)'].replace('%', '')),
        float(full_vacc_measles_rate['Host community North']['Not Yet Vaccinated -----> (%)'].replace('%', '')),
        float(full_vacc_measles_rate['Host community North']['Incomplete Vaccination -----> (%)'].replace('%', ''))
    ]
    refugee_values = [
        float(full_vacc_measles_rate['Refugees']['Full_Vaccination -----> (%)'].replace('%', '')),
        float(full_vacc_measles_rate['Refugees']['Not Yet Vaccinated -----> (%)'].replace('%', '')),
        float(full_vacc_measles_rate['Refugees']['Incomplete Vaccination -----> (%)'].replace('%', ''))
    ]

    # Reverse for top-down plotting
    categories = categories[::-1]
    host_values = host_values[::-1]
    refugee_values = refugee_values[::-1]

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

    # Custom premium colors
    color_host = '#aec7e8'    # soft light blue
    color_refugee = '#1f77b4' # deep bold blue

    # Host Community Plot
    axes[0].barh(categories, host_values, color=color_host)
    axes[0].set_title('Host community North')
    axes[0].set_xlim(0, 100)
    axes[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[0].invert_yaxis()
    axes[0].xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    axes[0].set_axisbelow(True)

    # Refugee Plot
    axes[1].barh(categories, refugee_values, color=color_refugee)
    axes[1].set_title('Refugees')
    axes[1].set_xlim(0, 100)
    axes[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[1].invert_yaxis()
    axes[1].xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    axes[1].set_axisbelow(True)

    # Add value labels at end of bars
    for ax, values in zip(axes, [host_values, refugee_values]):
        for idx, value in enumerate(values):
            ax.annotate(f'{value:.1f}%',
                        xy=(value, idx),
                        xytext=(2, 0),
                        textcoords='offset points',
                        va='center',
                        ha='left',
                        color='black',
                        fontsize=9,
                        fontweight='bold')

    fig.text(0.01, 0.03, 'Full Measles Vaccination Status', ha='left', va='bottom', fontsize=12, fontweight='bold')

    # Layout and show
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.show()

def reasons_for_not_receiving_vaccine(results_no_vacc):
    """
    Creates side-by-side horizontal bar charts showing reasons for not receiving vaccines 
    among 'Host community North' and 'Refugees'.

    Parameters:
    - results_no_vacc (dict): A nested dictionary containing percentage strings (with '%' symbols) 
      for each barrier category under both groups:
        - 'Do Not Trust Vaccine -----> (%)'
        - 'Issue With Vaccine Staff -----> (%)'
        - 'No Information About Immunization Schedules -----> (%)'
        - 'No Time -----> (%)'
        - 'Other Reasons -----> (%)'
        - 'Service Unavailable -----> (%)'
        - 'Transportation Issue -----> (%)'

    Features:
    - Two subplots: Host Community and Refugees
    - Categories displayed in reverse for top-down alignment
    - Bars color-coded per group
    - Value annotations added at end of each bar
    - Grid lines for improved readability
    - Plot saved as high-resolution PNG

    No return value. Displays and saves the plot as 'Reasons for not receiving vaccine.png'.
    """
    # Categories
    categories = ['Do Not Trust Vaccine', 'Issue With Vaccine Staff', 'No Information About Immunization Schedules',
                  'No Time', 'Other Reasons', 'Service Unavailable', 'Transportation Issue']

    # Extract values
    host_values = [
        float(results_no_vacc['Host community North']['Do Not Trust Vaccine -----> (%)'].replace('%', '')),
        float(results_no_vacc['Host community North']['Issue With Vaccine Staff -----> (%)'].replace('%', '')),
        float(results_no_vacc['Host community North']['No Information About Immunization Schedules -----> (%)'].replace('%', '')),
        float(results_no_vacc['Host community North']['No Time -----> (%)'].replace('%', '')),
        float(results_no_vacc['Host community North']['Other Reasons -----> (%)'].replace('%', '')),
        float(results_no_vacc['Host community North']['Service Unavailable -----> (%)'].replace('%', '')),
        float(results_no_vacc['Host community North']['Transportation Issue -----> (%)'].replace('%', ''))
    ]
    refugee_values = [
        float(results_no_vacc['Refugees']['Do Not Trust Vaccine -----> (%)'].replace('%', '')),
        float(results_no_vacc['Refugees']['Issue With Vaccine Staff -----> (%)'].replace('%', '')),
        float(results_no_vacc['Refugees']['No Information About Immunization Schedules -----> (%)'].replace('%', '')),
        float(results_no_vacc['Refugees']['No Time -----> (%)'].replace('%', '')),
        float(results_no_vacc['Refugees']['Other Reasons -----> (%)'].replace('%', '')),
        float(results_no_vacc['Refugees']['Service Unavailable -----> (%)'].replace('%', '')),
        float(results_no_vacc['Refugees']['Transportation Issue -----> (%)'].replace('%', ''))
    ]

    # Reverse for top-down plotting
    categories = categories[::-1]
    host_values = host_values[::-1]
    refugee_values = refugee_values[::-1]

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

    # Custom premium colors
    color_host = '#aec7e8'    # soft light blue
    color_refugee = '#1f77b4' # deep bold blue

    # Host Community Plot
    axes[0].barh(categories, host_values, color=color_host)
    axes[0].set_title('Host community North')
    axes[0].set_xlim(0, 100)
    axes[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[0].invert_yaxis()
    axes[0].xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    axes[0].set_axisbelow(True)

    # Refugee Plot
    axes[1].barh(categories, refugee_values, color=color_refugee)
    axes[1].set_title('Refugees')
    axes[1].set_xlim(0, 100)
    axes[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[1].invert_yaxis()
    axes[1].xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    axes[1].set_axisbelow(True)

    # Add value labels at end of bars
    for ax, values in zip(axes, [host_values, refugee_values]):
        for idx, value in enumerate(values):
            ax.annotate(f'{value:.1f}%',
                        xy=(value, idx),
                        xytext=(2, 0),
                        textcoords='offset points',
                        va='center',
                        ha='left',
                        color='black',
                        fontsize=9,
                        fontweight='bold')

    fig.text(0.01, 0.03, 'Reasons for not receiving vaccine', ha='left', va='bottom', fontsize=10, fontweight='bold')

    # Layout and save
    plt.tight_layout()
    plt.savefig('Reasons for not receiving vaccine.png', dpi=300, bbox_inches='tight')
    plt.show()

def pentavalent_vaccination_status(pentavalent_vacc_coverage_rate):
    """
    Creates side-by-side horizontal bar charts to visualize the pentavalent vaccination status 
    for 'Host community North' and 'Refugees', showing the percentage of 'Vaccinated' vs. 
    'Not Vaccinated'.

    Parameters:
    - pentavalent_vacc_coverage_rate (dict): A nested dictionary containing vaccination percentages 
      for each group, where:
        - 'Vaccinated -----> (%)' and 'Not Vaccinated -----> (%)' are the keys to be processed for 
          'Host community North' and 'Refugees'.

    Features:
    - Two subplots: Host Community and Refugees
    - Categories displayed in reverse for top-down alignment
    - Bars color-coded per group
    - Value annotations added at end of each bar
    - Grid lines for improved readability
    - Plot saved as high-resolution PNG

    No return value. Displays and saves the plot as 'Pentavalent Vaccination Status.png'.
    """
    # Categories
    categories = ['Vaccinated', 'Not Vaccinated']

    # Extract values
    host_values = [
        float(pentavalent_vacc_coverage_rate['Host community North']['Vaccinated -----> (%)'].replace('%', '')),
        float(pentavalent_vacc_coverage_rate['Host community North']['Not Vaccinated -----> (%)'].replace('%', '')),
    ]
    refugee_values = [
        float(pentavalent_vacc_coverage_rate['Refugees']['Vaccinated -----> (%)'].replace('%', '')),
        float(pentavalent_vacc_coverage_rate['Refugees']['Not Vaccinated -----> (%)'].replace('%', '')),
    ]

    # Reverse for top-down plotting
    categories = categories[::-1]
    host_values = host_values[::-1]
    refugee_values = refugee_values[::-1]

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

    # Custom premium colors
    color_host = '#aec7e8'    # soft light blue
    color_refugee = '#1f77b4' # deep bold blue

    # Host Community Plot
    axes[0].barh(categories, host_values, color=color_host)
    axes[0].set_title('Host community North')
    axes[0].set_xlim(0, 100)
    axes[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[0].invert_yaxis()
    axes[0].xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    axes[0].set_axisbelow(True)

    # Refugee Plot
    axes[1].barh(categories, refugee_values, color=color_refugee)
    axes[1].set_title('Refugees')
    axes[1].set_xlim(0, 100)
    axes[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[1].invert_yaxis()
    axes[1].xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    axes[1].set_axisbelow(True)

    # Add value labels at end of bars
    for ax, values in zip(axes, [host_values, refugee_values]):
        for idx, value in enumerate(values):
            ax.annotate(f'{value:.1f}%',
                        xy=(value, idx),
                        xytext=(2, 0),
                        textcoords='offset points',
                        va='center',
                        ha='left',
                        color='black',
                        fontsize=9,
                        fontweight='bold')

    # Layout and save
    fig.text(0.01, 0.03, 'Pentavalent Vaccination Status', ha='left', va='bottom', fontsize=12, fontweight='bold')
    plt.tight_layout(rect=[0, 0.05, 1, 1])  # Leaves space at bottom
    plt.savefig('Pentavalent Vaccination Status.png', dpi=300, bbox_inches='tight')
    plt.show()

def full_pentavalent_vaccination_status(pentavalent_vacc_rate):
    """
    Creates side-by-side horizontal bar charts to visualize the full pentavalent vaccination status 
    (Four Doses vs. Three Doses) for 'Host community North' and 'Refugees'.

    Parameters:
    - pentavalent_vacc_rate (dict): A nested dictionary containing vaccination percentages for each 
      group, where:
        - 'Four Doses -----> (%)' and 'Three Doses -----> (%)' are the keys to be processed for 
          'Host community North' and 'Refugees'.

    Features:
    - Two subplots: Host Community and Refugees
    - Categories displayed in reverse for top-down alignment
    - Bars color-coded per group
    - Value annotations added at end of each bar
    - Grid lines for improved readability
    - Plot saved as high-resolution PNG

    No return value. Displays and saves the plot as 'Full Pentavalent Vaccination Status.png'.
    """
    # Categories
    categories = ['Four Doses', 'Three Doses']

    # Extract values
    host_values = [
        float(pentavalent_vacc_rate['Host community North']['Four Doses -----> (%)'].replace('%', '')),
        float(pentavalent_vacc_rate['Host community North']['Three Doses -----> (%)'].replace('%', '')),
    ]
    refugee_values = [
        float(pentavalent_vacc_rate['Refugees']['Four Doses -----> (%)'].replace('%', '')),
        float(pentavalent_vacc_rate['Refugees']['Three Doses -----> (%)'].replace('%', '')),
    ]

    # Reverse for top-down plotting
    categories = categories[::-1]
    host_values = host_values[::-1]
    refugee_values = refugee_values[::-1]

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

    # Custom premium colors
    color_host = '#aec7e8'    # soft light blue
    color_refugee = '#1f77b4' # deep bold blue

    # Host Community Plot
    axes[0].barh(categories, host_values, color=color_host)
    axes[0].set_title('Host community North')
    axes[0].set_xlim(0, 100)
    axes[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[0].invert_yaxis()
    axes[0].xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    axes[0].set_axisbelow(True)

    # Refugee Plot
    axes[1].barh(categories, refugee_values, color=color_refugee)
    axes[1].set_title('Refugees')
    axes[1].set_xlim(0, 100)
    axes[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[1].invert_yaxis()
    axes[1].xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    axes[1].set_axisbelow(True)

    # Add value labels at end of bars
    for ax, values in zip(axes, [host_values, refugee_values]):
        for idx, value in enumerate(values):
            ax.annotate(f'{value:.1f}%',
                        xy=(value, idx),
                        xytext=(2, 0),
                        textcoords='offset points',
                        va='center',
                        ha='left',
                        color='black',
                        fontsize=9,
                        fontweight='bold')

    # Layout and save
    fig.text(0.01, 0.03, 'Full Pentavalent Vaccination Status', ha='left', va='bottom', fontsize=10, fontweight='bold')
    plt.tight_layout(rect=[0, 0.05, 1, 1])  # Leaves space at bottom
    plt.savefig('Full Pentavalent Vaccination Status.png', dpi=300, bbox_inches='tight')
    plt.show()



def vitamin_a_supplementation(vitamin_a_coverage):
    """
    Creates a side-by-side horizontal bar chart to visualize Vitamin A supplementation status 
    ('Supplemented' vs. 'Not Supplemented') for 'Refugees North' and 'Host community North'.

    Parameters:
    - vitamin_a_coverage (dict): A nested dictionary containing Vitamin A supplementation percentages for 
      'Refugees North' and 'Host community North', where:
        - 'Supplemented -----> (%)' and 'Not Supplemented -----> (%)' are the keys to be processed.

    Features:
    - Two bars for each group, displaying 'Supplemented' vs. 'Not Supplemented' percentages.
    - Categories displayed in reverse order for top-down chart.
    - Value annotations added at the end of each bar.
    - Grid lines for readability.
    - Plot saved as high-resolution PNG.

    No return value. Displays and saves the plot as 'Vitamin A Supplementation.png'.
    """
    # Process data
    group_labels = ['Refugees North', 'Host community North']
    values_yes = [
        float(vitamin_a_coverage['Refugees']['Supplemented -----> (%)'].replace('%', '')),
        float(vitamin_a_coverage['Host community North']['Supplemented -----> (%)'].replace('%', ''))
    ]
    values_no = [
        float(vitamin_a_coverage['Refugees']['Not Supplemented -----> (%)'].replace('%', '')),
        float(vitamin_a_coverage['Host community North']['Not Supplemented -----> (%)'].replace('%', ''))
    ]

    # Reverse order for top-down
    values_yes = values_yes[::-1]
    values_no = values_no[::-1]
    group_labels = group_labels[::-1]

    # Plotting
    y = np.arange(len(group_labels))
    height = 0.35

    fig, ax = plt.subplots(figsize=(9, 5))

    # Custom premium colors
    deep_blue = '#1f77b4'    # Deep premium blue
    light_blue = '#aec7e8'   # Soft premium skyblue

    # Bars
    bars1 = ax.barh(y - height/2, values_yes, height, label='Supplemented', color=deep_blue)
    bars2 = ax.barh(y + height/2, values_no, height, label='Not Supplemented', color=light_blue)

    # Labels
    ax.set_title('Vitamin A Supplementation')
    ax.set_xlabel('Percentage')
    ax.set_yticks(y)
    ax.set_yticklabels(group_labels)
    ax.set_xlim(0, 100)
    ax.invert_yaxis()  # Highest at top
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False)

    # Grid lines
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
    ax.set_axisbelow(True)

    # Add percentages right at the end of bars
    for bars in [bars1, bars2]:
        for bar in bars:
            width_bar = bar.get_width()
            # Tiny nudge to right (only 1 or 2 pixels) to avoid overlapping the bar end
            ax.annotate(f'{width_bar:.1f}%',
                        xy=(width_bar, bar.get_y() + bar.get_height()/2),
                        xytext=(2, 0),   # Only 2 pixels to right
                        textcoords='offset points',
                        va='center',
                        ha='left',
                        color='black',
                        fontsize=9,
                        fontweight='bold')

    # Layout and save
    plt.tight_layout()
    plt.savefig('Vitamin A Supplementation.png', dpi=300, bbox_inches='tight')
    plt.show()




def dewormed_children_coverage(GI_coverage_rate):
    """
    Creates a stacked horizontal bar chart to visualize the percentage of dewormed children 
    in different groups ('Yes' vs. 'No') for each group in the GI_coverage_rate dictionary.

    Parameters:
    - GI_coverage_rate (dict): A dictionary where keys are group names (e.g., regions), 
      and values are dictionaries with keys 'No -----> (%)' and 'Yes -----> (%)', representing 
      the percentage of children not dewormed and dewormed in the past six months, respectively.

    Features:
    - Stacked bars to show the percentage of 'No' vs. 'Yes' for each group.
    - Value labels are not added for stacked bars due to the stacked nature.
    - Plot saved as a high-resolution PNG file.

    No return value. Displays and saves the plot as 'Dewormed Children in the Past Six Months.png'.
    """
    # Prepare data
    groups = list(GI_coverage_rate.keys())
    categories = ['No -----> (%)', 'Yes -----> (%)']

    data = []
    for group in groups:
        values = [float(GI_coverage_rate[group][cat].replace('%', '')) for cat in categories]
        data.append(values)

    # Setup plot
    bar_height = 0.2
    y_pos = np.arange(len(groups))
    fig, ax = plt.subplots(figsize=(8, 3))

    # Colors
    colors = ['#1f77b4', '#aec7e8']  # No = dark blue, Yes = light blue

    # Plot stacked bars
    left = np.zeros(len(groups))
    for idx, category in enumerate(categories):
        values = [data[group_idx][idx] for group_idx in range(len(groups))]
        label = 'No' if 'No' in category else 'Yes'
        ax.barh(y_pos, values, left=left, height=bar_height, label=label, color=colors[idx])
        left += values

    # Decorate
    ax.set_yticks(y_pos)
    ax.set_yticklabels(groups)
    ax.set_xlim(0, 100)
    ax.set_xlabel('% of Dewormed Children in the Past Six Months')
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Legend
    ax.legend(title='Response', loc='upper center', bbox_to_anchor=(0.5, 1.25),
              ncol=2, frameon=False)

    # Layout and save
    plt.tight_layout()
    plt.savefig('Dewormed Children in the Past Six Months.png', dpi=300, bbox_inches='tight')
    plt.show()



def reported_diarrhea_cases(health_issue_rate):
    """
    Creates a stacked horizontal bar chart to visualize the percentage of reported diarrhea 
    cases ('Yes' vs. 'No') in different groups (e.g., regions) based on the provided data.

    Parameters:
    - health_issue_rate (dict): A dictionary where keys are group names (e.g., regions), 
      and values are dictionaries with keys 'No -----> (%)' and 'Yes -----> (%)', representing 
      the percentage of children with reported diarrhea cases ('No' and 'Yes').

    Features:
    - Stacked bars to show the percentage of 'No' vs. 'Yes' for each group.
    - The plot is saved as a high-resolution PNG file.

    No return value. Displays and saves the plot as 'Reported Diarrhea Cases Among Under-5 Children Past 2 Weeks.png'.
    """
    # Prepare data
    groups = list(health_issue_rate.keys())
    categories = ['No -----> (%)', 'Yes -----> (%)']

    data = []
    for group in groups:
        values = [float(health_issue_rate[group][cat].replace('%', '')) for cat in categories]
        data.append(values)

    # Setup plot
    bar_height = 0.2
    y_pos = np.arange(len(groups))
    fig, ax = plt.subplots(figsize=(8, 3))

    # Colors
    colors = ['#1f77b4', '#aec7e8']  # No = dark blue, Yes = light blue

    # Plot stacked bars
    left = np.zeros(len(groups))
    for idx, category in enumerate(categories):
        values = [data[group_idx][idx] for group_idx in range(len(groups))]
        label = 'No' if 'No' in category else 'Yes'
        ax.barh(y_pos, values, left=left, height=bar_height, label=label, color=colors[idx])
        left += values

    # Decorate
    ax.set_yticks(y_pos)
    ax.set_yticklabels(groups)
    ax.set_xlabel('% of Reported Diarrhea Cases in the Past Two Weeks')
    ax.set_xlim(0, 100)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Legend
    ax.legend(title='Response', loc='upper center', bbox_to_anchor=(0.5, 1.25),
              ncol=2, frameon=False)

    # Layout and save
    plt.tight_layout()
    plt.savefig('Reported Diarrhea Cases Among Under-5 Children Past 2 Weeks.png', dpi=300, bbox_inches='tight')
    plt.show()




def treatment_approaches_for_diarrhea(diarrhea_treatment):
    """
    Creates a horizontal stacked bar chart to visualize the treatment approaches for diarrhea 
    among two groups (e.g., Host community and Refugees) based on the provided data.

    Parameters:
    - diarrhea_treatment (dict): A dictionary where keys are group names (e.g., 'Host community North', 'Refugees'),
      and values are dictionaries with keys representing treatment categories ('Partial Recommended Treatment', 'Home Remedy', etc.),
      and the corresponding percentage values for each category.

    Features:
    - Stacked bars for each group, with color-coded categories.
    - The plot is saved as a high-resolution PNG file.

    No return value. Displays and saves the plot as 'Treatment Approaches for Under-5 Children with Diarrhea.png'.
    """
    
    # Categories in order you want
    categories = [
        'Partial Recommended Treatment',
        'Home Remedy',
        'No Treatment',
        'Medical Intervention Only',
        'Unknown Treatment'
    ]

    # Color mapping
    colors = {
        'Partial Recommended Treatment': '#152745',  # Dark navy blue
        'Home Remedy': '#0066b3',                    # Blue
        'No Treatment': '#a8c4e3',                   # Light blue
        'Medical Intervention Only': '#00a89c',      # Same teal
        'Unknown Treatment': '#7cd2c2'               # Light teal (different from medical intervention)
    }

    # Groups
    groups = ['Host community North', 'Refugees']

    # Prepare data
    group_data = {group: [] for group in groups}

    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            if key in diarrhea_treatment[group]:
                val = float(diarrhea_treatment[group][key].replace('%', ''))
            else:
                val = 0.0  # If missing, assume 0
            group_data[group].append(val)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 4.5))  # Wide, not too tall

    y_pos = np.arange(len(groups))
    left = np.zeros(len(groups))
    bar_height = 0.2  # Thick bars

    for i, cat in enumerate(categories):
        values = [group_data[group][i] for group in groups]
        ax.barh(y_pos, values, left=left, color=colors[cat], label=cat, height=bar_height)
        left += values

    # Aesthetics
    ax.set_yticks(y_pos)
    ax.set_yticklabels(groups, fontsize=11)
    ax.invert_yaxis()  # Top to bottom order
    ax.set_xlabel('Treatment approach for the Diarrhea by %', fontsize=12)
    ax.set_xlim(0, 100)

    # Simple legend
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.45), ncol=2, frameon=False, fontsize=10)

    # Background and grid
    ax.set_facecolor('white')
    fig.patch.set_facecolor('white')
    ax.xaxis.grid(True, linestyle='-', alpha=0.1)

    # Layout
    plt.tight_layout()

    # Show plot
    plt.savefig('Treatment Approaches for Under-5 Children with Diarrhea.png', dpi=300, bbox_inches='tight')
    plt.show()

