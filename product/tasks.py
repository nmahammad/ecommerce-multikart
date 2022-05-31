 import time
from celery import shared_task
from django.template.loader import render_to_string

from accounts.models import User
from product import
# from product.models import 

@shared_task
def process_func():
 time.sleep(10)
 return 'Proces done'



@shared_task
def send_mail_to_subscribers():
 email_list = []
 email_list = User.objects.filter(is_active=True).values_list('email',flat=True)
 mail_text = render_to_string('email-subscribers.html', {
        'products': products, 
    })
 # user_30_days_ago = 
 # products = 




@shared_task
def send_mail_to_subscribers():
    # select email from Subscriber # (('idris',), ('idris'), ('idris'))
    # email_list = Subscription.objects.filter(is_active=True).values_list('email', flat=True)
    email_list = []
    g = User.objects.filter(is_active=True).values_list('last_login','username', 'email')
    for gg in g:
        now = datetime.now(timezone.utc)
        if (now-gg[0] > timedelta(days=30)):
            email_list.append(gg[2])
    products = ProductVersion.objects.annotate(num_tags=models.Count('reviews')).filter(created_at__gte=datetime.now(timezone.utc)-timedelta(days=30)).order_by('-num_tags')[:5]
    
    mail_text = render_to_string('email-subscribers.html', {
        'products': products, 
    })    
    msg = EmailMultiAlternatives(subject='Products', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    msg.attach_alternative(mail_text, "text/html")
    msg.send()
    print(email_list)
# 1. background task
# 2. paralel
# 3. periodic task