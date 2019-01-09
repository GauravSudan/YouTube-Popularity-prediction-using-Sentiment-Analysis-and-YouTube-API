#RUN COMMAND = "--search="Kwality Walls Ice Cream Sandwich Chocolate and Vanilla " --key=AIzaSyBxfwXiIAh3iLAzfK6eRcxisKcQEHLrsW0"
import json
import sys
import argparse
from urllib.request import  urlopen
from keyword_matching_prog import keywordmatching


YOUTUBE_COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

class YouTubeApi():
    def search_keyword(self):

        def load_search_res(self):
            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                  videos.append("{} ({})".format(search_result["snippet"]["title"],
                                             search_result["id"]["videoId"]))
                elif search_result["id"]["kind"] == "youtube#channel":
                  channels.append("{} ({})".format(search_result["snippet"]["title"],
                                               search_result["id"]["channelId"]))
                
        parser = argparse.ArgumentParser()
        mxRes = 1
        parser.add_argument("--s", help="calls the search by keyword function", action='store_true')
        parser.add_argument("--r", help="define country code for search results for specific country", default="IN")
        parser.add_argument("--search", help="Search Term", default="Srce Cde")
        parser.add_argument("--max", help="number of results to return")
        parser.add_argument("--key", help="Required API key")

        args = parser.parse_args()

        if not args.max:
            args.max = mxRes

        if not args.key:
            exit("Please specify API key using the --key= parameter.")

        parms = {
                    'q': args.search,
                    'part': 'id,snippet',
                    'maxResults': args.max,
                    'regionCode': args.r,
                    'key': args.key
                }

        try:
            matches = self.openURL(YOUTUBE_SEARCH_URL, parms)

            search_response = json.loads(matches)
            
            videos = []
            channels=[]
            load_search_res(self)
            print("------------------------------------------------------------------")
            print(videos[0])
           # print(channels[0])
        
        except KeyboardInterrupt:
            print("User Aborted the Operation")

        except:
            print("Cannot Open URL or Fetch comments at a moment")

    #l1="Kwality Walls Ice Cream Sandwich Chocolate and Vanilla (LWGaiMjceeo)"
        l1=videos[0]
        keywordmatching(l1)
        
    def openURL(self, url, parms):
            f = urlopen(url + '?' + urlencode(parms))
            data = f.read()
            f.close()
            matches = data.decode("utf-8")
            return matches


def main():
    
    y = YouTubeApi()
    y.search_keyword()
    
  
    #l='learn python'
    #l="Kwality Walls Ice Cream Sandwich Chocolate and Vanilla"
    #l='travel is life'
    #l='loose weight'
   #l=input("Enter Name of Video :")        #For Manual Matching
    #print("ENTER YOUR VIDEO'S TITLE")
    #l=input("ENTER YOUR VIDEO'S TITLE :")
    #keywordmatching(l)
    

if __name__ == '__main__':
    main()
    
#--c --videourl=https://www.youtube.com/watch?v=Cr6VqTRO1v0&t=59s --key=AIzaSyBxfwXiIAh3iLAzfK6eRcxisKcQEHLrsW0     #for comments
#