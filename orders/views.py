import json
from codecs import decode
from http import HTTPStatus

from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


from orders.models import Order
from products.models import Basket
from products.views import basket_remove_all
import uuid

from yookassa import Configuration, Payment
from common.views import TitleMixin
from orders.forms import OrderForm


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Flowers Store - Спасибо за заказ!'

class CanceledTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/canceled.html'
    title = 'Flowers Store - Заказ не был создан'


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Flowers Store - Оформление заказа'

    Configuration.account_id = '334368'
    Configuration.secret_key = 'test_4ljvb1YEGs-BBVT32GBN72ALfW1R21d25_WBVAk2EUs'

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)

        baskets = Basket.objects.filter(user=request.user)
        payment = Payment.create({
        "metadata": {"order_id":self.object.id, "user_id": request.user.id},
        "amount": {
            "value": baskets.total_sum(),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "{}{}".format(settings.DOMAIN_NAME, reverse('orders:order_success'))
        },
        "capture": True,
        "description": f"Заказ №{self.object.id}"
        }, uuid.uuid4())
        return HttpResponseRedirect(payment.confirmation.confirmation_url, status=HTTPStatus.SEE_OTHER)
    
    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
    
@csrf_exempt
def UKassa_webhook_view(request):
    payload = request.body.decode('utf-8')
    payload_dict = json.loads(payload)
    if payload_dict['object']['status'] == 'succeeded':
        baskets = Basket.objects.filter(user_id=int(payload_dict['object']['metadata']['user_id']))
        for basket in baskets:
            basket.delete()


    return HttpResponse(status = 200)
