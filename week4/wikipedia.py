import sys
import collections
from collections import deque

class Wikipedia:

    # Initialize the graph of pages.
    def __init__(self, pages_file, links_file):

        # A mapping from a page ID (integer) to the page title.
        # For example, self.titles[1234] returns the title of the page whose
        # ID is 1234.
        self.titles = {}

        # A set of page links.
        # For example, self.links[1234] returns an array of page IDs linked
        # from the page whose ID is 1234.
        self.links = {}

        # Read the pages file into self.titles.
        with open(pages_file) as file:
            for line in file:
                (id, title) = line.rstrip().split(" ")
                id = int(id)
                assert not id in self.titles, id
                self.titles[id] = title
                self.links[id] = []
        print("Finished reading %s" % pages_file)

        # Read the links file into self.links.
        with open(links_file) as file:
            for line in file:
                (src, dst) = line.rstrip().split(" ")
                (src, dst) = (int(src), int(dst))
                assert src in self.titles, src
                assert dst in self.titles, dst
                self.links[src].append(dst)
        print("Finished reading %s" % links_file)
        print()


    # Find the longest titles. This is not related to a graph algorithm at all
    # though :)
    def find_longest_titles(self):
        titles = sorted(self.titles.values(), key=len, reverse=True)
        print("The longest titles are:")
        count = 0
        index = 0
        while count < 15 and index < len(titles):
            if titles[index].find("_") == -1:
                print(titles[index])
                count += 1
            index += 1
        print()


    # Find the most linked pages.
    def find_most_linked_pages(self):
        link_count = {}
        for id in self.titles.keys():
            link_count[id] = 0

        for id in self.titles.keys():
            for dst in self.links[id]:
                link_count[dst] += 1

        print("The most linked pages are:")
        link_count_max = max(link_count.values())
        for dst in link_count.keys():
            if link_count[dst] == link_count_max:
                print(self.titles[dst], link_count_max)
        print()


    # Find the shortest path.
    # |start|: The title of the start page.
    # |goal|: The title of the goal page.
    def find_shortest_path(self, start, goal):
        # title->id
        start_id = self.get_id_from_title(start)
        goal_id = self.get_id_from_title(goal)

        queue = deque()
        visited = set() #前に調べたノードをたどらないようにする
        queue.append((start_id,[start_id])) #ノードとそこまでのパスを一緒に保存
        print(queue)
        visited.add(start_id)

        while queue:
            (node_id, path) = queue.popleft()

            #辿り着いたときパスを出力
            if node_id == goal_id:
                shortest_path = []
                for node in path:
                    title = self.titles[node]
                    shortest_path.append(title)
                print(f'shortest_path={shortest_path}')
                return

            for child_id in self.links[node_id]:
                if child_id not in visited:
                    visited.add(child_id)
                    queue.append((child_id, path + [child_id]))
                    print(queue)

        print("Path not found")

        return None

    def get_id_from_title(self, title):
        for page_id, page_title in self.titles.items():
            if page_title == title:
                return page_id
        return None



    # Calculate the page ranks and print the most popular pages.
    def find_most_popular_pages(self):
        # rank_list = 
        #------------------------#
        # Write your code here!  #
        #------------------------#
        pass


    # Do something more interesting!!
    def find_something_more_interesting(self):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: %s pages_file links_file" % sys.argv[0])
        exit(1)

    wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    # wikipedia.find_longest_titles()
    # wikipedia.find_most_linked_pages()
    wikipedia.find_shortest_path("C", "F")
    # wikipedia.find_most_popular_pages()

# test用
# print(self.get_id_from_title(self, title))