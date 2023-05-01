# Bubble sort in Python

def bubbleSort(a):
    
  # loop to access each array element
  for i in range(len(a)):

    # loop to compare array elements
    for j in range(0, len(a) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if a[j] > a[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        var = a[j]
        a[j] = a[j+1]
        a[j+1] = var


data = [-2, 45, 0, 11, -9, 30, 53, 90, 21, 36, 28, 77, 54, 38, 67]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
