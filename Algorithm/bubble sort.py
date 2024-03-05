def bubble_sort(m):
    for i in range(1, len(m)):
        for j in range(len(m)):
            if m[i] > m[j]:
                pass
            else:
                m[i], m[j] = m[j], m[i]

    return m

print(bubble_sort([1,4,5,6,2,3,5,7,8]))