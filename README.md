DiningAnalysis – A Simple Tool to Tell You If You're Broke (or Ballin’) on Dining Dollars

What This Is:
This is a small Python project I made to figure out whether I’m spending my UW dining dollars too fast, too slow, or (miraculously) at the perfect rate.
If you’ve ever gotten halfway through the quarter and thought “wait… am I supposed to have $200 left or like $800?”, this tool answers that.

What It Does:
- Calculates how many days you’re actually on campus
- Figures out how much money you should have at the moment
- Tells you if you’re overspending or underspending
- Gives you a “how much to spend per day” number
- Predicts how much money you’ll end the quarter with
- Suggests whether you should move up or down a dining plan
- Basically, it’s a budgeting tool but without the guilt trip.

How to Use It:

1. Clone the repo
  git clone https://github.com/yourusername/yourrepo.git

2. Import the class and plug in your info:
  from dining_analysis import DiningAnalysis

  me = DiningAnalysis(
      name="Charlotte",
      dining_plan_level=3,
      move_in_date=(9, 25),
      move_out_date=(12, 15),
      days_home_total=3
  )
  
  me.print_analysis(
      current_date=(11, 5),
      days_home_current=1,
      current_balance=480
  )

Read your personalized verdict on whether you’ve been eating like:
a financially responsible adult or someone who just blew $35 on one sandwich from Local Point

What You Need:
- Python 3 (literally nothing else)

Files:
dining_analysis.py – all the logic lives here

Why I Made This:
UW dining plans have weirdly specific dollar amounts and it’s hard to know if you’re “on track,” so I made a tool that does the math for you.

Future Ideas (if I ever care enough):
- Automatic date handling
- Support for leap years
- Graphs (because everyone secretly loves graphs)
- A tiny website version

About Me:
Hi, I’m Charlotte. I like data science and making my life slightly easier with code.
