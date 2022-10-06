
def remove_element(object_to_be_removed, list_):
    """
    
    :param object_to_be_removed: string that needs to be removed from an entire list even if repeats
    :type object_to_be_removed: str
    :param list_: the iterable object that the object_to_be_removed is being removed from
    :type list_: list/str
    :return: the iterable object after all the 'object_to_be_removed' parts where removed 
    :rtype: list/str
    """

    while object_to_be_removed in list_:
        list_.remove(object_to_be_removed)
    return list_


def Rileys_question_and_answers(file_repository):
    """
    This function creates a dictionary consisting of
    all the questions and the answers to the questions
    
    :param file_repository: A repository that contains the questions and the answers(in text format)
    :type file_repository: str
    :return: A dictionary containing all the questions and answers
    :rtype: dict
    """
    question_and_answers_dict = {}
    with open(file_repository, 'r') as QnA_file:
        list_by_lines = QnA_file.read().split('\n')
        remove_element('', list_by_lines)
        
        for element in list_by_lines:
            question_and_answers_dict[element.split(' : ')[0]] = element.split(' : ')[1]


    return question_and_answers_dict


