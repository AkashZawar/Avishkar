from .models import Code

all_entries = Code.objects.all()
print(all_entries)