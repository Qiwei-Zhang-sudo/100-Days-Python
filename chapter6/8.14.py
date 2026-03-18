def make_car(make, model, **others):
    ''' 创建一个字典，并保存车辆的信息 '''
    car_info = {'make': make, 'model': model,}
    car_info.update(others)
    return car_info

car = make_car('xiaomi', 'su7',color='yellow',)
for key, value in car.items():
    print(f'{key}: {value}')
