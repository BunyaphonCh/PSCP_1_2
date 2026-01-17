class StudentNode:
    def __init__(self, sid, score):
        self.sid = sid
        self.score = score
        self.next = None
class ScoreBoard:
    def __init__(self):
        self.head = None
    def push(self, sid, score):
        new_node = StudentNode(sid, score)
        new_node.next = self.head
        self.head = new_node
def main():
    try:
        line = input()
        n = int(line)
    except:
        return
    students = ScoreBoard()
    total_score = 0.0
    for i in range(n):
        try:
            raw_input = input()
            sid, score_str = raw_input.split('\t')
            score = float(score_str)
            students.push(sid, score)
            total_score += score
        except:
            break
    if n == 0:
        return
    average = total_score / n
    best_sid = None
    best_score = -1.0
    
    current = students.head
    while current is not None:
        if current.score <= average:
            if current.score > best_score:
                best_score = current.score
                best_sid = current.sid
        current = current.next
    if best_sid is not None:
        print(str(best_sid) + '\t' + str(best_score))
    
if __name__ == '__main__':
    main()
