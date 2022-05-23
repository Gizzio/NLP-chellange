from load_data import load


def load_train():
    X_train, X_train_candidates, Y_train = load('train/in.tsv', 'train/expected.tsv')
    return X_train, X_train_candidates, Y_train


def load_dev():
    X_dev, X_dev_candidates, Y_dev = load('dev-0/in.tsv', 'dev-0/expected.tsv')
    return X_dev, X_dev_candidates, Y_dev
    
    
def load_test():
    X_test, X_test_candidates, _ = load('test-A/in.tsv', 'test-A/out.tsv')
    return X_test, X_test_candidates
