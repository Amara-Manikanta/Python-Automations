import threading
import queue


def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))


def print_square(count,row,q1):
    """
    function to print square of given num
    """
    count +=1
    row +=1
    q1.put(count)
    #q1.put(row)
   # print("Square: {}".format(num * num))


if __name__ == "__main__":
    count=0
    row=0
    print('hi')
    # creating thread
    q1=queue.Queue()
    t1 = threading.Thread(target=print_square, args=(count,row,q1))
   # t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    #t2.start()
    # wait until thread 1 is completely executed
    t1.join()
    count=q1.get()
    #row=q1.get()
    print('count post',count)
    print('row post', row)



    # wait until thread 2 is completely executed
   # t2.join()

    # both threads completely executed
    print("Done!")



