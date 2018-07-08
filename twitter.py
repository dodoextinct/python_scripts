#importing the libraries
import tweepy
import json
import warnings
import sys

#twitter api keys
consumer_key = "<Key>"
consumer_secret = "<key>"

access_token = "<key>"
access_secret="<key>"

#authenticating the api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def get_all_tweets(screen_name):
    """get's the user information and tweets"""

    #get's the user details
    profile_dictionary = get_user_details(screen_name)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))
       
    #write tweet objects to JSON
    file = open('{}.json'.format(screen_name), 'w')
    json.dump(profile_dictionary,file)
    print("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print("Done")
    file.close()

def get_user_details(screen_name):
    """get all the user details"""
    user = api.get_user(screen_name)
    return {"user_name" : user.screen_name, "description":user.description,"followers":user.followers_count,"tweets": user.statuses_count,"profile_url":user.url}
     

if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    try:
        #input should be command line
        arg = sys.argv[1]
        if 'https' in arg:#executes when profile link provided
            screen_name = arg.split("/")[3]
        else:#executes when user name provided
            screen_name = arg
        get_all_tweets(screen_name)

    except Exception as e:
        print(e)
        print("Expected command line argument of twitter profile link or user name")


"""output format

{"profile_url": "https://url", "followers": 554, "tweets": 1600, "user_name": "user_name", "description": "desciption"}

{
    "contributors": null, 
    "coordinates": null, 
    "created_at": "Sat Aug 20 01:00:12 +0000 2016", 
    "entities": {
        "hashtags": [
            {
                "indices": [
                    97, 
                    116
                ], 
                "text": "StandWithLouisiana"
            }
        ], 
        "media": [
            {
                "display_url": "pic.twitter.com/Ob7J2oBWhq", 
                "expanded_url": "https://twitter.com/realDonaldTrump/status/766801978085117952/video/1", 
                "id": 766801621007294464, 
                "id_str": "766801621007294464", 
                "indices": [
                    117, 
                    140
                ], 
                "media_url": "https://pbs.twimg.com/ext_tw_video_thumb/766801621007294464/pu/img/0utktWvDSyGamM4m.jpg", 
                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/766801621007294464/pu/img/0utktWvDSyGamM4m.jpg", 
                "sizes": {
                    "large": {
                        "h": 576, 
                        "resize": "fit", 
                        "w": 1024
                    }, 
                    "medium": {
                        "h": 338, 
                        "resize": "fit", 
                        "w": 600
                    }, 
                    "small": {
                        "h": 191, 
                        "resize": "fit", 
                        "w": 340
                    }, 
                    "thumb": {
                        "h": 150, 
                        "resize": "crop", 
                        "w": 150
                    }
                }, 
                "type": "photo", 
                "url": "https://t.co/Ob7J2oBWhq"
            }
        ], 
        "symbols": [], 
        "urls": [], 
        "user_mentions": []
    }, 
    "extended_entities": {
        "media": [
            {
                "additional_media_info": {
                    "monetizable": false
                }, 
                "display_url": "pic.twitter.com/Ob7J2oBWhq", 
                "expanded_url": "https://twitter.com/realDonaldTrump/status/766801978085117952/video/1", 
                "id": 766801621007294464, 
                "id_str": "766801621007294464", 
                "indices": [
                    117, 
                    140
                ], 
                "media_url": "https://pbs.twimg.com/ext_tw_video_thumb/766801621007294464/pu/img/0utktWvDSyGamM4m.jpg", 
                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/766801621007294464/pu/img/0utktWvDSyGamM4m.jpg", 
                "sizes": {
                    "large": {
                        "h": 576, 
                        "resize": "fit", 
                        "w": 1024
                    }, 
                    "medium": {
                        "h": 338, 
                        "resize": "fit", 
                        "w": 600
                    }, 
                    "small": {
                        "h": 191, 
                        "resize": "fit", 
                        "w": 340
                    }, 
                    "thumb": {
                        "h": 150, 
                        "resize": "crop", 
                        "w": 150
                    }
                }, 
                "type": "video", 
                "url": "https://t.co/Ob7J2oBWhq", 
                "video_info": {
                    "aspect_ratio": [
                        16, 
                        9
                    ], 
                    "duration_millis": 140000, 
                    "variants": [
                        {
                            "bitrate": 320000, 
                            "content_type": "video/mp4", 
                            "url": "https://video.twimg.com/ext_tw_video/766801621007294464/pu/vid/320x180/0t4SNNy1YU1rHCYo.mp4"
                        }, 
                        {
                            "content_type": "application/dash+xml", 
                            "url": "https://video.twimg.com/ext_tw_video/766801621007294464/pu/pl/QiF_xbP1ARIdGp-F.mpd"
                        }, 
                        {
                            "content_type": "application/x-mpegURL", 
                            "url": "https://video.twimg.com/ext_tw_video/766801621007294464/pu/pl/QiF_xbP1ARIdGp-F.m3u8"
                        }, 
                        {
                            "bitrate": 2176000, 
                            "content_type": "video/mp4", 
                            "url": "https://video.twimg.com/ext_tw_video/766801621007294464/pu/vid/1280x720/8zc8PRPYNM4KmCXd.mp4"
                        }, 
                        {
                            "bitrate": 832000, 
                            "content_type": "video/mp4", 
                            "url": "https://video.twimg.com/ext_tw_video/766801621007294464/pu/vid/640x360/q_ClmD0bzudWewVn.mp4"
                        }
                    ]
                }
            }
        ]
    }, 
    "favorite_count": 42550, 
    "favorited": false, 
    "geo": null, 
    "id": 766801978085117952, 
    "id_str": "766801978085117952", 
    "in_reply_to_screen_name": null, 
    "in_reply_to_status_id": null, 
    "in_reply_to_status_id_str": null, 
    "in_reply_to_user_id": null, 
    "in_reply_to_user_id_str": null, 
    "is_quote_status": false, 
    "lang": "en", 
    "place": null, 
    "possibly_sensitive": false, 
    "retweet_count": 16977, 
    "retweeted": false, 
    "source": "&amp;amp;amp;amp;lt;a href=\"https://twitter.com/download/iphone\" rel=\"nofollow\"&amp;amp;amp;amp;gt;Twitter for iPhone&amp;amp;amp;amp;lt;/a&amp;amp;amp;amp;gt;", 
    "text": "We are one nation. When one hurts, we all hurt. We must all work together-to lift each other up.\n#StandWithLouisiana https://t.co/Ob7J2oBWhq", 
    "truncated": false, 
    "user": {
        "contributors_enabled": false, 
        "created_at": "Wed Mar 18 13:46:38 +0000 2009", 
        "default_profile": false, 
        "default_profile_image": false, 
        "description": "#TrumpPence16", 
        "entities": {
            "description": {
                "urls": []
            }, 
            "url": {
                "urls": [
                    {
                        "display_url": "DonaldJTrump.com", 
                        "expanded_url": "https://www.DonaldJTrump.com", 
                        "indices": [
                            0, 
                            23
                        ], 
                        "url": "https://t.co/mZB2hymxC9"
                    }
                ]
            }
        }, 
        "favourites_count": 35, 
        "follow_request_sent": false, 
        "followers_count": 11087586, 
        "following": true, 
        "friends_count": 42, 
        "geo_enabled": true, 
        "has_extended_profile": false, 
        "id": 25073877, 
        "id_str": "25073877", 
        "is_translation_enabled": true, 
        "is_translator": false, 
        "lang": "en", 
        "listed_count": 37773, 
        "location": "New York, NY", 
        "name": "Donald J. Trump", 
        "notifications": false, 
        "profile_background_color": "6D5C18", 
        "profile_background_image_url": "https://pbs.twimg.com/profile_background_images/530021613/trump_scotland__43_of_70_cc.jpg", 
        "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/530021613/trump_scotland__43_of_70_cc.jpg", 
        "profile_background_tile": true, 
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/25073877/1468988952", 
        "profile_image_url": "https://pbs.twimg.com/profile_images/1980294624/DJT_Headshot_V2_normal.jpg", 
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1980294624/DJT_Headshot_V2_normal.jpg", 
        "profile_link_color": "0D5B73", 
        "profile_sidebar_border_color": "BDDCAD", 
        "profile_sidebar_fill_color": "C5CEC0", 
        "profile_text_color": "333333", 
        "profile_use_background_image": true, 
        "protected": false, 
        "screen_name": "realDonaldTrump", 
        "statuses_count": 32979, 
        "time_zone": "Eastern Time (US &amp;amp;amp;amp;amp; Canada)", 
        "url": "https://t.co/mZB2hymxC9", 
        "utc_offset": -14400, 
        "verified": true
    }
}{
    "contributors": null, 
    "coordinates": null, 
    "created_at": "Sat Aug 20 00:17:09 +0000 2016", 
    "entities": {
        "hashtags": [
            {
                "indices": [
                    0, 
                    14
                ], 
                "text": "WheresHillary"
            }
        ], 
        "symbols": [], 
        "urls": [], 
        "user_mentions": []
    }, 
    "favorite_count": 59882, 
    "favorited": false, 
    "geo": null, 
    "id": 766791143291916288, 
    "id_str": "766791143291916288", 
    "in_reply_to_screen_name": null, 
    "in_reply_to_status_id": null, 
    "in_reply_to_status_id_str": null, 
    "in_reply_to_user_id": null, 
    "in_reply_to_user_id_str": null, 
    "is_quote_status": false, 
    "lang": "en", 
    "place": null, 
    "retweet_count": 27272, 
    "retweeted": false, 
    "source": "&amp;amp;amp;amp;lt;a href=\"https://twitter.com/download/iphone\" rel=\"nofollow\"&amp;amp;amp;amp;gt;Twitter for iPhone&amp;amp;amp;amp;lt;/a&amp;amp;amp;amp;gt;", 
    "text": "#WheresHillary? Sleeping!!!!!", 
    "truncated": false, 
    "user": {
        "contributors_enabled": false, 
        "created_at": "Wed Mar 18 13:46:38 +0000 2009", 
        "default_profile": false, 
        "default_profile_image": false, 
        "description": "#TrumpPence16", 
        "entities": {
            "description": {
                "urls": []
            }, 
            "url": {
                "urls": [
                    {
                        "display_url": "DonaldJTrump.com", 
                        "expanded_url": "https://www.DonaldJTrump.com", 
                        "indices": [
                            0, 
                            23
                        ], 
                        "url": "https://t.co/mZB2hymxC9"
                    }
                ]
            }
        }, 
        "favourites_count": 35, 
        "follow_request_sent": false, 
        "followers_count": 11087586, 
        "following": true, 
        "friends_count": 42, 
        "geo_enabled": true, 
        "has_extended_profile": false, 
        "id": 25073877, 
        "id_str": "25073877", 
        "is_translation_enabled": true, 
        "is_translator": false, 
        "lang": "en", 
        "listed_count": 37773, 
        "location": "New York, NY", 
        "name": "Donald J. Trump", 
        "notifications": false, 
        "profile_background_color": "6D5C18", 
        "profile_background_image_url": "https://pbs.twimg.com/profile_background_images/530021613/trump_scotland__43_of_70_cc.jpg", 
        "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/530021613/trump_scotland__43_of_70_cc.jpg", 
        "profile_background_tile": true, 
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/25073877/1468988952", 
        "profile_image_url": "https://pbs.twimg.com/profile_images/1980294624/DJT_Headshot_V2_normal.jpg", 
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1980294624/DJT_Headshot_V2_normal.jpg", 
        "profile_link_color": "0D5B73", 
        "profile_sidebar_border_color": "BDDCAD", 
        "profile_sidebar_fill_color": "C5CEC0", 
        "profile_text_color": "333333", 
        "profile_use_background_image": true, 
        "protected": false, 
        "screen_name": "realDonaldTrump", 
        "statuses_count": 32979, 
        "time_zone": "Eastern Time (US &amp;amp;amp;amp;amp; Canada)", 
        "url": "https://t.co/mZB2hymxC9", 
        "utc_offset": -14400, 
        "verified": true
    }
}
