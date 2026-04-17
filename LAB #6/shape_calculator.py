import geometry_utils

mode = input()


operations_map = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }


if mode == 'circle_area':
    radius = float(input())
    operations_map[mode](radius)
elif mode == 'circle_perimeter':
    radius = float(input())
    operations_map[mode](radius)
elif mode == 'rectangle_area':
    width = float(input())
    height = float(input())
    operations_map[mode](width, height)
elif mode == 'rectangle_perimeter':
    width = float(input())
    height = float(input())
    operations_map[mode](width, height)
elif mode == 'triangle_area':
    base = float(input())
    height = float(input())
    print(geometry_utils.triangle_area(base,height))

