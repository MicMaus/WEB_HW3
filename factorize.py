from datetime import datetime
from multiprocessing import Pool, cpu_count

"""sync function"""


def factorize(*number):
    final_result = []
    for num in number:
        dividers_list = []
        for divider in range(1, num + 1):
            if num % divider == 0:
                dividers_list.append(divider)

        final_result.append(dividers_list)
    return final_result


"""async function, 
time of sync vs async func processing: 2.4  vs 1.65 sec"""


def optimized_factorize(*number):
    arguments_list = []
    for num in number:
        arguments_list.append(num)
    with Pool(cpu_count()) as pool:
        result = pool.map(processing, arguments_list)
    return result


def processing(number):
    dividers_list = []
    for divider in range(1, number + 1):
        if number % divider == 0:
            dividers_list.append(divider)
    return dividers_list


"""run of functions with time measurement"""
start = datetime.now()
print(factorize(128, 255, 99999, 10651060, 21302120))
# print(optimized_factorize(128, 255, 99999, 10651060, 21302120))
end = datetime.now()

timer = end - start
print(timer.total_seconds())
