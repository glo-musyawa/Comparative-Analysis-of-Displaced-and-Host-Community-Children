import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch
import pandas as pd

def plot_gender_distribution(combined_df):
    """
    Plots the gender distribution by group using a custom color palette.
    
    Parameters:
    combined_df (DataFrame): A pandas DataFrame containing at least the columns 
                             'ind_gender' and 'group'.
                             
    The function creates a count plot grouped by 'group' with customized 
    aesthetics, including spines, bar labels, and title.
    """
    custom_palette = {'Host': '#46B4E7', 'Refugee': '#ff7e00'}

    plt.figure(figsize=(7, 4))
    ax = sns.countplot(data=combined_df, x='ind_gender', hue='group', palette=custom_palette, width=0.4)

    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_ylabel('Population Count')
    ax.set_xlabel('Gender')

    for spine_name, spine in ax.spines.items():
        if spine_name in ['left', 'bottom']:
            spine.set_visible(True)
            spine.set_color('#B0B0B0')
        else:
            spine.set_visible(False)

    ax.grid(False)

    for c in ax.containers:
        ax.bar_label(c, fmt='%d', label_type='edge', padding=-12, color='white')

    plt.title('Gender Distribution by Group', fontsize=15, fontweight='bold')
    plt.tight_layout(pad=2)
    plt.show()


def plot_age_distribution(combined_df):
    """
    Plots the age distribution by group using a custom color palette and defined age order.
    
    Parameters:
    combined_df (DataFrame): A pandas DataFrame containing at least the columns 
                             'ind_age' and 'group'.
                             
    The function creates a count plot grouped by 'group' and 'ind_age' with 
    customized appearance, labels, and title.
    """
    custom_palette = {'Host': '#46B4E7', 'Refugee': '#ff7e00'}
    age_order = ['0_4', '5_11', '12_17']

    plt.figure(figsize=(7, 5))
    ax = sns.countplot(
        data=combined_df,
        x='ind_age',
        hue='group',
        order=age_order,
        palette=custom_palette,
        width=0.5
    )

    plt.title('Age Distribution by Group', fontsize=14, fontweight='bold')
    plt.xlabel('Age Group')
    plt.ylabel('Count')

    for c in ax.containers:
        ax.bar_label(c, fmt='%d', label_type='edge', padding=-12, color='black')

    ax.grid(False)
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_ylabel('Population Count')
    ax.set_xlabel('Age Group')

    for spine_name, spine in ax.spines.items():
        if spine_name in ['left', 'bottom']:
            spine.set_visible(True)
            spine.set_color('#B0B0B0')
        else:
            spine.set_visible(False)

    plt.tight_layout(pad=2)
    plt.show()


def plot_marital_status_by_age(combined_df):
    """
    Plots marital status distribution by age group for Host and Refugee communities in side-by-side subplots.
    
    Parameters:
    combined_df (DataFrame): A pandas DataFrame containing the columns 'group', 'hh_marital', and 'ind_age'.
    
    The function creates two count plots (one for each group) using a consistent age-based color palette,
    and includes labeled bars, cleaned spines, and a shared layout.
    """
    age_palette = {
        '0_4': '#b0b0b0',
        '5_11': '#F6B366',
        '12_17': '#ff7e00'
    }

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

    sns.countplot(
        data=combined_df[combined_df['group'] == 'Host'],
        x='hh_marital',
        hue='ind_age',
        hue_order=['0_4', '5_11', '12_17'],
        palette=age_palette,
        ax=axes[0]
    )
    axes[0].set_title('Host Community', fontsize=10, fontweight='bold', color='Grey')
    axes[0].set_xlabel('Marital Status')
    axes[0].set_ylabel('Population Count')

    sns.countplot(
        data=combined_df[combined_df['group'] == 'Refugee'],
        x='hh_marital',
        hue='ind_age',
        hue_order=['0_4', '5_11', '12_17'],
        palette=age_palette,
        ax=axes[1]
    )
    axes[1].set_title('Refugee Community', fontsize=10, fontweight='bold', color='Grey')
    axes[1].set_xlabel('Marital Status')
    axes[1].set_ylabel('')

    for ax in axes:
        for container in ax.containers:
            ax.bar_label(container, fmt='%d', label_type='edge', padding=0, color='black')

        ax.set_yticks([])
        ax.set_yticklabels([])
        ax.grid(False)
        ax.set_ylabel('Count')

        for spine_name, spine in ax.spines.items():
            if spine_name in ['left', 'bottom']:
                spine.set_visible(True)
                spine.set_color('#B0B0B0')
            else:
                spine.set_visible(False)

    fig.subplots_adjust(wspace=0.1)
    plt.suptitle('Marital Status by Age Group: Host vs Refugee Communities', fontsize=15, fontweight='bold')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


def plot_employment_status_by_group(combined_df):
    """
    Plots the employment status distribution by group using a custom color palette.
    
    Parameters:
    combined_df (DataFrame): A pandas DataFrame containing the columns 
                             'currently_working_contributin_1' and 'group'.
                             
    The function generates a count plot to show employment status for Host and Refugee groups,
    with customized spines, hidden gridlines, and data labels on bars.
    """
    custom_palette = {'Host': '#46B4E7', 'Refugee': '#ff7e00'}

    plt.figure(figsize=(6, 4))
    ax = sns.countplot(
        data=combined_df,
        x='currently_working_contributin_1',
        hue='group',
        palette=custom_palette,
        width=0.5
    )

    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_ylabel('')
    ax.grid(False)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.spines['left'].set_visible(True)
    ax.spines['left'].set_color('#d3d3d3')
    ax.spines['bottom'].set_visible(True)
    ax.spines['bottom'].set_color('#d3d3d3')

    plt.title('Employment Status by Group', fontsize=18, fontweight='bold')
    plt.xlabel('Currently Working')
    plt.ylabel('Population Count')

    for c in ax.containers:
        ax.bar_label(c, fmt='%d', label_type='edge', padding=0, color='black')

    plt.tight_layout(pad=-3)
    plt.show()

def plot_formal_education_enrollment(combined_df):
    """
    Plots the formal education enrollment status by group.
    
    Parameters:
    combined_df (DataFrame): A pandas DataFrame containing the columns 
                             'formal_edu_enrollment' and 'group'.
                             
    The function creates a count plot showing enrollment in formal education
    for Host and Refugee groups with customized axes, spines, and bar labels.
    """
    plt.figure(figsize=(8, 6))
    ax = sns.countplot(data=combined_df, x='formal_edu_enrollment', hue='group', width=0.4)

    plt.title('Formal Education Enrollment by Group', fontsize=18)
    plt.xlabel('Formal Education Enrollment')
    plt.ylabel('Population Count')

    ax.set_yticklabels([])
    ax.tick_params(axis='y', length=0)

    ax.spines['left'].set_color('lightgrey')
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_linewidth(1)
    ax.spines['bottom'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for c in ax.containers:
        ax.bar_label(c, fmt='%d', label_type='edge', padding=0, color='black')

    plt.show()

def plot_nonformal_education_enrollment(combined_df):
    """
    Plots the non-formal education enrollment status by group.
    
    Parameters:
    combined_df (DataFrame): A pandas DataFrame containing the columns 
                             'nonformal_edu_enrollment' and 'group'.
                             
    The function creates a count plot showing enrollment in non-formal education
    for Host and Refugee groups with customized axes, spines, and bar labels.
    """
    plt.figure(figsize=(8, 6))
    ax = sns.countplot(data=combined_df, x='nonformal_edu_enrollment', hue='group', width=0.4)

    plt.title('Non-Formal Education Enrollment by Group', fontsize=18)
    plt.xlabel('Non-Formal Education Enrollment by Group')
    plt.ylabel('Population Count')

    ax.set_yticklabels([])
    ax.tick_params(axis='y', length=0)

    ax.spines['left'].set_color('lightgrey')
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_linewidth(1)
    ax.spines['bottom'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for c in ax.containers:
        ax.bar_label(c, fmt='%d', label_type='edge', padding=0, color='black')

    plt.show()

def plot_nonformal_education_by_gender(combined_df):
    """
    Plots non-formal education enrollment by gender using a custom color palette.
    
    Parameters:
    combined_df (DataFrame): A pandas DataFrame containing the columns 
                             'nonformal_edu_enrollment' and 'ind_gender'.
                             
    The function renames 'ind_gender' to 'Gender' for display, and produces a count plot
    with customized spines, bar labels, and a clean layout.
    """
    custom_palette = {'male': '#00689D', 'female': '#4AC7DD'}

    plt.figure(figsize=(8, 6))
    ax = sns.countplot(
        data=combined_df.rename(columns={'ind_gender': 'Gender'}),
        x='nonformal_edu_enrollment',
        hue='Gender',
        palette=custom_palette,
        width=0.5
    )

    plt.title('Non- Formal Education Enrollment by Gender', fontsize=18)
    plt.xlabel('Non-Formal Education Enrollment')
    plt.ylabel('Population Count')

    ax.set_yticklabels([])
    ax.tick_params(axis='y', length=0)

    ax.spines['left'].set_color('lightgrey')
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_linewidth(1)
    ax.spines['bottom'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for c in ax.containers:
        ax.bar_label(c, fmt='%d', label_type='edge', padding=0, color='black')

    plt.show()

def plot_education_enrollment_weighted():
    """
    Plots weighted percentages of formal education enrollment for the Host group 
    and non-formal education enrollment for the Refugee group in two side-by-side bar charts.

    The function uses hardcoded data for both Host (formal education) and Refugee 
    (non-formal education), with customized styling, colors, and a shared legend.
    """
    formal_data = pd.DataFrame({
        'group': ['yes', 'no'],
        'weighted_percentage': [86.08, 13.92]
    })

    nonformal_data = pd.DataFrame({
        'group': ['no', 'yes'],
        'weighted_percentage': [29.79, 70.16]
    })

    fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

    host_color = '#377eb8'
    refugee_color = '#ff7f00'

    axes[0].bar(formal_data['group'], formal_data['weighted_percentage'], color=host_color)
    axes[0].set_title('Formal Education Enrollment (Host)')
    axes[0].set_ylabel('Percentage')
    axes[0].set_ylim(0, 100)
    axes[0].grid(axis='y', linestyle='--', alpha=0.3)

    axes[1].bar(nonformal_data['group'], nonformal_data['weighted_percentage'], color=refugee_color)
    axes[1].set_title('Non-formal Education Enrollment (Refugee)')
    axes[1].set_ylim(0, 100)
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)

    legend_elements = [
        Patch(facecolor=host_color, label='Host'),
        Patch(facecolor=refugee_color, label='Refugee')
    ]
    fig.legend(handles=legend_elements, loc='lower center', ncol=2, frameon=False, fontsize=12)

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.show()

def plot_weighted_edu_enrollment(combined_df):
    """
    Plots the weighted percentage of education enrollment (Yes/No) by group (e.g., Host, Refugee).

    Parameters:
    combined_df (DataFrame): A pandas DataFrame containing the columns 'edu_enrollment', 
                             'group', and 'weights'. Assumes 'edu_enrollment' has values 
                             like 'Yes' or 'No' and requires normalization.

    The function filters relevant data, computes weighted percentages, and displays
    a side-by-side bar plot with labeled percentages, styled axes, and custom annotations.
    """
    combined_df['edu_enrollment'] = combined_df['edu_enrollment'].astype(str).str.strip().str.title()
    edu_df = combined_df[combined_df['edu_enrollment'].isin(['Yes', 'No'])]

    grouped_data = edu_df.groupby(['group', 'edu_enrollment'], as_index=False)['weights'].sum()

    total_weight_per_group = edu_df.groupby('group')['weights'].sum().reset_index()
    total_weight_per_group = total_weight_per_group.rename(columns={'weights': 'group_total_weight'})

    grouped_data = grouped_data.merge(total_weight_per_group, on='group')
    grouped_data['weighted_percentage'] = (grouped_data['weights'] / grouped_data['group_total_weight']) * 100

    plt.figure(figsize=(10, 6))
    palette = {'Yes': '#B2EC5D', 'No': '#94989c'}
    ax = sns.barplot(
        x='group',
        y='weighted_percentage',
        hue='edu_enrollment',
        width=0.5,
        data=grouped_data,
        palette=palette
    )

    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%', label_type='edge', padding=2, color='black')

    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(True)

    ax.set_xticks(range(len(grouped_data['group'].unique())))
    ax.set_xticklabels(grouped_data['group'].unique(), rotation=0)

    ax.set_yticks([])
    ax.set_xlabel("Group")
    ax.set_ylabel("Percentage")

    plt.title('Educational Enrollment Comparison: Host Communities vs Refugees', fontsize=16, pad=20)
    plt.text(
        0.5, 1.02,
        "Note: Only host communities access formal education; refugees receive non-formal education.",
        fontsize=10,
        color='gray',
        ha='center',
        transform=ax.transAxes
    )

    ax.spines['left'].set_color('lightgrey')
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_linewidth(1)
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.legend(title='Enrollment', loc='upper right', frameon=False)
    plt.subplots_adjust(top=0.85)
    plt.tight_layout()
    plt.show()


def plot_education_barriers(barrier_df):
    """
    This function creates a bar plot visualizing the education barriers faced by different groups (Host and Refugee)
    based on the weighted percentages.

    Parameters:
    barrier_df (pd.DataFrame): A DataFrame containing the barriers, their weighted percentages, and group information.
    """
    # Visualization
    plt.figure(figsize=(14, 8))
    ax = sns.barplot(
        data=barrier_df,
        x='weighted_percentage',
        y='barrier',
        hue='group',
        palette={'Host': '#1f77b4', 'Refugee': '#ff7f0e'}
    )

    # Add data labels INSIDE the bars
    for p in ax.patches:
        width = p.get_width()
        if width > 0:  # Only label bars with positive values
            ax.text(
                width + 0.04,  # Position label in the middle of the bar
                p.get_y() + p.get_height() / 2,  # Vertically center
                f'{width:.1f}%',  # Format: 1 decimal place
                ha='center',  # Horizontal alignment
                va='center',  # Vertical alignment
                color='black',  # Text color for visibility
                fontsize=10
            )

    # Title and axis labels
    plt.title('Education Barriers by Group', fontsize=16, pad=20)
    plt.xlabel('Percentage of Group Facing Barrier (%)', fontsize=12)
    plt.ylabel('Barrier Type', fontsize=12)

    # Customize the legend
    plt.legend(title='Population Group', frameon=False)

    # Adjust spines for cleaner look
    sns.despine(left=True, bottom=True)
    ax.grid(False)  # Remove grid lines

    # Display the plot
    plt.tight_layout()
    plt.show()



def plot_school_attendance_reasons(edu_barriers):
    """
    This function creates a horizontal bar plot showing the top reasons for not attending school, 
    with weighted percentages and data labels. The plot distinguishes between 'Host' and 'Refugee' groups.

    Parameters:
    edu_barriers (pd.DataFrame): A DataFrame containing the reasons, weighted percentages, and group information.
    """
    # Plotting with data labels
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(
        data=edu_barriers.sort_values('weighted_percentage', ascending=False),
        y='reason',
        x='weighted_percentage',
        hue='group',
        palette={'Host': '#1f77b4', 'Refugee': '#ff7f0e'},
        orient='h'
    )

    # Add data labels (placed just outside bars)
    for p in ax.patches:
        width = p.get_width()
        if width > 0:  # Only label bars with values
            ax.text(
                width + 0.5,  # Position 0.5% right of bar end
                p.get_y() + p.get_height()/2,  # Vertical center
                f'{width:.1f}%',
                ha='left',  # Left-align to stick to bar
                va='center',
                color='black',
                fontsize=10
            )

    # Adjust x-axis limit to fit labels
    ax.set_xlim(right=ax.get_xlim()[1] * 1.1)  # 10% padding

    # Titles and labels
    plt.title('Top Reasons for Not Attending School', fontsize=16)
    plt.xlabel('Percentage of Out-of-School Children (%)', fontsize=12)
    plt.ylabel('')

    # Customize the legend
    plt.legend(title='Population Group')

    # Clean up the plot
    sns.despine()
    plt.tight_layout()

    # Save and show the plot
    plt.savefig("not_attending_school_reasons.png")
    plt.show()



def plot_healthcare_need(combined_df):
    """
    This function creates a bar plot showing the percentage of individuals needing healthcare by group 
    with weighted percentages and data labels.

    Parameters:
    combined_df (pd.DataFrame): A DataFrame containing group, healthcare_needed, and weights columns.
    """
    # Custom color palette
    custom_palette = {'yes': '#B2EC5D', 'no': '#94989c'}

    # Rename column for clarity in legend
    combined_df = combined_df.rename(columns={'health_needed_healthcare': 'healthcare_needed'})

    # Calculate weighted % of people who needed healthcare per group
    healthcare_need = combined_df[combined_df['healthcare_needed'].notna()].groupby(['group', 'healthcare_needed']).apply(
        lambda x: x['weights'].sum()
    ).reset_index(name='weighted_count')

    # Get total weights for normalization
    totals = combined_df[combined_df['healthcare_needed'].notna()].groupby('group')['weights'].sum().to_dict()
    healthcare_need['weighted_percent'] = healthcare_need.apply(
        lambda row: (row['weighted_count'] / totals[row['group']]) * 100, axis=1
    )

    # Plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=healthcare_need,
        x='group',
        y='weighted_percent',
        hue='healthcare_needed',
        width=0.5,
        palette=custom_palette
    )

    # Remove top and right spines
    sns.despine()

    # Set axis line colors
    ax.spines['left'].set_color('grey')
    ax.spines['bottom'].set_color('grey')

    # Style ticks
    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', left=False, labelleft=False)  # Hides y-axis ticks and labels

    # Axis label colors
    ax.yaxis.label.set_color('grey')
    ax.xaxis.label.set_color('grey')

    # Bold title
    plt.title('Percentage of Individuals Needing Healthcare', color='black', fontsize=16 ,weight='bold')

    # Axis labels
    plt.ylabel('Weighted Percentage(%)')
    plt.xlabel('Group')

    # Add data labels on top of bars
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%', color='grey', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.savefig("needing_healthcare.png")
    plt.show()




def plot_healthcare_need_by_age_group(host_data, refugee_data, age_order):
    """
    This function plots healthcare need by age group for Host and Refugee populations.
    
    Parameters:
    host_data (pd.DataFrame): DataFrame for the Host population.
    refugee_data (pd.DataFrame): DataFrame for the Refugee population.
    age_order (list): The order of the age groups to be displayed on the x-axis.
    """
    custom_palette = {'yes': '#B2EC5D', 'no': '#94989c'}

    # Set up subplots
    fig, axes = plt.subplots(1, 2, figsize=(18, 7), sharey=True)
    fig.suptitle('Healthcare Need by Age Group for Host and Refugee Populations', fontsize=18, weight='bold', color='black', y=1.05)

    # Plot Host Population
    sns.barplot(
        data=host_data,
        x='ind_age',
        y='weighted_percent',
        hue='healthcare_needed',
        palette=custom_palette,
        ax=axes[0],
        order=age_order
    )
    axes[0].set_title('Host Population', fontsize=16, weight='bold', color='black')
    axes[0].set_xlabel('Age Group', fontsize=12)
    axes[0].set_ylabel('Weighted Percentage (%)', fontsize=12)

    # Plot Refugee Population
    sns.barplot(
        data=refugee_data,
        x='ind_age',
        y='weighted_percent',
        hue='healthcare_needed',
        palette=custom_palette,
        ax=axes[1],
        order=age_order
    )
    axes[1].set_title('Refugee Population', fontsize=16, weight='bold', color='black')
    axes[1].set_xlabel('Age Group', fontsize=12)
    axes[1].set_ylabel('')  # No duplicate y-label on the second plot

    # Clean up both plots
    for ax in axes:
        sns.despine(ax=ax)
        ax.spines['left'].set_color('grey')
        ax.spines['bottom'].set_color('grey')
        ax.tick_params(axis='x', rotation=45, colors='black')
        ax.tick_params(axis='y', left=False, labelleft=False)  # Hide y-axis ticks and labels
        ax.yaxis.label.set_color('black')
        ax.xaxis.label.set_color('black')

        # Add data labels inside the bars
        for container in ax.containers:
            ax.bar_label(container, fmt='%.1f%%', label_type='edge', padding=-20, color='black', fontsize=12, weight='bold')

    # Legend
    axes[1].legend(title='Healthcare Needed', loc='upper right')
    axes[0].legend().set_visible(False)  # Only one legend on the right

    # Adjust layout and save plot
    plt.tight_layout()
    plt.savefig("needing_healthcare_by_age.png")
    plt.show()




def plot_healthcare_received(received_summary):
    """
    This function plots the weighted percentage of healthcare received by group.
    
    Parameters:
    received_summary (pd.DataFrame): DataFrame containing the summary data for healthcare received by group.
    """
    custom_palette = {'Yes': '#B2EC5D', 'No': '#94989c'}

    # Plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=received_summary,
        x='group',
        y='weighted_percent',
        palette=custom_palette,
        width=0.5,
        hue='health_received_healthcare'
    )

    # Add data labels
    for p in ax.patches:
        height = p.get_height()
        if not pd.isna(height) and height > 0:
            ax.annotate(f'{height:.1f}%',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom',
                        fontsize=9, color='black',
                        xytext=(0, 3),
                        textcoords='offset points')

    # Customize plot appearance
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('grey')
    ax.spines['bottom'].set_color('grey')

    # Set title and labels
    plt.title('Healthcare Received by Group', weight='bold')
    plt.ylabel('Weighted Percentage')
    plt.xlabel('Group')

    # Show legend
    plt.legend(title='Received Healthcare')

    # Adjust layout and save the plot
    plt.tight_layout()
    plt.savefig("received_healthcare.png")
    plt.show()




def plot_healthcare_received_by_age_group(host_data, refugee_data):
    """
    This function plots healthcare received by age group for both host and refugee populations.
    
    Parameters:
    host_data (pd.DataFrame): Data for the host population, with columns 'ind_age', 'health_received', and 'weighted_percent'.
    refugee_data (pd.DataFrame): Data for the refugee population, with columns 'ind_age', 'health_received', and 'weighted_percent'.
    """
    # Custom color palette
    custom_palette = {'yes': '#B2EC5D', 'no': '#94989c', 'dont_know': 'black'}

    # Set up subplots
    fig, axes = plt.subplots(1, 2, figsize=(18, 7), sharey=True)
    fig.suptitle('Healthcare Received by Age Group for Host and Refugee Populations', fontsize=18, weight='bold', color='black', y=1.05)

    # Plot Host
    sns.barplot(
        data=host_data,
        x='ind_age',
        y='weighted_percent',
        hue='health_received',
        palette=custom_palette,
        ax=axes[0]
    )

    axes[0].set_title('Host Population', fontsize=16, weight='bold', color='black')
    axes[0].set_xlabel('Age Group', fontsize=12)
    axes[0].set_ylabel('Weighted Percentage (%)', fontsize=12)

    # Plot Refugee
    sns.barplot(
        data=refugee_data,
        x='ind_age',
        y='weighted_percent',
        hue='health_received',
        palette=custom_palette,
        ax=axes[1]
    )

    axes[1].set_title('Refugee Population', fontsize=16, weight='bold', color='black')
    axes[1].set_xlabel('Age Group', fontsize=12)
    axes[1].set_ylabel('')  # No duplicate y-label on the second plot

    # Clean up both plots
    for ax in axes:
        # Set spines (axis lines) to faint grey
        ax.spines['left'].set_color('lightgrey')
        ax.spines['bottom'].set_color('lightgrey')
        ax.spines['right'].set_color('lightgrey')
        ax.spines['top'].set_color('lightgrey')

        # Set tick marks to black for better visibility
        ax.tick_params(axis='x', rotation=45, colors='black')
        ax.tick_params(axis='y', colors='black')  # Set y-axis ticks to black

        # Remove y-axis ticks and labels for a clean look
        ax.set_yticks([])  # Remove y-axis ticks
        ax.set_yticklabels([])  # Remove y-axis labels

        # Keep axis labels black
        ax.yaxis.label.set_color('black')
        ax.xaxis.label.set_color('black')

        # Add data labels inside the bars
        for container in ax.containers:
            ax.bar_label(container, fmt='%.1f%%', label_type='edge', padding=0, color='black', fontsize=12, weight='bold')

    # Adjust the legend position to avoid overlap
    axes[1].legend(title='Received Healthcare', loc='upper left', bbox_to_anchor=(1, 1))
    axes[0].legend().set_visible(False)  # Only one legend on the right

    # Adjust the layout to prevent overlap and make space for the legend
    plt.tight_layout(rect=[0, 0, 0.9, 1])  # Make space on the right for the legend
    plt.savefig("received_healthcare_by_group.png")
    plt.show()



def plot_treatment_types(treatment_summary):
    """
    This function plots the types of treatment needed by group, with percentage labels inside the bars.

    Parameters:
    treatment_summary (pd.DataFrame): DataFrame containing 'treatment_type', 'weighted_percent', and 'group' columns.
    """
    # Plot
    plt.figure(figsize=(14, 6))
    ax = sns.barplot(data=treatment_summary, x='treatment_type', y='weighted_percent', hue='group')

    # Add percentage labels inside bars
    for container in ax.containers:
        ax.bar_label(container, labels=[f'{v:.1f}%' for v in container.datavalues], label_type='edge', padding=0, color='black', fontsize=9)

    # Customize title (larger and bold)
    plt.title('Types of Treatment Needed by Group', fontsize=18, fontweight='bold')

    # Axis customizations
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('grey')
    ax.spines['bottom'].set_color('grey')

    # Hide y-tick values but keep label
    ax.set_yticks([])  # Remove tick marks and numbers
    ax.set_ylabel('Weighted Percentage', fontsize=12)
    ax.set_xlabel('Treatment Type', fontsize=12)

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("treatment_type.png")
    plt.show()



def plot_maternal_healthcare(maternal_melted):
    """
    Plots maternal healthcare needs for adolescents aged 12–17.

    Parameters:
    maternal_melted (pd.DataFrame): DataFrame with columns ['Care Type', 'Percentage', 'group']
    """
    # Color palette with good contrast
    color_palette = sns.color_palette("coolwarm", n_colors=2)

    # Plot
    plt.figure(figsize=(8, 4))
    ax = sns.barplot(
        x='Care Type', y='Percentage', hue='group',
        data=maternal_melted,
        palette=color_palette
    )

    # Add percentage labels
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%', padding=5, fontsize=12, fontweight='bold', color='black')

    # Style adjustments
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_alpha(0.5)
    ax.spines['bottom'].set_alpha(0.5)
    ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)

    # Titles and labels
    plt.title('Maternal Healthcare Needs (Ages 12–17)', fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('Percentage Needing Care (%)', fontsize=12, alpha=0.7)
    plt.xlabel('')
    plt.xticks([0, 1], ['Antenatal Care', 'Safe Delivery'], fontsize=12, fontweight='bold')
    plt.legend(title='Community', frameon=False, fontsize=12, loc='upper left')

    plt.tight_layout()
    plt.show()


def plot_healthcare_services(service_df):
    """
    Plots a horizontal bar chart showing the percentage of healthcare services needed by group.

    Parameters:
    - service_df (DataFrame): A pandas DataFrame containing the columns 'percentage', 'service', and 'group'.

    Saves:
    - A PNG file named 'healthcare services.png'.
    """
    plt.figure(figsize=(12, 7))
    ax = sns.barplot(data=service_df, x='percentage', y='service', hue='group')

    # Add data labels
    for container in ax.containers:
        ax.bar_label(container, label_type='edge', padding=3, fmt='%.1f%%')

    plt.title("Types of Healthcare Services Needed by Group")
    plt.xlabel("Percentage (%)")
    plt.ylabel("Healthcare Service")

    # Move legend inside, lower right
    ax.legend(loc='lower right', frameon=True)

    plt.tight_layout()
    plt.savefig("healthcare services.png")
    plt.show()
