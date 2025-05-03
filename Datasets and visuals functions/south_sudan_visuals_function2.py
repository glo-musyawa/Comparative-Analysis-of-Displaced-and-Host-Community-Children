import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_pregnancy_rate_among_children(pregnancy_rate_among_children):
    """
    Plots a horizontal bar chart comparing pregnancy rates among children
    between Host community North and Refugees.

    Parameters:
        pregnancy_rate_among_children (dict): Nested dictionary with percentage strings for 'Yes' and 'No'.
    """
    

    # Categories in display order
    categories = ['No', 'Yes'][::-1]

    # Extract and reverse values
    host_values = [
        float(pregnancy_rate_among_children['Host community North']['No -----> (%)'].replace('%', '')),
        float(pregnancy_rate_among_children['Host community North']['Yes -----> (%)'].replace('%', '')),
    ][::-1]

    refugee_values = [
        float(pregnancy_rate_among_children['Refugees']['No -----> (%)'].replace('%', '')),
        float(pregnancy_rate_among_children['Refugees']['Yes -----> (%)'].replace('%', '')),
    ][::-1]

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    # Colors
    color_host = '#aec7e8'    # soft light blue
    color_refugee = '#1f77b4' # deep bold blue

    # Host Plot
    axes[0].barh(categories, host_values, color=color_host)
    axes[0].set_title('Host community North')
    axes[0].set_xlim(0, 100)
    axes[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[0].invert_yaxis()
    axes[0].xaxis.grid(True, linestyle='-', linewidth=0.2, color='gray')
    axes[0].set_axisbelow(True)

    # Refugee Plot
    axes[1].barh(categories, refugee_values, color=color_refugee)
    axes[1].set_title('Refugees')
    axes[1].set_xlim(0, 100)
    axes[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[1].invert_yaxis()
    axes[1].xaxis.grid(True, linestyle='-', linewidth=0.2, color='gray')
    axes[1].set_axisbelow(True)

    # Value labels
    for ax, values in zip(axes, [host_values, refugee_values]):
        for idx, value in enumerate(values):
            ax.annotate(f'{value:.1f}%',
                        xy=(value, idx),
                        xytext=(1, 0),
                        textcoords='offset points',
                        va='center',
                        ha='left',
                        color='black',
                        fontsize=9,
                        fontweight='bold')

    plt.tight_layout()
    plt.show()

def plot_children_marriage_rate(children_marriage_rate):
    """
    Plots a stacked horizontal bar chart showing marriage status among children
    in Host community North and Refugee groups.

    Parameters:
        children_marriage_rate (dict): Nested dictionary containing percentages for 'Married' and 'Never Married'.
    """

    # Categories and colors
    categories = ['Married', 'Never Married']
    colors = {
        'Married': '#152745',
        'Never Married': '#a8c4e3'
    }

    groups = ['Host community North', 'Refugees']
    group_data = {group: [] for group in groups}

    # Extract data
    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            val = float(children_marriage_rate[group].get(key, '0').replace('%', ''))
            group_data[group].append(val)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 4.5))
    y_pos = np.arange(len(groups))
    left = np.zeros(len(groups))
    bar_height = 0.2

    for i, cat in enumerate(categories):
        values = [group_data[group][i] for group in groups]
        ax.barh(y_pos, values, left=left, color=colors[cat], label=cat, height=bar_height)
        left += values

    # Aesthetics
    ax.set_yticks(y_pos)
    ax.set_yticklabels(groups, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlabel('Percentage (%)', fontsize=12)
    ax.set_xlim(0, 100)
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.45), ncol=2, frameon=False, fontsize=10)
    ax.set_facecolor('white')
    fig.patch.set_facecolor('white')
    ax.xaxis.grid(True, linestyle='-', alpha=0.1)

    plt.tight_layout()
    plt.savefig('Marriage Among children.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_female_children_marriage_rate(f_children_marriage_rate):
    """
    Plots a stacked horizontal bar chart showing marriage status among female children
    in Host community North and Refugee groups.

    Parameters:
        f_children_marriage_rate (dict): Nested dictionary containing percentages for 'Married' and 'Never Married'.
    """

    # Categories and their colors
    categories = ['Married', 'Never Married']
    colors = {
        'Married': '#152745',
        'Never Married': '#a8c4e3'
    }

    groups = ['Host community North', 'Refugees']
    group_data = {group: [] for group in groups}

    # Extract data
    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            val = float(f_children_marriage_rate[group].get(key, '0').replace('%', ''))
            group_data[group].append(val)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 4.5))
    y_pos = np.arange(len(groups))
    left = np.zeros(len(groups))
    bar_height = 0.2

    for i, cat in enumerate(categories):
        values = [group_data[group][i] for group in groups]
        ax.barh(y_pos, values, left=left, color=colors[cat], label=cat, height=bar_height)
        left += values

    # Aesthetics
    ax.set_yticks(y_pos)
    ax.set_yticklabels(groups, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlabel('Percentage (%)', fontsize=12)
    ax.set_xlim(0, 100)
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.45), ncol=2, frameon=False, fontsize=10)
    ax.set_facecolor('white')
    fig.patch.set_facecolor('white')
    ax.xaxis.grid(True, linestyle='-', alpha=0.1)

    # Additional label
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    fig.text(0.01, 0.03, 'Female children marriage rate', ha='left', va='bottom', fontsize=12, fontweight='bold')

    plt.savefig('1marriage among females.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_male_children_marriage_rate(m_children_marriage_rate):
    """
    Plots a stacked horizontal bar chart showing marriage status among male children
    in Host community North and Refugee groups.

    Parameters:
        m_children_marriage_rate (dict): Nested dictionary with percentages for 'Married' and 'Never Married'.
    """
    # Categories and colors
    categories = ['Married', 'Never Married']
    colors = {
        'Married': '#152745',
        'Never Married': '#a8c4e3'
    }

    groups = ['Host community North', 'Refugees']
    group_data = {group: [] for group in groups}

    # Extract data
    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            val = float(m_children_marriage_rate[group].get(key, '0').replace('%', ''))
            group_data[group].append(val)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 4.5))
    y_pos = np.arange(len(groups))
    left = np.zeros(len(groups))
    bar_height = 0.2

    for i, cat in enumerate(categories):
        values = [group_data[group][i] for group in groups]
        ax.barh(y_pos, values, left=left, color=colors[cat], label=cat, height=bar_height)
        left += values

    # Aesthetics
    ax.set_yticks(y_pos)
    ax.set_yticklabels(groups, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlabel('Percentage (%)', fontsize=12)
    ax.set_xlim(0, 100)
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.45), ncol=2, frameon=False, fontsize=10)
    ax.set_facecolor('white')
    fig.patch.set_facecolor('white')
    ax.xaxis.grid(True, linestyle='-', alpha=0.1)

    # Add annotation
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    fig.text(0.01, 0.03, 'Male children marriage rate', ha='left', va='bottom', fontsize=12, fontweight='bold')

    plt.savefig('1marriage among males.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_pre_school_attendance_dots(standard_pre_school_rate):
    """
    Plots a 10x10 dot grid for each group showing standard pre-school attendance rate.

    Parameters:
        standard_pre_school_rate (dict): Dictionary with 'Yes' and 'No' percentages for each group.
    """
    # Colors
    colors = {
        'Yes': '#a8c4e3',  # light blue
        'No': '#FFD700'    # Yellow
    }
    background_color = '#152745'  # Dark Blue background

    # Settings
    n_rows, n_cols = 10, 10
    groups = ['Host community North', 'Refugees']

    # Build figure
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.patch.set_facecolor(background_color)

    for idx, group in enumerate(groups):
        ax = axes[idx]
        ax.set_facecolor(background_color)

        # Extract values
        yes_pct = float(standard_pre_school_rate[group]['Yes -----> (%)'].replace('%', ''))
        no_pct = float(standard_pre_school_rate[group]['No -----> (%)'].replace('%', ''))

        yes_dots = int(round(yes_pct))
        no_dots = 100 - yes_dots

        # Create dot data
        data = ['Yes'] * yes_dots + ['No'] * no_dots
        data = np.array(data).reshape((n_rows, n_cols))

        for i in range(n_rows):
            for j in range(n_cols):
                color = colors[data[i, j]]
                ax.scatter(j, n_rows - i - 1, color=color, s=100, edgecolors='white', linewidth=0.5)

        ax.set_xlim(-0.5, n_cols - 0.5)
        ax.set_ylim(-0.5, n_rows - 0.5)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(group, fontsize=14, weight='bold', color='white')

    # Title and legend
    fig.suptitle('Standard Pre-School Attendance Rate', fontsize=18, weight='bold', color='white')
    legend_labels = ['Yes', 'No']
    custom_lines = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[label], markersize=10, markeredgecolor='white')
        for label in legend_labels
    ]
    fig.legend(custom_lines, legend_labels, loc='lower center', ncol=2, frameon=False, fontsize=12, labelcolor='white')

    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig('pre_school_attendance.png', dpi=300, bbox_inches='tight')
    plt.show()


def plot_extended_pre_school_attendance_dots(fds_pre_school_rate):
    """
    Plots a 10x10 dot grid visualization for extended pre-school attendance rate (ages 0–6)
    for each group in the provided data.

    Parameters:
        fds_pre_school_rate (dict): Dictionary with 'Yes' and 'No' percentages for each group.
    """

    # Colors
    colors = {
        'Yes': '#a8c4e3',  # light blue
        'No': '#FFD700'    # Yellow
    }
    background_color = '#152745'  # Dark Blue background

    # Settings
    n_rows, n_cols = 10, 10
    groups = ['Host community North', 'Refugees']

    # Build figure
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.patch.set_facecolor(background_color)

    for idx, group in enumerate(groups):
        ax = axes[idx]
        ax.set_facecolor(background_color)

        # Extract values
        yes_pct = float(fds_pre_school_rate[group]['Yes -----> (%)'].replace('%', ''))
        no_pct = float(fds_pre_school_rate[group]['No -----> (%)'].replace('%', ''))

        yes_dots = int(round(yes_pct))
        no_dots = 100 - yes_dots

        # Create grid
        data = ['Yes'] * yes_dots + ['No'] * no_dots
        data = np.array(data).reshape((n_rows, n_cols))

        for i in range(n_rows):
            for j in range(n_cols):
                color = colors[data[i, j]]
                ax.scatter(j, n_rows - i - 1, color=color, s=100, edgecolors='white', linewidth=0.5)

        ax.set_xlim(-0.5, n_cols - 0.5)
        ax.set_ylim(-0.5, n_rows - 0.5)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(group, fontsize=14, weight='bold', color='white')

    # Title and legend
    fig.suptitle('Extended Pre-School Attendance Rate (0–6)', fontsize=18, weight='bold', color='white')
    legend_labels = ['Yes', 'No']
    custom_lines = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[label], markersize=10, markeredgecolor='white')
        for label in legend_labels
    ]
    fig.legend(custom_lines, legend_labels, loc='lower center', ncol=2, frameon=False, fontsize=12, labelcolor='white')

    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig('extendend_attendance.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_school_attendance_rate(school_attendance_rate):
    """
    Plots stacked horizontal bar charts showing primary and secondary school attendance
    for different groups.

    Parameters:
        school_attendance_rate (dict): Dictionary where keys are group names and values are
            dicts with 'Yes -----> (%)' and 'No -----> (%)' attendance rates as strings.
    """

    # Prepare data
    groups = list(school_attendance_rate.keys())
    categories = ['No -----> (%)', 'Yes -----> (%)']  # Ensure order: No then Yes

    data = []
    for group in groups:
        values = [float(school_attendance_rate[group][cat].replace('%', '')) for cat in categories]
        data.append(values)

    # Plot settings
    bar_height = 0.2
    y_pos = np.arange(len(groups))
    fig, ax = plt.subplots(figsize=(8, 3))

    # Colors
    colors = ['#1f77b4', '#aec7e8']  # No = dark blue, Yes = light blue

    # Plot
    left = np.zeros(len(groups))
    for idx, category in enumerate(categories):
        values = [data[group_idx][idx] for group_idx in range(len(groups))]
        label = 'No' if 'No' in category else 'Yes'
        ax.barh(y_pos, values, left=left, height=bar_height, label=label, color=colors[idx])
        left += values

    # Decorate plot
    ax.set_yticks(y_pos)
    ax.set_yticklabels(groups)
    ax.set_xlim(0, 100)
    ax.set_xlabel('Primary and Secondary School Attendance Rate')
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Legend
    ax.legend(title='Response', loc='upper center', bbox_to_anchor=(0.5, 1.25),
              ncol=2, frameon=False)

    # Optional bottom text
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    fig.text(0.01, 0.03, 'School Attendance Rate', ha='left', va='bottom', fontsize=10, fontweight='bold')

    # Save and show
    plt.savefig('pri_sec_school_attendance.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_school_attendance_frequency(school_attendance_frequency):
    """
    Plots horizontal bar charts comparing frequency of school attendance
    between Host community and Refugees.

    Parameters:
        school_attendance_frequency (dict): Dictionary with keys 'Host community North' and 'Refugees',
            each containing two keys:
                - 'Most Of The Year -----> (%)'
                - "Less Than Most Of The Year Or Don'T Know -----> (%)"
    """
    # Categories and colors
    categories = ['Most Of The Year', "Less Than Most Of The Year Or Don'T Know"]
    categories = categories[::-1]  # Reverse for top-to-bottom plotting

    color_host = '#aec7e8'    # Soft light blue
    color_refugee = '#1f77b4' # Deep bold blue

    # Values
    host_values = [
        float(school_attendance_frequency['Host community North']['Most Of The Year -----> (%)'].replace('%', '')),
        float(school_attendance_frequency['Host community North']["Less Than Most Of The Year Or Don'T Know -----> (%)"].replace('%', '')),
    ][::-1]

    refugee_values = [
        float(school_attendance_frequency['Refugees']['Most Of The Year -----> (%)'].replace('%', '')),
        float(school_attendance_frequency['Refugees']["Less Than Most Of The Year Or Don'T Know -----> (%)"].replace('%', '')),
    ][::-1]

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

    # Host plot
    axes[0].barh(categories, host_values, color=color_host)
    axes[0].set_title('Host community North')
    axes[0].set_xlim(0, 100)
    axes[0].invert_yaxis()
    axes[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[0].xaxis.grid(True, linestyle='-', linewidth=0.1, color='gray')
    axes[0].set_axisbelow(True)

    # Refugee plot
    axes[1].barh(categories, refugee_values, color=color_refugee)
    axes[1].set_title('Refugees')
    axes[1].set_xlim(0, 100)
    axes[1].invert_yaxis()
    axes[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    axes[1].xaxis.grid(True, linestyle='-', linewidth=0.1, color='gray')
    axes[1].set_axisbelow(True)

    # Value annotations
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

    plt.tight_layout()
    plt.savefig('frequency_school_attendance.png', dpi=300, bbox_inches='tight')
    plt.show()




def plot_education_delay_rate(education_delay_rate):
    # Simplify category names and define colors
    categories = ['Advanced', 'No Delay', 'Delayed']
    colors = {
        'Advanced': '#152745',   # Dark blue
        'No Delay': '#ADD8E6',   # Light blue
        'Delayed': '#FFD700'     # Yellow
    }

    # Settings
    n_rows, n_cols = 10, 10
    groups = list(education_delay_rate.keys())

    # Create figure
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.patch.set_facecolor('#152745')

    for idx, group in enumerate(groups):
        ax = axes[idx]
        ax.set_facecolor('#152745')

        # Convert and round data
        values = education_delay_rate[group]
        counts = {
            cat: int(round(float(values[f'{cat} -----> (%)'].replace('%', ''))))
            for cat in categories
        }

        # Fix total dots = 100
        total = sum(counts.values())
        if total != 100:
            diff = 100 - total
            max_cat = max(counts, key=counts.get)
            counts[max_cat] += diff

        # Build data grid
        data = sum([[cat] * counts[cat] for cat in categories], [])
        data = np.array(data).reshape((n_rows, n_cols))

        # Plot dots
        for i in range(n_rows):
            for j in range(n_cols):
                label = data[i, j]
                ax.scatter(j, n_rows - i - 1, color=colors[label], s=100, edgecolors='white', linewidth=0.5)

        ax.set_xlim(-0.5, n_cols - 0.5)
        ax.set_ylim(-0.5, n_rows - 0.5)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(group, fontsize=14, weight='bold', color='white')

    # Main title
    fig.suptitle('Education Delay Rate', fontsize=18, weight='bold', color='white')

    # Legend
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[cat],
                   markeredgecolor='white', markersize=10)
        for cat in categories
    ]
    fig.legend(legend_elements, categories, loc='lower center', ncol=3, frameon=False, fontsize=12, labelcolor='white')

    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.show()


def plot_school_type_rate(school_type_rate):
    # Categories in order you want
    categories = [
        'Government Or Public',
        'Un Or Ngo',
        'Other: Specify',
        'Community',
        'Private',
        'Religious Or Faith-Based Organization'
    ]

    # Color mapping
    colors = {
        'Government Or Public': '#152745',
        'Un Or Ngo': '#0066b3',
        'Other: Specify': '#FFD700',
        'Community': '#00a89c',
        'Private': '#7cd2c2',
        'Religious Or Faith-Based Organization': '#a8c4e3'
    }

    # Groups
    groups = ['Host community North', 'Refugees']

    # Prepare data
    group_data = {group: [] for group in groups}

    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            if key in school_type_rate[group]:
                val = float(school_type_rate[group][key].replace('%', ''))
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
    ax.set_xlabel('Percentage (%)', fontsize=12)
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
    plt.show()



def plot_attendance_accepted_rate(attendance_n_accepted_rate):
    """
    This function generates a horizontal bar plot showing the percentages of 'Accepted' 
    and 'Not Accepted' for different groups (e.g., Refugees and Host community North).
    
    It expects a dictionary `attendance_n_accepted_rate` with the structure:
    - Keys are group names (e.g., 'Refugees', 'Host community North')
    - Values are dictionaries with keys 'Yes -----> (%)' and 'No -----> (%)' containing the corresponding percentages.
    
    Args:
    - attendance_n_accepted_rate (dict): Dictionary containing the attendance acceptance data.
    """
    
    # Process data
    group_labels = ['Refugees North', 'Host community North']
    values_yes = [
        float(attendance_n_accepted_rate['Refugees']['Yes -----> (%)'].replace('%', '')),
        float(attendance_n_accepted_rate['Host community North']['Yes -----> (%)'].replace('%', ''))
    ]
    values_no = [
        float(attendance_n_accepted_rate['Refugees']['No -----> (%)'].replace('%', '')),
        float(attendance_n_accepted_rate['Host community North']['No -----> (%)'].replace('%', ''))
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
    bars1 = ax.barh(y - height/2, values_yes, height, label='Accepted', color=deep_blue)
    bars2 = ax.barh(y + height/2, values_no, height, label='Not accepted', color=light_blue)

    # Labels
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

    # Add percentages **right at the end** of bars
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

    plt.tight_layout()
    plt.show()



def plot_top_reasons_for_not_attending_school(data):
    """
    This function generates a horizontal bar plot showing the top reasons for not attending school,
    grouped by different categories (e.g., Host community North and Refugees).
    
    The function takes a dictionary `data` where each key is a group name (e.g., 'Host community North', 'Refugees'),
    and the values are dictionaries where keys are reasons and the values are percentages (as strings with a '%' symbol).
    
    Args:
    - data (dict): Dictionary containing reasons for not attending school with corresponding percentages for each group.
    """
    
    # Convert percentage strings to floats
    for group in data:
        for reason in data[group]:
            data[group][reason] = float(data[group][reason].replace('%', ''))

    # Create dataframe
    df1 = pd.DataFrame(data).fillna(0)

    # Sort by total impact (optional)
    df1['Total'] = df1.sum(axis=1)
    df1 = df1.sort_values('Total', ascending=True)
    df1.drop(columns='Total', inplace=True)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 7))

    df1.plot(kind='barh', ax=ax, color=['#1f77b4', '#aec7e8'])  # dark and light blue
    ax.set_xlabel('Percentage (%)')
    ax.set_title('Top Reasons for Not Attending School (≥10%)')
    plt.legend(title='Group')
    plt.tight_layout()
    plt.show()



def plot_interruptions_rate(interruptions_rate):
    """
    This function generates a horizontal bar plot comparing the interruptions rate for different groups.
    
    It takes the dictionary `interruptions_rate` where each key represents a group (e.g., 'Refugees North', 'Host community North') 
    and the values are dictionaries with keys 'Yes -----> (%)' and 'No -----> (%)' indicating the percentages of interrupted and 
    non-interrupted attendance rates.

    Args:
    - interruptions_rate (dict): Dictionary containing groups as keys and their respective interruption rates as values.
    """
    
    # Process data
    group_labels = ['Refugees North', 'Host community North']
    values_yes = [
        float(interruptions_rate['Refugees']['Yes -----> (%)'].replace('%', '')),
        float(interruptions_rate['Host community North']['Yes -----> (%)'].replace('%', ''))
    ]
    values_no = [
        float(interruptions_rate['Refugees']['No -----> (%)'].replace('%', '')),
        float(interruptions_rate['Host community North']['No -----> (%)'].replace('%', ''))
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
    bars1 = ax.barh(y - height/2, values_yes, height, label='Interrupted', color=deep_blue)
    bars2 = ax.barh(y + height/2, values_no, height, label='Never Interrupted', color=light_blue)

    # Labels
    ax.set_xlabel('Percentage')
    ax.set_yticks(y)
    ax.set_yticklabels(group_labels)
    ax.set_xlim(0, 100)
    ax.invert_yaxis()  # Highest at top
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False)

    # Grid lines
    ax.xaxis.grid(True, linestyle='--', linewidth=0.1, color='gray')
    ax.set_axisbelow(True)

    # Add percentages **right at the end** of bars
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

    plt.tight_layout()
    plt.show()



def plot_school_interruption_reasons(host_reasons, refugee_reasons):
    """
    This function generates a horizontal bar plot comparing the top reasons for school interruption 
    between host communities and refugees based on the provided data.

    Args:
    - host_reasons (dict): A dictionary with reasons as keys and percentage values for host communities.
    - refugee_reasons (dict): A dictionary with reasons as keys and percentage values for refugees.
    """
    
    # Sorting and aligning categories
    categories = sorted(set(host_reasons) | set(refugee_reasons))
    host_values = [host_reasons.get(cat, 0) for cat in categories]
    refugee_values = [refugee_reasons.get(cat, 0) for cat in categories]

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_width = 0.4
    x = range(len(categories))

    ax.barh([i + bar_width/2 for i in x], host_values, height=bar_width, label='Host Community', color='#aec7e8')
    ax.barh([i - bar_width/2 for i in x], refugee_values, height=bar_width, label='Refugees', color='#1f77b4')

    # Labels and styling
    ax.set_xlabel('Percentage (%)')
    ax.set_title('Top Reasons for Last School Interruption')
    ax.set_yticks(x)
    ax.set_yticklabels(categories)
    ax.invert_yaxis()  # highest values on top
    ax.legend()
    plt.tight_layout()
    plt.show()



def plot_illiteracy_data(illiteracy_data):
    """
    This function generates a horizontal bar plot showing the percentage of illiteracy rates for 
    different groups, with labels indicating the exact percentage.

    Args:
    - illiteracy_data (dict): A dictionary where keys are group names and values are illiteracy percentages.
    """
    
    # Styling
    bar_color = '#1f77b4'  # blue
    labels = list(illiteracy_data.keys())
    values = list(illiteracy_data.values())

    # Plot
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.barh(labels, values, color=bar_color)

    # Add percentage labels on bars
    for bar in bars:
        width = bar.get_width()
        label_x = width - 5 if width > 10 else width + 1  # Inside if wide enough
        ax.text(label_x, bar.get_y() + bar.get_height()/2,
                f'{width:.1f}%', va='center', ha='right' if width > 10 else 'left',
                color='white' if width > 10 else 'black', fontsize=12, fontweight='bold')

    # Clean up axes
    ax.set_xlim(0, 105)
    ax.set_xticks([])  # No x-axis ticks
    ax.set_xlabel('')  # No axis label
    ax.set_title('Children Unable to Read or Write a Simple Text', fontsize=14, fontweight='bold')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_linewidth(0.8)
    ax.spines['bottom'].set_visible(False)
    ax.grid(False)

    plt.tight_layout()
    plt.show()



def plot_difficulty_seeing(difficulty_seeing_rate):
    """
    This function generates a stacked horizontal bar plot to show the difficulty levels of seeing 
    for different groups (e.g., Host community North, Refugees). It plots the percentage of people 
    in each group who experience 'No Difficulty', 'Some Difficulty', and 'A Lot Of Difficulty'.

    Args:
    - difficulty_seeing_rate (dict): A dictionary where keys are group names, and values are dictionaries 
                                      with categories as keys and percentage values as strings.
    """
    
    # Categories in order you want
    categories = [
        'No Difficulty',
        'Some Difficulty',
        'A Lot Of Difficulty'
    ]

    # Color mapping
    colors = {
        'No Difficulty': '#152745',
        'Some Difficulty': '#0066b3',
        'A Lot Of Difficulty': '#a8c4e3'
    }

    # Groups
    groups = ['Host community North', 'Refugees']

    # Prepare data
    group_data = {group: [] for group in groups}

    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            if key in difficulty_seeing_rate[group]:
                val = float(difficulty_seeing_rate[group][key].replace('%', ''))
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
    ax.set_xlabel('Percentage (%)', fontsize=12)
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
    plt.show()



def plot_difficulty_hearing(difficulty_hearing_rate):
    """
    This function generates a stacked horizontal bar plot to show the hearing difficulty levels 
    for different groups (e.g., Host community North, Refugees). It plots the percentage of people 
    in each group who experience 'No Difficulty', 'Some Difficulty', 'A Lot Of Difficulty', and 
    'Cannot Do At All'.

    Args:
    - difficulty_hearing_rate (dict): A dictionary where keys are group names, and values are dictionaries 
                                      with categories as keys and percentage values as strings.
    """
    
    # Categories in order you want
    categories = [
        'No Difficulty',
        'Some Difficulty',
        'A Lot Of Difficulty',
        'Cannot Do At All'
    ]

    # Color mapping
    colors = {
        'No Difficulty': '#152745',
        'Some Difficulty': '#0066b3',
        'A Lot Of Difficulty': '#a8c4e3',
        'Cannot Do At All' : '#00a89c'
    }

    # Groups
    groups = ['Host community North', 'Refugees']

    # Prepare data
    group_data = {group: [] for group in groups}

    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            if key in difficulty_hearing_rate[group]:
                val = float(difficulty_hearing_rate[group][key].replace('%', ''))
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
    ax.set_xlabel('Percentage (%)', fontsize=12)
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
    plt.show()



def plot_difficulty_walking(difficulty_walking_rate):
    """
    This function generates a stacked horizontal bar plot to show the walking difficulty levels 
    for different groups (e.g., Host community North, Refugees). It plots the percentage of people 
    in each group who experience 'No Difficulty', 'Some Difficulty', 'A Lot Of Difficulty', and 
    'Cannot Do At All'.

    Args:
    - difficulty_walking_rate (dict): A dictionary where keys are group names, and values are dictionaries 
                                      with categories as keys and percentage values as strings.
    """
    
    # Categories in order you want
    categories = [
        'No Difficulty',
        'Some Difficulty',
        'A Lot Of Difficulty',
        'Cannot Do At All'
    ]

    # Color mapping
    colors = {
        'No Difficulty': '#152745',
        'Some Difficulty': '#0066b3',
        'A Lot Of Difficulty': '#a8c4e3',
        'Cannot Do At All' : '#00a89c'
    }

    # Groups
    groups = ['Host community North', 'Refugees']

    # Prepare data
    group_data = {group: [] for group in groups}

    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            if key in difficulty_walking_rate[group]:
                val = float(difficulty_walking_rate[group][key].replace('%', ''))
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
    ax.set_xlabel('Percentage (%)', fontsize=12)
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
    plt.show()



def plot_difficulty_concentrating(difficulty_concentrating_rate):
    """
    This function generates a stacked horizontal bar plot to show the concentration difficulty levels 
    for different groups (e.g., Host community North, Refugees). It plots the percentage of people 
    in each group who experience 'No Difficulty', 'Some Difficulty', and 'A Lot Of Difficulty'.

    Args:
    - difficulty_concentrating_rate (dict): A dictionary where keys are group names, and values are dictionaries 
                                            with categories as keys and percentage values as strings.
    """
    
    # Categories in order you want
    categories = [
        'No Difficulty',
        'Some Difficulty',
        'A Lot Of Difficulty'
    ]

    # Color mapping
    colors = {
        'No Difficulty': '#152745',
        'Some Difficulty': '#0066b3',
        'A Lot Of Difficulty': '#a8c4e3'
    }

    # Groups
    groups = ['Host community North', 'Refugees']

    # Prepare data
    group_data = {group: [] for group in groups}

    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            if key in difficulty_concentrating_rate[group]:
                val = float(difficulty_concentrating_rate[group][key].replace('%', ''))
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
    ax.set_xlabel('Percentage (%)', fontsize=12)
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
    plt.show()



def plot_difficulty_selfcare(difficulty_selfcare_rate):
    """
    This function generates a stacked horizontal bar plot to show the self-care difficulty levels 
    for different groups (e.g., Host community North, Refugees). It plots the percentage of people 
    in each group who experience 'No Difficulty', 'Some Difficulty', 'A Lot Of Difficulty', 
    and 'Cannot Do At All' in self-care.

    Args:
    - difficulty_selfcare_rate (dict): A dictionary where keys are group names, and values are dictionaries 
                                        with categories as keys and percentage values as strings.
    """
    
    # Categories in order you want
    categories = [
        'No Difficulty',
        'Some Difficulty',
        'A Lot Of Difficulty',
        'Cannot Do At All'
    ]

    # Color mapping
    colors = {
        'No Difficulty': '#152745',
        'Some Difficulty': '#0066b3',
        'A Lot Of Difficulty': '#a8c4e3',
        'Cannot Do At All': '#00a89c'
    }

    # Groups
    groups = ['Host community North', 'Refugees']

    # Prepare data
    group_data = {group: [] for group in groups}

    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            if key in difficulty_selfcare_rate[group]:
                val = float(difficulty_selfcare_rate[group][key].replace('%', ''))
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
    ax.set_xlabel('Percentage (%)', fontsize=12)
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
    plt.show()



def plot_difficulty_communicating(difficulty_communicating_rate):
    """
    This function generates a stacked horizontal bar plot to show the difficulty levels in communication 
    for different groups (e.g., Host community North, Refugees). It plots the percentage of people 
    in each group who experience 'No Difficulty', 'Some Difficulty', 'A Lot Of Difficulty', 
    and 'Cannot Do At All' in communication.

    Args:
    - difficulty_communicating_rate (dict): A dictionary where keys are group names, and values are dictionaries 
                                              with categories as keys and percentage values as strings.
    """
    
    # Categories in order you want
    categories = [
        'No Difficulty',
        'Some Difficulty',
        'A Lot Of Difficulty',
        'Cannot Do At All'
    ]

    # Color mapping
    colors = {
        'No Difficulty': '#152745',
        'Some Difficulty': '#0066b3',
        'A Lot Of Difficulty': '#a8c4e3',
        'Cannot Do At All': '#00a89c'
    }

    # Groups
    groups = ['Host community North', 'Refugees']

    # Prepare data
    group_data = {group: [] for group in groups}

    for group in groups:
        for cat in categories:
            key = f'{cat} -----> (%)'
            if key in difficulty_communicating_rate[group]:
                val = float(difficulty_communicating_rate[group][key].replace('%', ''))
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
    ax.set_xlabel('Percentage (%)', fontsize=12)
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
    plt.show()
