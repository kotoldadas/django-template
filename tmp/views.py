from django.shortcuts import render
from datetime import datetime, timezone

# Create your views here.


def index(req):
    print(f"time now => {datetime.now()}")
    print(f"time now timestamp => {datetime.now().astimezone()}")
    print(f"time utc-0=> {datetime.now(timezone.utc)}")
    print(f"time utc-0 timestamp=> {datetime.now(timezone.utc).timestamp()}")
    return render(req, "index.html")
