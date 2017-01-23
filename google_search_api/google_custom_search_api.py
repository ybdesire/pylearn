import pprint

from googleapiclient.discovery import build


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
    service = build("customsearch", "v1",
            developerKey="AIzaSyBpTkSdF1yAFHr93DC0wx-svc_-eWfQw8I")#API key

    res = service.cse().list(
      q='droid',
      cx='002604350963883255681:70v20qffkha',#search engine
    ).execute()
    #pprint.pprint(res)
    print(res['items'][5])

if __name__ == '__main__':
    main()
