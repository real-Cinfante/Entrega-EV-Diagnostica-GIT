import re
import json



def main():


    tweets = []
    

    # count = 0

    for line in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        new_tweet = json.loads(line)
        tweets.append(new_tweet)
        # count += 1
        # if count == 10000:
        #     break



    #print(len(tweets))
    print("Tweet id of top 10 most retweeted tweets:")
    print(top_10_most_retweeted_tweets(tweets))
    print("Top 10 most active users (most tweets):")
    print(top_10_most_acticve_users(tweets))
    print("Top 10 most active days (most tweets):")
    print(top_10_most_acticve_days(tweets))
    print("Top 10 most hashtags used (most tweets):")
    print(top_10_most_hashgtags(tweets))
    return 





def top_10_most_retweeted_tweets(tweets):
    most_retweeted_tweet = [0,0,0,0,0,0,0,0,0,0]
    most_retweeted_tweet_id = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(tweets)):
        for j in range(10):
            if tweets[i]['retweetCount'] > most_retweeted_tweet[j]:
                most_retweeted_tweet[j] = tweets[i]['retweetCount']
                most_retweeted_tweet_id[j] = tweets[i]['id']
                break
    return most_retweeted_tweet_id



def top_10_most_acticve_users(tweets):
    most_active_users = []
    users_tweets_count = []
    for i in range(len(tweets)):
        for e in users_tweets_count:
            if tweets[i]['user']['username'] == e[0]:
                e[1] += 1
                break
        else:
            users_tweets_count.append([tweets[i]['user']['username'], 1])

    users_tweets_count.sort(key=lambda inner_list:inner_list[1], reverse=True)
    for i in range(10):
        most_active_users.append(users_tweets_count[i])


    return most_active_users


def top_10_most_acticve_days(tweets):
    most_active_days = []
    days_tweets_count = []
    for i in range(len(tweets)):
        date = tweets[i]['date'].split('T')[0]
        for e in days_tweets_count:
            if date == e[0]:
                e[1] += 1
                break
        else:
            days_tweets_count.append([date, 1])

    days_tweets_count.sort(key=lambda inner_list:inner_list[1], reverse=True)

    if len(most_active_days) < 10:
        for i in range(len(days_tweets_count)):
            most_active_days.append(days_tweets_count[i])
    else:
        for i in range(10):
            most_active_days.append(days_tweets_count[i])

    return most_active_days

def top_10_most_hashgtags(tweets):
    most_hashgtags = []
    hashgtags_count = []
    for i in range(len(tweets)):
        tweet = tweets[i]['content'].split(' ')
        for e in tweet:
            if len(e) > 1:
                if e[0] == '#':
                    for f in hashgtags_count:
                        if e == f[0]:
                            f[1] += 1
                            break
                    else:
                        hashgtags_count.append([e, 1])
    


    hashgtags_count.sort(key=lambda inner_list:inner_list[1], reverse=True)
    for i in range(10):
        most_hashgtags.append(hashgtags_count[i])

    return most_hashgtags



main()