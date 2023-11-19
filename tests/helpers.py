from src.data_structures.linked_list import LinkedList


def list_to_linked_list(nums : list[int]) -> LinkedList:
    root = LinkedList(nums[0])
    head = root
    
    for i in range(1, len(nums)):
        new_node = LinkedList(nums[i])
        head.next=new_node
        head = head.next
    
    
    return root


def are_lists_equal(l1 : list, l2 : list) -> bool:
    assert len(l1) == len(l2) and sorted(l1) == sorted(l2)