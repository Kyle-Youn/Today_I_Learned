def solution(skill, skill_trees):
    answer = 0
    skill_list = []
    skill_dict = {}
    
    for element_list in skill:
        skill_list.append(element_list)
    
    for element_dict in skill:
        skill_dict[element_dict] = 1
    
    for skill_tree in skill_trees:
        start = 0
        for element in skill_tree:
            if element in skill_dict and skill_list[start] == element:
                start += 1
            if start == len(skill):
                answer += 1
                
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)