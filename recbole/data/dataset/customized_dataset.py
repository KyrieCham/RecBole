# @Time   : 2020/10/19
# @Author : Yupeng Hou
# @Email  : houyupeng@ruc.edu.cn

"""
recbole.data.customized_dataset
##########################
"""

from recbole.data.dataset import Kg_Seq_Dataset


class GRU4RecKGDataset(Kg_Seq_Dataset):
    def __init__(self, config, saved_dataset=None):
        super().__init__(config, saved_dataset=saved_dataset)