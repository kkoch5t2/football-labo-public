from django.utils import timezone
from django.conf import settings
from datetime import datetime, date, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from multiprocessing.shared_memory import SharedMemory
import tweepy

from soccer.models import(
    CustomUser,
    Comment,
    ManagerComment,
    NationalComment,
    ClubComment,
    ClubCommentLikeIpAddress,
    NationalCommentLikeIpAddress,
    ManagerLikeIpAddress,
    LikeIpAddress,
)

bearer_token = settings.TWEEPY_BEARER_TOKEN
consumer_key = settings.TWEEPY_CONSUMER_KEY
consumer_secret = settings.TWEEPY_CONSUMER_SECRET
access_token = settings.TWEEPY_ACCESS_TOKEN
access_token_secret = settings.TWEEPY_ACCESS_TOKEN_SECRET

client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


def delete_customuser():
    qs = CustomUser.objects.filter(is_active=False)
    for user in qs:
        user_date_joined = user.date_joined + timedelta(days=1)
        if user_date_joined < timezone.localtime(timezone.now()):
            user.delete()


def club_comment_like_count_update():
    qs = ClubCommentLikeIpAddress.objects.all()
    for like_ip in qs:
        if like_ip.like_click_count > 0:
            like_ip.like_click_count -= 1
            like_ip.save()
        else:
            like_ip.save()


def national_comment_like_count_update():
    qs = NationalCommentLikeIpAddress.objects.all()
    for like_ip in qs:
        if like_ip.like_click_count > 0:
            like_ip.like_click_count -= 1
            like_ip.save()
        else:
            like_ip.save()


def manager_comment_like_count_update():
    qs = ManagerLikeIpAddress.objects.all()
    for like_ip in qs:
        if like_ip.like_click_count > 0:
            like_ip.like_click_count -= 1
            like_ip.save()
        else:
            like_ip.save()


def player_comment_like_count_update():
    qs = LikeIpAddress.objects.all()
    for like_ip in qs:
        if like_ip.like_click_count > 0:
            like_ip.like_click_count -= 1
            like_ip.save()
        else:
            like_ip.save()


def player_comment_auto_tweet():
    random_comment = Comment.objects.order_by('?')[0]
    print(random_comment)
    player_name = random_comment.player.name
    author = random_comment.author
    ovr = random_comment.ovr
    if len(random_comment.text) <= 40:
        text = random_comment.text
    else:
        text = random_comment.text[:40] + "…"
    player_id = random_comment.player.id
    tweet = F"""⚽️みんなのサッカーラボ｜{ player_name }の評価

📝コメント
🗣️{ author }さん - 📊総合評価：{ ovr }／7
{ text }
https://football-labo.com/player/{ player_id }/ """
    client.create_tweet(text = tweet)


def manager_comment_auto_tweet():
    random_comment = ManagerComment.objects.order_by('?')[0]
    manager_name = random_comment.manager.name
    author = random_comment.author
    ovr = random_comment.ovr
    if len(random_comment.text) <= 40:
        text = random_comment.text
    else:
        text = random_comment.text[:40] + "…"
    manager_id = random_comment.manager.id
    tweet = F"""⚽️みんなのサッカーラボ｜{ manager_name }の評価

📝コメント
🗣️{ author }さん - 📊総合評価：{ ovr }／7
{ text }
https://football-labo.com/manager/{ manager_id }/ """
    client.create_tweet(text = tweet)


def club_comment_auto_tweet():
    random_comment = ClubComment.objects.order_by('?')[0]
    team_name = random_comment.team.name
    author = random_comment.author
    ovr = random_comment.ovr
    if len(random_comment.text) <= 40:
        text = random_comment.text
    else:
        text = random_comment.text[:40] + "…"
    team_slug = random_comment.team.slug
    tweet = F"""⚽️みんなのサッカーラボ｜{ team_name }の評価

📝コメント
🗣️{ author }さん - 📊総合評価：{ ovr }／7
{ text }
https://football-labo.com/team/{ team_slug }/ """
    client.create_tweet(text = tweet)


def national_comment_auto_tweet():
    random_comment = NationalComment.objects.order_by('?')[0]
    country_name = random_comment.country.name
    author = random_comment.author
    ovr = random_comment.ovr
    if len(random_comment.text) <= 40:
        text = random_comment.text
    else:
        text = random_comment.text[:40] + "…"
    country_slug = random_comment.country.slug
    tweet = F"""⚽️みんなのサッカーラボ｜{ country_name }の評価

📝コメント
🗣️{ author }さん - 📊総合評価：{ ovr }／7
{ text }
https://football-labo.com/country/{ country_slug }/ """
    client.create_tweet(text = tweet)


def start():
    try:
        # 共有メモリが取得できた場合は過去に既にapschedulerが実行されているので何もせず処理を抜ける
        sm = SharedMemory(create=False, name="apscheduler_start")
        return
    except:
        # 共有メモリが取得できなかった場合は初回のapscheduler実行なので共有メモリを登録して処理を続行
        shm = SharedMemory(create=True, size=1, name="apscheduler_start")
    
    scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Tokyo'})
    scheduler.add_job(delete_customuser, 'interval', days=1)

    if settings.ENVIRONMENT_NAME == 'production':
        scheduler.add_job(club_comment_like_count_update, 'interval', hours=5)
        scheduler.add_job(national_comment_like_count_update, 'interval', hours=5)
        scheduler.add_job(manager_comment_like_count_update, 'interval', hours=5)
        scheduler.add_job(player_comment_like_count_update, 'interval', hours=5)
        scheduler.add_job(player_comment_auto_tweet, 'cron', hour=19, minute=30)
        scheduler.add_job(manager_comment_auto_tweet, 'cron', hour=20, minute=30)
        scheduler.add_job(club_comment_auto_tweet, 'cron', hour=22, minute=30)
        scheduler.add_job(national_comment_auto_tweet, 'cron', hour=23, minute=30)
    
    scheduler.start()

