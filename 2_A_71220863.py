def buatKata(str):
    strLength = len(str)
    if strLength % 2 == 0:
       return str[0] + str[1]+str[2],"dan",str[-3]+ str[-2],str[1]
    else :
        midle = int(strLength/2)
        return str[midle - 1 ]+ str[midle]+str[midle+1]
word = input("Masukkan Kata ")
then = buatKata(word)
print("Huruf yang di ambil pada kata ", word,"adalah",then)


Berikut adalah implementasi kodenya:

```python
class PriorityQueueSorted:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def remove(self):
        if not self.is_empty():
            self.queue.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def add(self, data, priority):
        self.queue.append((data, priority))
        self.queue = sorted(self.queue, key=lambda x: x[1], reverse=True)

    def print_all(self):
        print([item[0] for item in self.queue])

# TEST CASE
myQueue = PriorityQueueSorted()

myQueue.add('Gian', 2)
myQueue.add('Kezia', 8)

myQueue.print_all()

print("Peek:", myQueue.peek())

myQueue.add('Glen', 5)
myQueue.add('Christo', 9)

myQueue.print_all()

print("Peek:", myQueue.peek())

print("========REMOVE========")

myQueue.remove()
myQueue.print_all()

myQueue.remove()
myQueue.print_all()

myQueue.remove()
myQueue.print_all()

myQueue.add('Saya', 7)
myQueue.print_all()
```

Jalankan kode di atas untuk menguji implementasinya sesuai dengan test case yang diberikan.