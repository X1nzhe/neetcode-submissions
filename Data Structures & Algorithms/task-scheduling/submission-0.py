class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        case 1 (no idle)
        n = 2, tasks = [A,A,A,B,B,B,C,C,C,D,D,D]

        A B C D
        A B C D
        A B C D
        A B C D

        time = len(tasks)


        case 2
        tasks = ["A","A","A","B","C"], n = 3

        A B C - 
        A - - -
        A

        col = n + 1
        full rows = most occurrences of a task - 1
        last row = num of tasks at max occurrences

        """
        count = Counter(tasks) 
        max_count = max(count.values())
        num_peak_tasks = sum(1 for c in count.values() if c == max_count)
        full_row = max_count - 1
        col = n + 1
        last_row = num_peak_tasks
        return max(len(tasks), full_row * col + last_row )

        
        
        