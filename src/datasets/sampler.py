import torch
from torch.utils.data import Sampler, ConcatDataset
import random
import torch
from torch.utils.data import Sampler, ConcatDataset


class RandomConcatSampler(Sampler):
    def __init__(self,
                 data_source: ConcatDataset,
                 n_samples_per_subset: int,
                 subset_replacement: bool=True,
                 seed: int=None,
                 ):
        if not isinstance(data_source, ConcatDataset):
            raise TypeError("data_source should be torch.utils.data.ConcatDataset")
        
        self.data_source = data_source
        self.n_subset = len(self.data_source.datasets)
        self.n_samples_per_subset = n_samples_per_subset
        self.n_samples = self.n_subset * self.n_samples_per_subset 
        self.subset_replacement = subset_replacement
        self.generator = torch.manual_seed(seed)
        
    def __len__(self):
        return self.n_samples
    
    def __iter__(self):
        indices = []
        # sample from each sub-dataset
        for d_idx in range(self.n_subset):
            low = 0 if d_idx==0 else self.data_source.cumulative_sizes[d_idx-1]
            high = self.data_source.cumulative_sizes[d_idx]
            
            if self.subset_replacement:
                rand_tensor = torch.randint(low, high, (self.n_samples_per_subset, ),
                                            generator=self.generator, dtype=torch.int64)
            else:  # sample without replacement
                len_subset = len(self.data_source.datasets[d_idx])
                rand_tensor = torch.randperm(len_subset, generator=self.generator) + low
                if len_subset >= self.n_samples_per_subset:
                    rand_tensor = rand_tensor[:self.n_samples_per_subset]
                else: # padding with replacement
                    rand_tensor_replacement = torch.randint(low, high, (self.n_samples_per_subset - len_subset, ),
                                                            generator=self.generator, dtype=torch.int64)
                    rand_tensor = torch.cat([rand_tensor, rand_tensor_replacement])
            indices.append(rand_tensor)
        indices = torch.stack(indices)
        indices=indices.permute(1, 0).reshape(-1)
       
        assert indices.shape[0] == self.n_samples
        return iter(indices.tolist())