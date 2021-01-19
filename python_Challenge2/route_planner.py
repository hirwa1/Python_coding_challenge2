def route_planner(peaks):
    peaks_list = peaks.split(" ")
    final_route = []
    for peak in peaks_list:
        if len(final_route) == 0:
            final_route.append(peak)
        elif int(peak) > int(final_route[len(final_route) - 1]):
            final_route.append(peak)
    return final_route

print(route_planner("0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15"))
