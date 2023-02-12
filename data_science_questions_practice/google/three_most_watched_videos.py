"""
After a new user creates an account and starts watching videos, the user ID, video ID, and date watched are captured in
 the database. Find the top 3 videos most users have watched as their first 3 videos. Output the video ID and the number
  of times it has been watched as the users' first 3 videos.


In the event of a tie, output all the videos in the top 3 that users watched as their first 3 videos.
Algorithm:
1. Group by user id and create a rank column. rank column will have values from 1 to 3 for each group. rank 1 is first video, rank 2
is second video rank 3 third video. save the result in a dataframe.
2. group by above df, by video id. Create a dataframe with video id and count.
3. Create dense rank in the descending order of count obtained from the above dataframe.
2. Final result will be all the videos with rank <= 3
"""
import pandas as pd
videos_watched = pd.read_csv('../data_files/videos_watched.csv')
videos_watched['watch_order'] = videos_watched.groupby('user_id')['watched_at'].rank()
first_three_videos_bool_mask = videos_watched.loc[:, 'watch_order'] <= 3
videos_watched = videos_watched.loc[first_three_videos_bool_mask, :]
videos = videos_watched.groupby('video_id').size().rename('count').reset_index()

videos['rank'] = videos['count'].rank(method='dense', ascending=False)
bool_mask = videos.loc[:, 'rank'] <= 3
videos = videos.loc[bool_mask, :]
print(videos.loc[:, ['video_id', 'count']])
