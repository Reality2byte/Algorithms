# Tower of Hanoi algorithm using recursion
def tower_of_hanoi(n, source_rod, auxiliary_rod, target_rod, steps=None):
    """
    Solve the Tower of Hanoi problem using recursion.
    
    Parameters:
    n (int): The number of disks.
    source_rod (str): The label of the source rod.
    auxiliary_rod (str): The label of the auxiliary rod.
    target_rod (str): The label of the target rod.
    steps (list): A list to store the steps taken to solve the problem.
    
    Returns:
    list: A list of steps taken to solve the Tower of Hanoi problem.
    """
    if steps is None:
        steps = []
    
    if n == 1:
        steps.append(f"Move disk 1 from {source_rod} to {target_rod}")
        return steps
    tower_of_hanoi(n - 1, source_rod, target_rod, auxiliary_rod, steps)
    steps.append(f"Move disk {n} from {source_rod} to {target_rod}")
    tower_of_hanoi(n - 1, auxiliary_rod, source_rod, target_rod, steps)
    
    return steps

# Pytest test cases for the Tower of Hanoi algorithm
def test_tower_of_hanoi():
    assert tower_of_hanoi(1, 'A', 'B', 'C') == ["Move disk 1 from A to C"]
    assert tower_of_hanoi(2, 'A', 'B', 'C') == ["Move disk 1 from A to B", "Move disk 2 from A to C", "Move disk 1 from B to C"]
    assert tower_of_hanoi(3, 'A', 'B', 'C') == ["Move disk 1 from A to C", "Move disk 2 from A to B", "Move disk 1 from C to B", 
                                                "Move disk 3 from A to C", "Move disk 1 from B to A", "Move disk 2 from B to C", 
                                                "Move disk 1 from A to C"]
# Directly run the test function to validate the algorithm
test_tower_of_hanoi()
print("All tests passed for Tower of Hanoi algorithm.")
