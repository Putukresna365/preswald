from preswald import connect, get_df, table, text, query, plotly
import plotly.express as px

text("# My Data Analysis App")
text("This is your first app. 🎉")
data_set = "data/student_habits_performance.csv"
# task 1
text("# Task 1")
text("here are the result for the task 1")
connect()
df = get_df(f"{data_set}")
table(df)

# task 2
sql = f"SELECT * FROM {data_set} WHERE student_id LIKE '%001'"
filtered_df = query(sql, data_set)

# task 3
text("# Task 3")
text("here are the result for the task 3")
table(filtered_df, title="Filtered Data")

# task 4
text("# Task 4")
text("here are the result for the task 4")
fig = px.scatter(df, 
    x='gender', y='exam_score', text='age',
    title='Gender vs. Exam Score', 
    labels={'gender': 'Gender', 'exam_score': 'Exam Score'}
)
fig.update_traces(textposition='top right', marker=dict(size=12, color='lightblue'))
fig.update_layout(template='plotly_white')
plotly(fig)