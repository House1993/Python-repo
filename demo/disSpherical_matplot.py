import iofiles
import matplotlib.pyplot as plt
import math

ID = "207707"
MAX = 1e20
Min_lat, Max_lat, Min_lon, Max_lon, Num_lat, Num_lon, Num_grids = \
    27.1470214, 35.1779993, 116.3180252, 122.4807201, 804, 617, 496068
STEP = 0.01
color = ['r', 'g', 'b']
RADIUS = 6371000


def cal_dis(s_lat, s_lon, e_lat, e_lon):
    s_lat = math.radians(s_lat)
    s_lon = math.radians(s_lon)
    e_lat = math.radians(e_lat)
    e_lon = math.radians(e_lon)
    theta_lat = s_lat - e_lat
    theta_long = s_lon - e_lon
    first = pow(math.sin(theta_lat / 2.0), 2)
    second = math.cos(s_lat) * math.cos(e_lat) * pow(math.sin(theta_long / 2.0), 2)
    angle = 2 * math.asin(math.sqrt(first + second))
    return math.floor(RADIUS * angle + 0.5)


def get_range(grid_id):
    x = grid_id / Num_lon
    y = grid_id % Num_lon
    loc_x = Min_lat + STEP * x
    loc_y = Min_lon + STEP * y
    return [loc_x, loc_x + STEP, loc_y, loc_y + STEP]


if __name__ == "__main__":
    rang = get_range(int(ID))
    plt.axis(rang)
    grid = iofiles.read_json(ID)
    i = 0
    max_dis = -MAX
    min_dis = MAX
    for item in grid:
        it = item.values()[0]
        s = it[u"s_node"]
        e = it[u"e_node"]
        plt.plot([s[0], e[0]], [s[1], e[1]], color[i])
        i = (i + 1) % 3
        dis = cal_dis(s[0], s[1], e[0], e[1])
        max_dis = max(max_dis, dis)
        min_dis = min(min_dis, dis)
    print max_dis, min_dis
    plt.show()
