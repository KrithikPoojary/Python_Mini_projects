'''"""
IPL 2022 Capstone Project
=========================
The Indian Premier League (IPL) is a professional T20 cricket league in
India, featuring franchises representing cities. This script explores
IPL 2022 match-level data to derive meaningful insights and understand
match outcomes, player performances, and team dynamics.
'''


# ---------------------------------------------------------------------------
# 1. Loading the libraries and the dataset
# ---------------------------------------------------------------------------
# numpy/pandas handle the number-crunching and tabular data, seaborn/matplotlib
# handle the visuals, and we silence warnings so the output stays readable.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# Load the raw IPL match data from the CSV file sitting alongside this script.
df = pd.read_csv("IPL.csv")

# Peek at the first few rows just to sanity-check that everything loaded fine.
print("First 5 rows of the dataset:")
print(df.head())


# ---------------------------------------------------------------------------
# 2. Basic information about the dataset
# ---------------------------------------------------------------------------
# df.info() gives us column names, data types, and non-null counts in one shot.
print("\nDataset info:")
df.info()

# How big is this dataset, really? Rows = matches, columns = features per match.
print(f"\nyour rows are {df.shape[0]} and your columns are {df.shape[1]}")

# Are there any gaps in the data we should be aware of before analyzing?
print("\nNull values per column:")
print(df.isnull().sum())


# ---------------------------------------------------------------------------
# 3. Basic Questions
# ---------------------------------------------------------------------------

# --- Q1. Which team won the most matches? -----------------------------------
# Count how many times each team shows up as the match_winner, then plot it
# as a horizontal bar chart so the team names are easy to read.
match_wins = df["match_winner"].value_counts()
print("\nMatch wins by team:")
print(match_wins)

sns.barplot(y=match_wins.index, x=match_wins.values, palette="viridis")
plt.title("Most match win by team")
plt.xlabel("Wins")
plt.ylabel("Team")
plt.tight_layout()
plt.show()

# --- Q2. Toss Decision Trends ------------------------------------------------
# Do captains generally prefer to bat first or field first after winning the
# toss? A simple count plot answers that at a glance.
sns.countplot(x=df["toss_decision"], palette="rainbow")
plt.title("Toss Decision Trends")
plt.xlabel("Toss Decision")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# --- Q3. Toss Winner vs Match Winner ----------------------------------------
# Does winning the toss actually give a team an edge? We check what percentage
# of matches were won by the same team that won the toss.
toss_equals_match_wins = df[df["toss_winner"] == df["match_winner"]]["match_id"].count()
percentage = (toss_equals_match_wins * 100) / df.shape[0]
print(f"\nPercentage of matches where the toss winner also won the match: {percentage.round(2)}%")

# --- Q4. How do teams win? (Runs vs Wickets) --------------------------------
# When teams win, do they typically win by defending a total (Runs) or by
# chasing one down successfully (Wickets)?
sns.countplot(x=df["won_by"])
plt.title("Won by")
plt.xlabel("Victory Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------------
# 4. Key Player Performances
# ---------------------------------------------------------------------------

# --- 4.1 Most "Player of the Match" Awards ----------------------------------
# Tally up how many times each player was named Player of the Match, then
# spotlight the top 10 standout performers.
top_potm = df["player_of_the_match"].value_counts().head(10)
print("\nTop 10 Player of the Match award winners:")
print(top_potm)

sns.barplot(x=top_potm.values, y=top_potm.index, palette="mako")
plt.title("Top 10 players with man of the match")
plt.xlabel("Awards")
plt.ylabel("Player")
plt.tight_layout()
plt.show()

# --- 4.2 Top Scorers ---------------------------------------------------------
# Group by each player's name in the "top_scorer" column and sum their
# highest scores across matches, then surface the top run-getters.
high_scorers = df.groupby("top_scorer")["highscore"].sum().sort_values(ascending=False).head(2)
print("\nTop scorers (summed highscore across matches):")
print(high_scorers)

high_scorers.plot(kind="barh")
plt.title("Top Scorers")
plt.xlabel("Total Runs")
plt.tight_layout()
plt.show()

# --- 4.3 Best Bowling Figures -------------------------------------------------
# The "best_bowling_figure" column looks like "3--21" (wickets--runs conceded).
# We split on "--" and grab the wicket count so we can rank bowlers numerically.
df["highest_wickets"] = df["best_bowling_figure"].apply(lambda x: x.split("--")[0])
df["highest_wickets"] = df["highest_wickets"].astype(int)

top_bowlers = (
    df.groupby("best_bowling")["highest_wickets"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 bowlers by total wickets taken:")
print(top_bowlers)

top_bowlers.plot(kind="barh")
plt.title("Top 10 Bowlers by Wickets")
plt.xlabel("Wickets")
plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------------
# 5. Venue Analysis
# ---------------------------------------------------------------------------

# Which stadiums hosted the most matches this season?
venue_count = df["venue"].value_counts()
print("\nMatches played per venue:")
print(venue_count)

sns.barplot(y=venue_count.index, x=venue_count.values, palette="rainbow")
plt.title("Most Matches Played by Venue")
plt.xlabel("Matches")
plt.ylabel("Venue")
plt.tight_layout()
plt.show()


# ---------------------------------------------------------------------------
# 6. Custom Questions & Insights
# ---------------------------------------------------------------------------

# --- Q1: Who won by the highest margin of runs? -----------------------------
# Filter to matches won by "Runs", sort by margin descending, and grab the
# single biggest blowout.
biggest_runs_win = (
    df[df["won_by"] == "Runs"]
    .sort_values(by="margin", ascending=False)
    .head(1)[["match_winner", "margin"]]
)
print("\nBiggest win by runs margin:")
print(biggest_runs_win)

# --- Q2: Which player had the highest individual score? ---------------------
# Simply find the row(s) where highscore equals the maximum highscore overall.
best_individual_score = df[df["highscore"] == df["highscore"].max()][["top_scorer", "highscore"]]
print("\nHighest individual score of the season:")
print(best_individual_score)

# --- Q3: Which bowler had the best bowling figures? --------------------------
# Same idea, but using the wicket count we extracted earlier.
best_bowling_figures = df[df["highest_wickets"] == df["highest_wickets"].max()][
    ["best_bowling", "best_bowling_figure"]
]
print("\nBest bowling figures of the season:")
print(best_bowling_figures)

