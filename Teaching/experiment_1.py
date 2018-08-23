'''
Traffic Assignment in python.
expriment 1
'''

class Node:
        def __init__(self):
                self.node_id = 0
                self.x = 0.0
                self.y = 0.0

def g_ReadInputData():
        g_node_list = []
        g_number_of_nodes = 0
        with open('input_node.csv','r') as fp:
                lines = fp.readlines()   
                for l in lines[1:]:
                    l = l.strip().split(',')  
                    node = Node()
                    node.node_id = int(l[1])
                    node.x = float(l[3])
                    node.y = float(l[4])
                    print (node.node_id, node.x, node.y)
                                
                    g_node_list.append(node)
                    g_number_of_nodes += 1
                               
                print('nodes_numbers:{}'.format(g_number_of_nodes))

              
if __name__=='__main__':
        print('Reading data......')
        g_ReadInputData()
 