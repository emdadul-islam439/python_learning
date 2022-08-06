n, m, a, b = map(int, input().split())

one_ride_ticket_cost = a * n
only_special_ticket_cost = b * (0 - n//-m)
special_and_one_ride_cost = b*int(n/m) + a*(n%m)

print(min([one_ride_ticket_cost, only_special_ticket_cost, special_and_one_ride_cost]))