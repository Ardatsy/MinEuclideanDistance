def euclideanDistance(p1,p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)**0.5

def distances(points):
    distance_list=[]
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distance_list.append(distance) 
            
    return distance_list

#EXAMPLE
points = [(1,2),(1,7),(5,5),(4,7)]
x=min(distances(points))
print('Minimun distance is',x)







    


