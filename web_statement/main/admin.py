from django.contrib import admin
from .models import Bid , Rule, Signers_bid, SourceBid, RecipientBid

admin.site.register(Bid)
admin.site.register(Rule)
admin.site.register(Signers_bid)
admin.site.register(SourceBid)
admin.site.register(RecipientBid)
# Register your models here.
