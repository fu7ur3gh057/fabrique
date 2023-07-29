from celery import shared_task
from django.db.models import Q

from other.enums import Status
from utils.api_client import send_message_api
from apps.client.models import Client
from apps.distribution.models import Distribution, Message
from utils.datetime_utils import compare_datetime
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(name='send_messages_task')
def send_messages_task() -> None:
    logger.info('start sending messages')
    distribs = Distribution.objects.all()
    # compare dates, get active distributions
    active_list = [i for i in distribs if compare_datetime(start_time=i.start_time, end_time=i.end_time)]
    logger.info(f'active distributions size - {len(active_list)}')
    for distribution in active_list:
        receivers = []
        # get clients by distribution filter
        for i in distribution.filter:
            # could be operator_code
            if i.isnumeric():
                clients = Client.objects.filter(Q(operator_code=int(i)) | Q(tag__iexact=i)).all()
            # only tag
            else:
                clients = Client.objects.filter(tag__iexact=i).all()
            if len(clients) != 0:
                receivers.extend(clients)
        for receiver in receivers:
            messages = receiver.messages.all()
            if messages.filter(distribution=distribution).first() is not None:
                continue
            msg = Message.objects.create(client=receiver, distribution=distribution)
            # send message to receivers using external API
            data = {'id': msg.pk_id, 'phone': receiver.phone_number, 'text': distribution.text}
            result = send_message_api(data=data)
            if result:
                msg.status = Status.SUCCESS
            else:
                msg.status = Status.ERROR
            msg.save()
    logger.info('finish sending messages')
    return None


@shared_task(name='retry_send_error_messages_task')
def retry_send_error_messages_task() -> None:
    logger.info('start sending error tasks')
    error_messages = Message.objects.filter(status=Status.ERROR).all()
    for msg in error_messages:
        distribution = msg.distribution
        if compare_datetime(start_time=distribution.start_time, end_time=distribution.end_time):
            data = {'id': msg.pk_id, 'phone': msg.client.phone_number, 'text': msg.distribution.text}
            result = send_message_api(data=data)
            if result:
                msg.status = Status.SUCCESS
        else:
            msg.status = Status.EXPIRED
        msg.save()
    logger.info('finish sending error tasks')
    return None
