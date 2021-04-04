"""
Sometimes damaged nodes are unrecoverable.
In that case, people that were connected to the crushed node must migrate to another district while administration attempts to fix the node.
But if a crushed node disconnects multiple districts from one another,then the network splits into two sub-networks and every sub-network should have their own Mayor.
And Mayors must use pigeons for mailing between each other. In that case, when the network is split you don’t need hundreds of pigeons.
Your mission is to figure out how many Mayors you need to control the entire city when some nodes are crushed.
In other words, you need to figure out how many sub-networks will be formed after some nodes are crush and not recovered.

Input: Two arguments: the network structure (as a list of connections between the nodes) and the list of crashed nodes.
Output: Int. The amount of sub-networks formed after some nodes were crushed.
"""

def subnetworks(net: list, crushes: list) -> int:    

    nodes: set = set([node for connection in net for node in connection])
    print(f"list of nodes {nodes}")
    subnet: list = []
    for node in nodes:
        result: list = []
        
        flat_subnet: list = [item for subl in subnet for item in subl]
        if node in flat_subnet or node in crushes:
            print(f'{node} already exit in subnet or {node} is cruched')
            continue
        
        for connection in net:
            if node in connection:
                result.extend(connection)
        
        subnet.append(list(set(result)))
    print(f"subnet : {subnet}")
    return len(subnet)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['B']) == 2, "First"
    assert subnetworks([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['D', 'F']
    ], ['A']) == 3, "Second"
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
