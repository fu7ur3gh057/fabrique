from django.utils import timezone


def compare_datetime(start_time: timezone, end_time: timezone):
    current_datetime = timezone.localtime(timezone.now())
    start_time = timezone.localtime(start_time)
    print(start_time)
    print(current_datetime)
    return start_time <= current_datetime <= end_time
