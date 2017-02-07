from django.contrib import admin
from .models import About, News, NewsCategory, PartnersBanner, Players, ClubPlayers, Match, Goals, Cards, Teams, \
    Championship, Season, VideoCategory, Videos

# Register your models here.

admin.site.register(About)
admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(PartnersBanner)
admin.site.register(Players)
admin.site.register(ClubPlayers)
admin.site.register(Match)
admin.site.register(Goals)
admin.site.register(Cards)
admin.site.register(Teams)
admin.site.register(Championship)
admin.site.register(Season)
admin.site.register(VideoCategory)
admin.site.register(Videos)
