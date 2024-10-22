import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import time

root = tk.Tk()
root.title("Sorting Algorithm Visualizer By Group_16")
root.geometry("800x600")
root.config(bg="white")     

canvas_width = 700
canvas_height = 400

arr = []
bars = []

algo_list = ['Merge Sort', 'Selection Sort', 'Bubble Sort', 'Insertion Sort', 'Quick Sort', 'Heap Sort']
speed_list = ['Fast', 'Medium', 'Slow']
speed = 0.1


def generate_array():
    global arr, bars
    arr = []
    canvas.delete("all")
    bars.clear()

    size = int(size_entry.get())

    for _ in range(size):
        value = random.randint(1, 100)
        arr.append(value)

    bar_width = canvas_width / size
    offset = bar_width / 2

    for i, value in enumerate(arr):
        x0 = i * bar_width + offset
        y0 = canvas_height - value * 3
        x1 = (i + 1) * bar_width + offset
        y1 = canvas_height
        bar = canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        bars.append(bar)


def display_arr(arr, colors):
    canvas.delete("all")

    bar_width = canvas_width / len(arr)
    offset = bar_width / 2

    for i, value in enumerate(arr):
        x0 = i * bar_width + offset
        y0 = canvas_height - value * 3
        x1 = (i + 1) * bar_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])

    root.update()


def set_speed():
    selected_speed = speed_comboBox.get()

    if selected_speed == 'Fast':
        return 0.01
    elif selected_speed == 'Medium':
        return 0.1
    elif selected_speed == 'Slow':
        return 0.5
    else:
        return 0.1  # Default speed


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [arr[left + i] for i in range(n1)]
    R = [arr[mid + 1 + i] for i in range(n2)]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    display_arr(arr, ["yellow" if left + i <= k <= mid or mid + 1 + j <= k <= right else "blue" for k in range(len(arr))])
    time.sleep(speed)


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

    display_arr(arr, ["blue"] * len(arr))


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        display_arr(arr, ["yellow" if k <= i else "blue" for k in range(len(arr))])
        time.sleep(speed)


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

            display_arr(arr, ["yellow" if k == j or k == j + 1 else "blue" for k in range(len(arr))])
            time.sleep(speed)
            

        if not swapped:
            break


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        display_arr(arr, ["yellow" if k == i or k == j + 1 else "blue" for k in range(len(arr))])
        time.sleep(speed)


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    display_arr(arr, ["blue"] * len(arr))


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

        display_arr(arr, ["yellow" if k == 0 or k == i else "blue" for k in range(len(arr))])
        time.sleep(speed)


def sort():
    global speed
    global selected_algo
    selected_algo = algo_comboBox.get()
    speed = set_speed()

    if selected_algo == 'Merge Sort':
        merge_sort(arr, 0, len(arr) - 1)
        display_arr(arr, ["blue"] * len(arr))
    elif selected_algo == 'Selection Sort':
        selection_sort(arr)
    elif selected_algo == 'Bubble Sort':
        bubble_sort(arr)
    elif selected_algo == 'Insertion Sort':
        insertion_sort(arr)
    elif selected_algo == 'Quick Sort':
        quick_sort(arr, 0, len(arr) - 1)
        display_arr(arr, ["blue"] * len(arr))
    elif selected_algo == 'Heap Sort':
        heap_sort(arr)

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(pady=20)

frame = tk.Frame(root, bg="white")
frame.pack(pady=10)

size_label = tk.Label(frame, text="Enter Array Size:", bg="white")
size_label.grid(row=0, column=0, padx=3)

size_entry = ttk.Entry(frame, width=10)
size_entry.grid(row=0, column=1, padx=5)

generate_button = ttk.Button(frame, text="Generate Array", command=generate_array)
generate_button.grid(row=0, column=2, padx=5)

# algo_label = tk.Label(frame, text="Sorting Algorithm:", bg="white")
# algo_label.grid(row=1, column=0, padx=5)
algo_frame = tk.LabelFrame(frame, text="Time Complexity", bg="white")
algo_frame.grid(row=1, column=0, padx=10, pady=10)

algo_comboBox = ttk.Combobox(frame, values=algo_list, state="readonly")
algo_comboBox.grid(row=1, column=1, padx=5)



speed_label = tk.Label(frame, text="Speed:", bg="white")
speed_label.grid(row=1, column=2, padx=5)

speed_comboBox = ttk.Combobox(frame, values=speed_list, state="readonly")
speed_comboBox.grid(row=1, column=3, padx=5)

sort_button = ttk.Button(frame, text="Sort", command=sort)
sort_button.grid(row=1, column=4, padx=5)

# Function to update complexity label based on selected algorithm
def update_complexity(event):
    selected_algo = algo_comboBox.get()

    if selected_algo == 'Merge Sort':
        complexity_label.config(text="O(nlogn)")
    elif selected_algo == 'Selection Sort':
        complexity_label.config(text="O(n^2)")
    elif selected_algo == 'Bubble Sort':
        complexity_label.config(text="O(n^2)")
    elif selected_algo == 'Insertion Sort':
        complexity_label.config(text="O(n^2)")
    elif selected_algo == 'Quick Sort':
        complexity_label.config(text="O(n^2)")
    elif selected_algo == 'Heap Sort':
        complexity_label.config(text="O(nlogn)")

complexity_label = tk.Label(algo_frame, text="", bg="white")
complexity_label.pack(side=tk.LEFT, padx=10, pady=10)

# Bind the update_complexity function to the algorithm dropdown menu
algo_comboBox.bind("<<ComboboxSelected>>", update_complexity)

# Call the update_complexity function once initially to display complexity for the first algorithm in the list
update_complexity(None)

root.mainloop()

   