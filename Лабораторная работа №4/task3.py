def delete(list_, index=None):
    if index is None:
        list_ = list_[:-1]  # удаление последнего элемента по индексу
    else:
        list_ = list_[0:index] + list_[index+1:]
    return list_  # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
