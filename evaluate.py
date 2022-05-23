from typing import Iterable


def mean_reciprocal_rank(y_pred: Iterable[Iterable[str]], y_gt: Iterable[str]) -> float:
    ret = 0
    for pred, gt in zip(y_pred, y_gt):
        for i, s in enumerate(pred, 1):
            if s.strip().lower() == gt.strip().lower():
                ret += 1 / i
                continue
                
    return ret / len(y_gt)
