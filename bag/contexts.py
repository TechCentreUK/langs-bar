from django.shortcuts import get_object_or_404
from events.models import Event


def bag_contents(request):
    """
    Bag contents contexts.py.
    Get sessions bag contents and total price
    and work out the sum based on the quantity
    of the item in the bag.
    """
    bag_items = []
    total = 0
    event_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            event = get_object_or_404(Event, pk=item_id)
            total += item_data * event.price
            event_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'event': event,
            })
        else:
            event = get_object_or_404(Event, pk=item_id)
            for quantity in item_data['quantity'].items():
                total += quantity * event.price
                event_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'event': event,
                })

    context = {
        'bag_items': bag_items,
        'total': total,
        'event_count': event_count,
    }

    return context
