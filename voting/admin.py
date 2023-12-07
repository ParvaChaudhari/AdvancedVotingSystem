from django.contrib import admin
from voting.models import Voter,PoliticalParty,Time_Num,Vote,Result
# Register your models here.

admin.site.register(Voter)
admin.site.register(PoliticalParty)
admin.site.register(Time_Num)
admin.site.register(Vote)
admin.site.register(Result)


