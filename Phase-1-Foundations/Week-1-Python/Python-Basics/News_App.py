from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="e6aed0e5e74e4ae18cf7193883e7c4a8")
while True:
    try:
        n=int(input("Enter 1 for football \nEnter 2 for Politics\nEnter 3 Bitcoin\nEnter 4 for Cars\nEnter 5 for Technology\nEnter 6 for AI\nEnter your choice : "))
        if(n>0 and n<7):
            break
        else:
            print("Wrong Input")
    except Exception as e:
        print("Something Went Wrong!\n Please Try Again")
z=0
match n:
    case 1:
        z='football'
    case 2:
        z='politics'
    case 3:
        z='bitcoin'
    case 4:
        z='cars'
    case 5:
        z='technology'
    case 6:
        z='AI'

data = newsapi.get_everything(q=z,
    language='en',
    sort_by='publishedAt')

# STEP 1: Check if API returned success
if data.get('status') != 'ok':
    print("API Error:", data.get('message'))
    exit()

# STEP 2: If no articles
if not data.get('articles'):
    print("No news found.")
    exit()

# STEP 3: Print formatted news
for i, article in enumerate(data['articles'], start=1):
    print(f"\n------ NEWS {i} ------")
    print("Title:", article.get('title'))
    print("Description:", article.get('description'))
    print("Source:", article.get('source', {}).get('name'))
    print("URL:", article.get('url'))
