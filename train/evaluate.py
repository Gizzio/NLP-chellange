def mrr(y_pred, y_gt):
    ret = 0
    for pred, gt in zip(y_pred, y_gt):
        for i, s in enumerate(pred, 1):
            if s == gt:
                ret += 1 / i
                continue

    return ret / len(y_gt)
