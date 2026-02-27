import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from home.models import Headings, Features, SubFeatures

def populate():
    print("Populating database with project data...")

    # Data to add
    projects = [
        {
            "heading": "Ads Posting",
            "subHeading": "A Craigslist-like site for posting and browsing ads.",
            "icon": "fa fa-bullhorn",
            "btnApp": "/ads/",
            "btnCode": "https://github.com/umairny/django_py_any_where/tree/main/ads",
            "videoLink": "https://www.youtube.com/embed/TQm_RWh3ScU?si=YiVp0c9i4vkGOxO3", # Placeholder
            "features": ["Create/Delete Ads", "Search by Category", "Comments & Favorites"]
        },
        {
            "heading": "Auctions Bidding",
            "subHeading": "eBay-like auction site where users can bid on items.",
            "icon": "fa fa-gavel",
            "btnApp": "/auctions/",
            "btnCode": "https://github.com/umairny/django_py_any_where/tree/main/auctions",
            "videoLink": "https://www.youtube.com/embed/uiIx6cprAaE?si=Uxv1bbLOxK2gmq74",
            "features": ["Place Bids", "Watchlist", "Categories"]
        },
        {
            "heading": "Social network",
            "subHeading": "Twitter-like social network for posting and following.",
            "icon": "fa fa-share-alt",
            "btnApp": "/network/",
            "btnCode": "https://github.com/umairny/django_py_any_where/tree/main/network",
            "videoLink": "https://www.youtube.com/embed/YGODEgPwSGY?si=-m1nDfit67xKaRVW",
            "features": ["Post Content", "Follow Users", "Like Posts"]
        },
        {
            "heading": "Wiki app",
            "subHeading": "Encyclopedia-like site for creating and editing articles.",
            "icon": "fa fa-wikipedia-w",
            "btnApp": "/wiki/",
            "btnCode": "https://github.com/umairny/django_py_any_where/tree/main/wiki",
            "videoLink": "https://www.youtube.com/embed/YOcolbDtCLo?si=jVjxS50TLAec76Me",
            "features": ["Create/Edit Markdown Pages", "Search Articles", "Random Page"]
        },
        {
            "heading": "E-mail App",
            "subHeading": "Single-page email client for sending/receiving mail.",
            "icon": "fa fa-envelope",
            "btnApp": "/mail/",
            "btnCode": "https://github.com/umairny/django_py_any_where/tree/main/mail",
            "videoLink": "https://www.youtube.com/embed/MtOYfxbSdJo?si=RmVjfDfWMDKL1H7V",
            "features": ["Inbox/Sent/Archived", "Compose Mail", "Single Page App"]
        }
    ]

    for p in projects:
        heading, created = Headings.objects.get_or_create(
            heading=p["heading"],
            defaults={
                "subHeading": p["subHeading"],
                "icon": p["icon"],
                "btnApp": p["btnApp"],
                "btnCode": p["btnCode"],
                "videoLink": p["videoLink"]
            }
        )
        if created:
            print(f"Created heading: {p['heading']}")
            for f_text in p["features"]:
                Features.objects.create(head=heading, feature=f_text)
        else:
            print(f"Heading already exists: {p['heading']}")

    print("Success!")

if __name__ == "__main__":
    populate()
