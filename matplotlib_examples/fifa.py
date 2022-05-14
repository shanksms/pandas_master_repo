import matplotlib.pyplot as plt
import pandas as pd


class Fifa:
    def __init__(self):
        self.fifa_df = pd.read_csv('fifa.csv')
        self.fifa_df.loc[:, 'Weight'] = self.fifa_df.loc[:, 'Weight'].str.replace('lbs', '')

    def get_fifa_df(self):
        return self.fifa_df


def hist_plot(fifa_df: pd.DataFrame):
    bins = [40, 50, 60, 70, 80, 90, 100]
    plt.hist(fifa_df['Overall'])
    plt.xticks(bins)
    plt.xlabel('SkillLevel')
    plt.ylabel('Number Of Players')
    plt.title('Distribution of Player Skills in Fifa 2018')
    plt.show()


def pie_plot_foot_preference(fifa_df: pd.DataFrame):
    left = fifa_df.loc[fifa_df['Preferred Foot'] == 'Left', :].shape[0]
    right = fifa_df.loc[fifa_df['Preferred Foot'] == 'Right', :].shape[0]
    labels = ['Left', 'Right']
    colors = ['#42d1f5', '#f5425d']
    plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f %%')
    plt.title('Foot preference of Fifa players')
    plt.show()



if __name__ == '__main__':
    fifa_df = Fifa().get_fifa_df()
    hist_plot(fifa_df)
    pie_plot_foot_preference(fifa_df)

