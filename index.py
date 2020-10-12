import math

# Calculates the distance between the xy and the point
distance = lambda x, y: math.sqrt(x ** 2 + y ** 2)

# Is the given xy coordinate a valid 3pt shot?
is_3 = lambda x, y: abs(x) > 22 or (y > 14 and distance(x, y) > 23.75)

# Make sure some points are indeed 3 point shots
tests = [(0, 23.76, True), (-23, 0, True), (0, 23.75, False), (22, 0, False), (-22, 0, False),
         (23, -3, True), (-23, -3, True)]

# Test my sample test cases
for x, y, exp in tests:
    assert(exp == is_3(x, y))

# Here's a naive solution not using Pandas and just using built-in libs:

# Go line-by-line in the CSV ignoring the header, and convert each entry to float
# shots should be a list of tuples of the structure [(x, y, fgmade?), ...] where x, y, and fgmade are floats
shots = [tuple(map(float, line.split(',')))
            for line in open('shots_data.csv', 'r').read().split('\n')[1:]]

for x, y, fgmade in shots:
    print(x, y, distance(x, y), is_3(x, y))

# get the 2-point and 3-point shots in two lists
pts_2 = [fgmade for x, y, fgmade in shots if not is_3(x, y)]
pts_3 = [fgmade for x, y, fgmade in shots if is_3(x, y)]

# Computes the average of a list
avg_fg = lambda l: sum(l) / len(l)

print("2 PT FG%:", avg_fg(pts_2))
print("3 PT FG%:", avg_fg(pts_3))

def with_pandas():
    # Not sure if I'm allowed to use Pandas. Here's a solution using Pandas
    import pandas as pd

    print("--- USING PANDAS ---")

    df = pd.read_csv('shots_data.csv')
    df['value'] = [3 if is_3(row['x'], row['y']) else 2 for i, row in df.iterrows()]
    pts_2 = df[df['value'] == 2].agg('mean')['fgmade']
    print("2PT FG%", pts_2)

    pts_3 = df[df['value'] == 3].agg('mean')['fgmade']
    print("3PT FG%", pts_3)

# Uncomment to use Pandas
with_pandas()