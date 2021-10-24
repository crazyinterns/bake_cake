from django.shortcuts import render
import csv
from django.http import HttpResponse
from statistic.stat_functions import get_stats


def show_admin_stat_page(request):
    return render(request, 'statistic/admin_summary_stat.html', context=get_stats())

def get_csv_stats(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stats.csv"'

    stats = get_stats()

    writer = csv.writer(response)

    # users
    writer.writerow(['Пользователи', 'Всего'])
    writer.writerow(['Клиенты(совершили заказ)', stats['customers']])
    writer.writerow(['Зарегистрированных пользователей', stats['all_users']])

    # orders
    writer.writerow(['Cтатистика по заказам'])
    writer.writerow(['Статус', 'Количество заказов'])
    for order_status in stats['orders_by_status']:
        writer.writerow([order_status['get_status_display'], order_status['count']])
    writer.writerow(['Итого', stats['total_orders_count']])

    # forms
    writer.writerow(['Статистика по формам торта'])
    writer.writerow(['Форма', 'Количество заказов'])
    for form, count in stats['orders_by_forms'].items():
        writer.writerow([form, count])

    # layers
    writer.writerow(['Статистика по формам торта'])
    writer.writerow(['Количество слоёв', 'Количество заказов'])
    for layer, count in stats['orders_by_layers'].items():
        writer.writerow([layer, count])

    # toppings
    writer.writerow(['Статистика по топпингам'])
    writer.writerow(['Топпинг', 'Количество заказов'])
    for top, count in stats['toppings_by_orders'].items():
        writer.writerow([top, count])

    # berry
    writer.writerow(['Статистика по ягодам'])
    writer.writerow(['Ягоды', 'Количество заказов'])
    for berry, count in stats['berries_by_orders'].items():
        writer.writerow([berry, count])

    # decoration
    writer.writerow(['Статистика по декору'])
    writer.writerow(['Декор', 'Количество заказов'])
    for decor, count in stats['decors_by_orders'].items():
        writer.writerow([decor, count])

    return response
