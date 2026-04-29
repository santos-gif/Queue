import streamlit as st
import time

class Node: 
        def __init__(self, value):
                """
                A Node consists of a value and a next attribute which is used to point to the next node
                """
                self.value = value
                self.next = None
class Queue:
        def __init__(self):
                """
                Instantiating the Queue creates tail and head
                """
                self.tail = None
                self.head = None

        
        def enqueue(self, item):
                """
                Creates a new node using the item as the value of the node
                if the tail is None -> Queue is empty -> head and tail is now the same node(the new node)
                else the tail is not None -> current tail points to this new node -> new node becomes the new tail
                """
                new_node = Node(item)
                if self.tail is None:
                        self.head = new_node
                        self.tail = new_node
                        return
                self.tail.next = new_node
                self.tail = new_node
        
        def dequeue(self) -> None | int:
                """
                Returns None if the Queue is Empty else returns the value of the head
                """
                if self.is_empty():
                        return None
                
                removed_value = self.head.value
                self.head = self.head.next

                if self.head is None:
                        self.tail = None
                return removed_value
        
        def is_empty(self) -> bool:
                """
                Boolean check that checks if the queue is empty via the head
                """
                return self.head is None

        def peek(self) -> None | int:
                """
                Returns the first element/head 
                """
                return self.head.value if self.head else None
        
        def to_list(self) -> list:
                items = []
                current = self.head
                while current:
                        items.append(current.value)
                        current = current.next
                return items


def main():
        st.title("Queue Visualizer")

        # Initialize the queue in session state if it doesn't exist
        if 'my_queue' not in st.session_state:
                st.session_state.my_queue = Queue()

        queue = st.session_state.my_queue

        # UI Inputs
        item_input = st.text_input("Enter item:")
        col1, col2, col3 = st.columns(3)

        if col1.button("Enqueue"):
                if item_input:
                        time_start = time.time()
                        queue.enqueue(item_input)
                        time_end = time.time()
                        st.success(f"Added {item_input} | Operation Time : {(time_end - time_start):.4f}s")
                else:
                        st.error(f"Please input an item")

        if col2.button("Dequeue"):
                time_start = time.time()
                removed = queue.dequeue()
                time_end = time.time()
                if removed:
                        st.warning(f"Removed {removed} | Operation Time : {(time_end - time_start):.4f}s")
                else:
                        st.error("Queue is empty!")
        
        if col3.button("Peek"):
                time_start = time.time()
                val = queue.peek()
                time_end = time.time()
                if val is not None:
                        st.info(f"Peek {val} | Operation Time : {(time_end - time_start):.4f}s")
                else:
                        st.error("Queue is empty!")

        # --- SHOWING THE ITEMS ---
        st.subheader("Current Queue:")
        current_items = queue.to_list()
        
        if not current_items:
                st.write("The queue is currently empty.")
        else:
                # Display as a list or a pretty arrow-separated string
                st.write(" → ".join([str(i) for i in current_items]))
                st.json(current_items) # Another way to visualize
        # 4. Analisis Kompleksitas (Big-O)
        st.divider()
        st.subheader("Complexity Analysis (Big-O)")
        col1, col2, col3 = st.columns(3)
        with col1:
                st.metric("Enqueue Complexity", "O(1)")
                st.write("Adding an item to the end of the list takes constant time.")
        with col2:
                st.metric("Dequeue Complexity", "O(1)")
                st.write("Removing the first item takes constant time.")
        with col3:
                st.metric("Peek Complexity", "O(1)")
                st.write("Peeking the first item takes constant time.")
main()