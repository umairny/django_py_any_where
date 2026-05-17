import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from django.contrib.auth import get_user_model

from home.models import Features, Headings


DEMO_ACCOUNTS = [
    {
        "username": "mike",
        "password": "3256nike",
        "email": "mike@t.com",
    },
    {
        "username": "emma",
        "password": "1254emma",
        "email": "emma@w.com",
    },
    {
        "username": "harry",
        "password": "9856harr",
        "email": "harry@p.com",
    },
]


PROJECTS = [
    {
        "heading": "Ads Posting",
        "subHeading": "A Craigslist-like site for posting and browsing ads.",
        "icon": "fa fa-bullhorn",
        "btnApp": "/ads/",
        "btnCode": "https://github.com/umairny/django_py_any_where/tree/main/ads",
        "videoLink": "https://www.youtube.com/embed/TQm_RWh3ScU?si=YiVp0c9i4vkGOxO3",
        "features": ["Create/Delete Ads", "Search by Category", "Comments & Favorites"],
    },
    {
        "heading": "Auctions Bidding",
        "subHeading": "eBay-like auction site where users can bid on items.",
        "icon": "fa fa-gavel",
        "btnApp": "/auctions/",
        "btnCode": "https://github.com/umairny/django_py_any_where/tree/main/auctions",
        "videoLink": "https://www.youtube.com/embed/uiIx6cprAaE?si=Uxv1bbLOxK2gmq74",
        "features": ["Place Bids", "Watchlist", "Categories"],
    },
    {
        "heading": "Social network",
        "subHeading": "Twitter-like social network for posting and following.",
        "icon": "fa fa-share-alt",
        "btnApp": "/network/",
        "btnCode": "https://github.com/umairny/django_py_any_where/tree/main/network",
        "videoLink": "https://www.youtube.com/embed/YGODEgPwSGY?si=-m1nDfit67xKaRVW",
        "features": ["Post Content", "Follow Users", "Like Posts"],
    },
    {
        "heading": "Wiki app",
        "subHeading": "Encyclopedia-like site for creating and editing articles.",
        "icon": "fa fa-wikipedia-w",
        "btnApp": "/wiki/",
        "btnCode": "https://github.com/umairny/django_py_any_where/tree/main/wiki",
        "videoLink": "https://www.youtube.com/embed/YOcolbDtCLo?si=jVjxS50TLAec76Me",
        "features": ["Create/Edit Markdown Pages", "Search Articles", "Random Page"],
    },
    {
        "heading": "E-mail App",
        "subHeading": "Single-page email client for sending/receiving mail.",
        "icon": "fa fa-envelope",
        "btnApp": "/mail/",
        "btnCode": "https://github.com/umairny/django_py_any_where/tree/main/mail",
        "videoLink": "https://www.youtube.com/embed/MtOYfxbSdJo?si=RmVjfDfWMDKL1H7V",
        "features": ["Inbox/Sent/Archived", "Compose Mail", "Single Page App"],
    },
]


def populate_demo_accounts():
    User = get_user_model()
    created_count = 0
    updated_count = 0

    for account in DEMO_ACCOUNTS:
        user, created = User.objects.get_or_create(
            username=account["username"],
            defaults={"email": account["email"]},
        )
        user.email = account["email"]
        user.set_password(account["password"])
        user.save()

        if created:
            created_count += 1
            print(f"Created demo account: {account['username']}")
        else:
            updated_count += 1
            print(f"Updated demo account: {account['username']}")

    return created_count, updated_count


def populate_projects():
    created_count = 0
    updated_count = 0
    feature_count = 0

    for project in PROJECTS:
        heading, created = Headings.objects.update_or_create(
            heading=project["heading"],
            defaults={
                "subHeading": project["subHeading"],
                "icon": project["icon"],
                "btnApp": project["btnApp"],
                "btnCode": project["btnCode"],
                "videoLink": project["videoLink"],
            },
        )

        for feature_text in project["features"]:
            _, feature_created = Features.objects.get_or_create(
                head=heading,
                feature=feature_text,
            )
            if feature_created:
                feature_count += 1

        if created:
            created_count += 1
            print(f"Created project: {project['heading']}")
        else:
            updated_count += 1
            print(f"Updated project: {project['heading']}")

    return created_count, updated_count, feature_count


def populate():
    print("Populating database...")

    users_created, users_updated = populate_demo_accounts()
    projects_created, projects_updated, features_created = populate_projects()

    print(
        "Done: "
        f"{users_created} users created, {users_updated} users updated; "
        f"{projects_created} projects created, {projects_updated} projects updated; "
        f"{features_created} features created."
    )


if __name__ == "__main__":
    populate()
