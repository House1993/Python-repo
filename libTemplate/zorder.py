__author__ = 'Fang'

'''
z order curve
use dfs() to get the NODE_LIST's z order list
parameters are the 4 edges of the area and node list
'''


def dfs(top_edge, bottom_edge, left_edge, right_edge, node_list):
    if top_edge == bottom_edge or left_edge == right_edge:
        return sorted(node_list)
    mid_top_bottom = (top_edge + bottom_edge) / 2
    mid_left_right = (left_edge + right_edge) / 2
    lis_left_top = []
    lis_right_top = []
    lis_left_bottom = []
    lis_right_bottom = []
    for item in node_list:
        if item[0] <= mid_left_right:
            if item[1] <= mid_top_bottom:
                lis_left_top.append(item)
            else:
                lis_left_bottom.append(item)
        else:
            if item[1] <= mid_top_bottom:
                lis_right_top.append(item)
            else:
                lis_right_bottom.append(item)
    result = []
    result.extend(dfs(top_edge, mid_top_bottom, left_edge, mid_left_right, lis_left_top))
    result.extend(dfs(top_edge, mid_top_bottom, mid_left_right + 1, right_edge, lis_right_top))
    result.extend(dfs(mid_top_bottom + 1, bottom_edge, left_edge, mid_left_right, lis_left_bottom))
    result.extend(dfs(mid_top_bottom + 1, bottom_edge, mid_left_right + 1, right_edge, lis_right_bottom))
    return result


if __name__ == "__main__":
    data = list()
    inf = 999999999999999999999999999
    up = inf
    down = -inf
    left = inf
    right = -inf
    with open("in", "r") as infile:
        for line in infile:
            sp = line.strip().split("\t")
            x = int(sp[0])
            y = int(sp[1])
            v = int(sp[2])
            data.append((x, y, v))
            up = min(up, y)
            down = max(down, y)
            left = min(left, x)
            right = max(right, x)
    res = dfs(up, down, left, right, data)
    with open("out", "w") as outfile:
        for itm in res:
            outfile.write(itm)
