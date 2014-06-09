#!/usr/bin/env python
#
#

import requests
import re
import argparse
import sys


def posts_sorted_count(posts_of_users):
    users_list = posts_of_users.keys()

    users_list = sorted(users_list, key=posts_of_users.__getitem__, reverse = True)

    total_posts = 0

    for name in users_list:
        total_posts += posts_of_users[name]

    i = 1
    for name in users_list:
        percents_post = (posts_of_users[name] / (total_posts / 100.0))
        print "%d) %s => %d (%f percents)" % (i, name, posts_of_users[name], percents_post)
        i += 1

    print "Total: %d" % total_posts

def find_user_posts(topic_id, start_page, last_page):

    pattern = re.compile(r'quote\(selection,\'(?P<user_name>.*)\'\)')

    user_posts = {}

    page_id = start_page

    for i in xrange(start_page, last_page + 1):

        payload = {'topic' : topic_id, 'page' : page_id}
        page_content = requests.get("http://reps.ru/forum.php", params=payload)
        
        for line in page_content.text.splitlines():
            result = pattern.search(line )
            
            if result:
                if result.group("user_name") in user_posts.keys():
                    user_posts[result.group("user_name")] += 1
                else:
                    user_posts[result.group("user_name")] = 1

        page_id += 1

    return user_posts


def main():

    argps = argparse.ArgumentParser()
    argps.add_argument("topic", type=str,
                help="ID of topic on forum")
    argps.add_argument("-s", "--start", type=int,
                help="ID of start page in topic")
    argps.add_argument("-e", "--end", type=int,
                help="ID of end page in topic")

    args = argps.parse_args()

    topic = args.topic

    if args.start:
        page_start = args.start
    else:
        page_start = 1

    if args.end:
        end_page = args.end
    else:
        end_page = 1


    users_posts = find_user_posts(topic, page_start, end_page)
    posts_sorted_count(users_posts)
    
if __name__ == '__main__':
    main()