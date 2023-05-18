from map.models import HeadCount, CountHistory
from events.models import Event
from django.db.models import Sum
from datetime import datetime

def updateCountHistory():
    print(datetime.now())
    headcounts = HeadCount.objects.values("event_id").annotate(Sum('count'))
    for headcount in headcounts:
        print(datetime.now())
        history = CountHistory(count=headcount["count__sum"])
        history.event_id = Event.objects.get(id=headcount["event_id"])
        history.save()