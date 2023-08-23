from celery import shared_task
import logging

from .email import send_review_email

logger = logging.getLogger(__name__)


@shared_task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    logger.info("Sent review email")
    return send_review_email(name, email, review)