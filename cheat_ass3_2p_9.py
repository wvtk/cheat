# Assignment 3.2P Solutions - 2023 Programming in Psychological Science
# Q9: repository
#
# Date         Programmer
# =========    ===============================
# 27-Jan-23    Wouke van 't Klooster (12146323)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def cheat(exercise):
    """This function prints the correct solution for the specified
    week 3 Python exercise (from the UvA's Programming in Psychological
    Science course). Input should be an integer from 1-4.
    """
    if exercise == 1:
        print(f"import numpy as np\n"
              "import matplotlib.pyplot as plt\n"
              "import seaborn as sns\n"
              "\n"
              "# Randomly distributed data between -10 and 10\n"
              "my_data = np.random.uniform(-10, 10, 100)\n"
              "\n"
              "# Boxplot of randomly distributed data\n"
              "plt.boxplot(my_data)\n"
              "plt.savefig('Q1_boxplot.png')\n"
              "plt.show()\n"
              "\n"
              "# Violinplot of jittered randomly distributed data\n"
              "sns.violinplot(my_data)\n"
              "sns.stripplot(data=my_data, color='black')\n"
              "plt.savefig('Q1_violinplot.png')\n"
              "plt.show()\n")
    elif exercise == 2:
        print(f"import matplotlib.pyplot as plt\n"
              "import pandas as pd\n"
              "\n"
              "URL = ('https://raw.githubusercontent.com/hannesrosenbusch/"
              "schiphol_class/master/titanic.csv')\n"
              "titanic = pd.read_csv(URL)\n"
              "\n"
              "# Count how many survived in each group\n"
              "titanic_grouped = titanic.groupby('Sex').sum()[['Survived']]\n"
              "# Count how many people there were in total in each group\n"
              "titanic_count = titanic.groupby('Sex').count()[['Survived']]\n"
              "# Merge these 2 dataframes\n"
              "titanic_survived = pd.merge(titanic_grouped, titanic_count,\n"
              "                            left_index=True, "
              "right_index=True)\n"
              "# Plot stacked barchart\n"
              "x_sex = titanic_survived.index.values\n"
              "y_total = titanic_survived.Survived_y\n"
              "y_survived = titanic_survived.Survived_x\n"
              "bar_total = plt.bar(x_sex, y_total)\n"
              "bar_survived = plt.bar(x_feature, y_survived)\n"
              "plt.xticks(x_sex, x_sex)\n"
              "plt.xlabel('Sex')\n"
              "plt.ylabel('Number of passengers')\n"
              "plt.title('Survivors by sex')\n"
              "plt.legend([bar_total, bar_survived], ['Died', 'Survived'])\n"
              "plt.savefig('Q2_titanic_barchart_class.png')\n"
              "plt.show()\n")
    elif exercise == 3:
        print(f"import numpy as np\n"
              "import matplotlib.pyplot as plt\n"
              "import seaborn as sns\n"
              "\n"
              "tips = sns.load_dataset('tips')\n"
              "\n"
              "# Scatterplot with LARGE font size\n"
              "total_bill = tips['total_bill']\n"
              "tip = tips['tip']\n"
              "plt.scatter(x=total_bill, y=tip)\n"
              "plt.xlabel('Total bill', fontsize=20)\n"
              "plt.ylabel('Tip', fontsize=20)\n"
              "\n"
              "# Add regression line to scatterplot\n"
              "polyfit = np.polyfit(total_bill, tip, deg=1)\n"
              "slope = polyfit[0]\n"
              "intercept = polyfit[1]\n"
              "plt.plot(total_bill, slope * total_bill + intercept, "
              "color='red')\n"
              "\n"
              "plt.savefig('Q3_tips_scatterplot.png')\n"
              "plt.show()\n")
    elif exercise == 4:
        print(f"import matplotlib.pyplot as plt\n"
              "import seaborn as sns\n"
              "\n"
              "diamonds = sns.load_dataset('diamonds')\n"
              "\n"
              "# common figure\n"
              "plt.figure(1, figsize=(13, 5))\n"
              "\n"
              "# subplot 1: heatmap\n"
              "plt.subplot(121)\n"
              "diamonds_subset = diamonds[\n"
              "   ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']]\n"
              "diamond_correlations = diamonds_subset.corr()\n"
              "sns.heatmap(diamond_correlations)\n"
              "plt.title('Correlations between all numeric diamond "
              "variables')\n"
              "\n"
              "# subplot 2: kdeplot\n"
              "plt.subplot(122)\n"
              "sns.kdeplot(diamonds, x='carat', y='price')\n"
              "plt.title('Distribution of carat and price observations ')\n"
              "\n"
              "plt.savefig('Q4_diamonds')\n"
              "plt.show()\n")
    elif exercise == 5 or exercise == 6 or exercise == 7 or exercise == 8 \
            or exercise == 9:
        print("Sorry, I can only give the answers for Q1-4.")
    else:
        print("Sorry, this exercise does not exist.")
