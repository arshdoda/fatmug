import random
import operator
from django.utils import timezone
from apps.po.models import PO
from apps.vendors.models import Vendor

operators = {
    '+': operator.add, 
    '-': operator.sub
}

def random_date(start, end):
    d1 = timezone.datetime.strptime(start, '%Y-%m-%d').astimezone()
    d2 = timezone.datetime.strptime(end, '%Y-%m-%d').astimezone()
    delta = d2 - d1
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return d1 + timezone.timedelta(seconds=random_second)


vendor_list = []
for i in range(10):
    v = {"name": f"Vendor {i}", "contact_details": f"Phone Number {i}",
         "address": f"Address {i}", "on_time_delivery_rate": 0.0, "quality_rating_avg": 0.0, 
         "average_response_time": 0.0, "fulfillment_rate": 0.0}
    vendor_list.append(Vendor(**v))

Vendor.objects.bulk_create(vendor_list)

po_list = []
for i in range(100000):
    order_date = random_date("2023-11-01", "2023-11-22")
    expected_delivery_date = order_date + timezone.timedelta(days=random.randint(1,7))
    
    op = random.choice(list(operators.keys()))
    actual_delivery_date = operators[op](expected_delivery_date, timezone.timedelta(days=random.randint(1,2))) 
    
    issue_date = order_date + timezone.timedelta(days=random.randint(1,2)) 
    acknowledgment_date = [issue_date + timezone.timedelta(days=random.randint(2,3)), None] 

    items = {f"item {random.randint(11,20)}" : random.randint(1,5), f"item {random.randint(21,30)}" : random.randint(1,5)}
    p = {"vendor":random.choice(vendor_list), "order_date": order_date, 
         "expected_delivery_date":expected_delivery_date, "actual_delivery_date":actual_delivery_date,
         "items":items, "quantity":random.randint(1,3), "status":"pending", "quality_rating":random.randint(1,5),
         "issue_date":issue_date, "acknowledgment_date":random.choice(acknowledgment_date)}
    po_list.append(PO(**p))

PO.objects.bulk_create(po_list, batch_size=50000)
